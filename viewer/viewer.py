# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for
from flask import request, jsonify
import sys
import json
import glob


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策

@app.context_processor
def filelist():
    # ls data/
    return dict(ls_data=glob.glob("data/*"))

@app.route('/api/<string:jname>', methods=['POST'])
def post_json(jname):
    with open('data/{}'.format(jname), mode = "r", encoding='utf-8') as f:
        f_str = json.load(f)


    jsondata = request.get_json()  # POSTされたJSONを取得
    search_result = {}
    for k, v in f_str.items():   # for/if文では文末のコロン「:」を忘れないように
        if jsondata['data'] in str(v):
            search_result[k] = v
    return jsonify(search_result)  # JSONをレスポンス


@app.route('/')
def top_route():
    return redirect(url_for('json_pp'))


@app.route('/viewer')
def json_pp():
    # URLの?以降を取得。 ( /viewer?file=hogehoge の hogehoge を変数filenameに代入)
    filename = request.args.get('file', default = None, type = str)

    file_json = filename
    try:
        fp_in = open (file_json,encoding='utf-8')
    except:
        # top、未指定の場合。
        return render_template('main.html', json_rows=[{}] )

    json_str = fp_in.read()
    fp_in.close()
    dict_aa = {}
    dict_aa = json.loads(json_str)
    rows = []
    for key in sorted (dict_aa.keys()):
        unit = dict_aa[key]
        unit['id'] = key
        rows.append(unit)

    return render_template('main.html', title=file_json, json_rows=rows)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


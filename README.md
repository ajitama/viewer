# json_viewer

特定の形式のJsonファイルを閲覧するサイト。  
形式はdata/sample.jsonを見てください。  
素早く見やすく検索しやすいものを少ないのコードで書いてみました。  
表の列はJsonファイルのキーを動的に読み込みます。  
  
JqueryのDatatableを使用しサーチと表示件数を変えられます。  
データを一度読み込んだあとに表示を整形するので、  
巨大なファイルを読み込むと遅くなります。  

ドロップダウンのSelectは
サイトを読み込んだときにdataディレクトリを読みに行くので、
ファイルをdataディレクトリに置くだけで動的にメニューに表示してくれます。

centosの場合はetc/systemd/system/viewer.serviceのexec startをいじってください。

  
### require  

Python3 
Python3-pip  
Fedora/Redhat (CentOS7 : yum groupinstall "Development Tools")

### install(first step)

sudo -s (change user. root.)  

cd viewer  
bash install.sh  


### check status
systemctl status viewer  

### start
systemctl start viewer  

### stop
systemctl stop viewer  


### Debug start
python3 viewer/viewer.py  

##  access
http://[server_ip]:5000/  

##  api
http://[server_ip]:5000/api/[filename].json  

- ` curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' -d '{"data":"小山"}' http://localhost:5000/api/cities.json`

```json
{"t0922":{"date_mod":"2003-5-15","name":"小山","population":38756}}
```

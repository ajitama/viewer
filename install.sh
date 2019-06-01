#!/bin/bash

#### !! please exec root !!!
sudo pip3 install flask uwsgi

sudo cp -pr viewer /usr/local/bin/
chmod 777 /usr/local/bin/viewer/data
chmod 777 /usr/local/bin/viewer/static
chmod 777 /usr/local/bin/viewer/templates

sudo cp etc/systemd/system/viewer.service /etc/systemd/system/viewer.service


systemctl daemon-reload
sudo systemctl stop viewer
sudo systemctl start viewer


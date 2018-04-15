#!/usr/bin/python
#coding=utf-8


'''
使用这种方法引入本地的python virtural env
'''
#activate_this = '/Users/pujielan/ENV/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

from flask import Flask, jsonify, request
import sys
import json
import base64
from parse.es_parse import EsParse 
from urllib import unquote
import time

esp = EsParse()

# 用于强制转换为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

#'/root/kod/data/Group/public/home/doc/outInput'

def writeIntoFile(text, title, path="/root/kod/data/Group/public/home/doc/outInput"):
    fileName = "{1}_{2}.html".format(path, title, int(time.time()))
    print fileName
    try:
        with open(path + "/" + fileName, 'w') as f:
            f.write(text)
            f.close()
    except Exception, e:
        print str(e)

@app.route('/es', methods=['POST'])
def parse_es():
    print request
    if request.headers["PW"] != "guojirenzheng123qwe":
        return jsonify({"result":"yes"})
    try:
        plus = request.get_data()
        html = unquote(plus.replace("+"," "))
        htext = "cliper[text]="
        htitle = "&cliper[title]="
        hurl = "&cliper[url]="
        hdata = html.split(htitle)
        text = hdata[0].split(htext)[1]
        title = hdata[1].split(hurl)[0]
        writeIntoFile(text, title)
    except Exception, e:
        print str(e)
        return jsonify({"result":str(e)})
    return jsonify({"result":"success"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

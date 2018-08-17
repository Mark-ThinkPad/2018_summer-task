from flask import Flask, render_template, request, jsonify
from noe_spider import func
from pymongo import MongoClient
from selenium import webdriver
import json
from bson import json_util

app = Flask(__name__)

app.debug = True

client = MongoClient("localhost", 27017)
db = client["mydb"]
col = db["thc"]

def GetInfo(user_id, passwd):
    client = MongoClient("localhost", 27017)
    db = client["mydb"]
    col = db["thc"]
    info = col.find({"user_id":user_id})
    if info.count() == 1:
        if info[0]["passwd"] == passwd:
            return info[0]
        else:
            return False
    elif info.count() == 0:
        info = func(user_id, passwd)
        col.insert(info)
        return info

# 添加一个防止多次插入相同数据的函数(用于储存订阅数据库的数据库), 0表示数据库没有完全一致的一组数据,1表示有
def join_in(user_id, passwd, email):
    client = MongoClient("localhost", 27017)
    db = client["mydb"]
    col = db["join"]
    info = col.find({"user_id":user_id})
    if info.count() == 1:
        if info[0]["passwd"] == passwd:
            if info[0]["email"] == email:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0
    return 0

@app.route('/',methods=["POST","GET"])
def index():
    return render_template("index.html")

@app.route('/join',methods=["POST","GET"])
def remind():
    if request.method == "GET":
        content = "兄弟,你的操作有问题啊"
        return render_template("error.html",content=content)
    elif request.method == "POST":
        # 获取表单数据
        user_id = request.form["username"]
        passwd = request.form["password"]
        email = request.form["email"]
        client = MongoClient("localhost", 27017)

        # 数据库ready
        db = client["mydb"]
        col = db["join"]

        # 防止多次插入相同数据
        content = "QAQ"
        sign_num = join_in(user_id, passwd, email)
        if sign_num == 0:
            infos = {}
            infos["user_id"] = user_id
            infos["passwd"] = passwd
            infos["email"] = email
            col.insert(infos)
            content = "订阅成功"
            return render_template("error.html",content=content)
        elif sign_num == 1:
            content = "你已经订阅过了"
            return render_template("error.html",content=content)
    return render_template("index.html")

@app.route('/info',methods=["POST","GET"])
def showInfos():
    if request.method == "GET":
        content = "兄弟,你的操作有问题啊"
        return render_template("error.html",content=content)
    elif request.method == "POST":
        user_id = request.form["username"]
        passwd = request.form["password"]
        #print(user_id)
        #print(passwd)
        Infos = GetInfo(user_id, passwd)
        return render_template("info.html", content=Infos)
    return render_template("index.html")

@app.route("/api/info",methods=["POST", "GET"])
def api_info():
    if request.method == "GET":
        content = "你没有填数据吧"
        return str({"message":content})
    elif request.method == "POST":
        user_id = request.form["username"]
        password = request.form["password"]
        infos = GetInfo(user_id,password)
        res = jsonify(infos)
        res.headers['Access-Control-Allow-Origin'] = '*'.encode("utf-8").decode("latin1")
        res.headers['Access-Control-Allow-Methods'] = 'POST，GET,OPTIONS'.encode("utf-8").decode("latin1")
        res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'.encode("utf-8").decode("latin1")
        return res


@app.errorhandler(405)
def error(e):
    content = "找不到吧哈哈哈-405"
    return render_template("error.html",content=content)

@app.errorhandler(404)
def error(e):
    content = "找不到略略略-404"
    return render_template("error.html",content=content)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
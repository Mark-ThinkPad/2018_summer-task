# 暑假作业(成绩查询系统)

`嫌github慢去码云呀，码云的链接我不给略略`

---

## 目录

<!-- TOC -->

- [暑假作业(成绩查询系统)](#暑假作业成绩查询系统)
    - [目录](#目录)
    - [开发环境](#开发环境)
    - [介绍(图文)](#介绍图文)
    - [简单说一下这些文件](#简单说一下这些文件)
    - [千万不要看这个介绍!!!这是我一遍写代码一遍记的,基于线性逻辑,可能会看的有点懵](#千万不要看这个介绍这是我一遍写代码一遍记的基于线性逻辑可能会看的有点懵)

<!-- /TOC -->

---

## 开发环境

- **Ubuntu Mate 18.04** *(我就是死, 从这里跳下去, 也不会再用Ubuntu! -"您的系统出现内部错误" 真香!)*

- 这个制作完成的成绩查询系统会被我打包到docker镜像里, 并且会尝试部署在我的阿里云服务器上

- 已经部署在我的阿里云服务器上了, [http://112.74.63.169:80](http://112.74.63.169:80)

---

## 介绍(图文)

1. 前情提示
- 最终成品基于`暑期培训`中的`成绩查询系统`
- 很多新想法的实现来自于`原来代码`的`启发`(俗称`突然醒悟`,`灵光一现`)
2. 网页部分的改动
- 为了达成自动向用户发送邮件的目标,加入`订阅服务`

![p1](http://static.zybuluo.com/Mark201802/zzanc9doowayjxnirwdgfcmz/1.png)

```html
{% extends "base.html" %}
{% block content %}
<form class="info_form" action="/info" method="POST" >
<div class="line" ><div class="key" >学号：</div> <input type="text" name="username" id="username"></div>
<div class="line" ><div class="key" >密码：</div> <input type="password" name="password" id="password"></div>
<div class="center"><input type="submit" value="登录" > </div>
</form>
<div class="line"><font color="dc134c">想自动收到成绩更新的通知邮件吗, 加入订阅服务吧!</font></div>
<form class="info_form" action="/join" method="POST">
<div class="line" ><div class="key" >学号：</div> <input type="text" name="username" id="username"></div>
<div class="line" ><div class="key" >密码：</div> <input type="password" name="password" id="password"></div>
<div class="line" ><div class="key" >邮箱：</div> <input type="email" name="email" id="email"></div>
<div class="center"><input type="submit" value="点击加入订阅服务" ></div>
</form>
{% endblock %}
```

(说了是mac os主题)

- 订阅成功后将会给用户一个`订阅成功`的反馈(这里面其实设计了一个小小的验证函数)

![p2](http://static.zybuluo.com/Mark201802/z4lwf52qpnojg4nscpxsd3fs/2.png)

- 在成绩查询页面添加了绩点(在这里发现原来的的代码中,爬成绩获得的总绩点并没有中括号)

![p3](http://static.zybuluo.com/Mark201802/ry9ejmlishdugqg5cx1gdbfl/4.png)

```html
{% extends "base.html" %}
{% block content %}

        <div class="info" >
            
            <ul class="s_info" > <li class="ss_info" >姓名：</li> <li class="ss_info" > {{content.姓名}}</li>  <li class="ss_info" >学号：</li> <li class="ss_info" > {{content.学号}}</li> <li class="ss_info" >性别：</li> <li class="ss_info" > {{content.性别}}</li> <li class="ss_info" >学制：</li> <li class="ss_info last" > {{content.学制}}</li> </ul>
            <ul class="s_info" > <li class="ss_info" >院系：</li> <li class="ss_info faculty" > {{content.院系}}</li> <li class="ss_info" >专业：</li> <li class="ss_info faculty" > {{content.专业}}</li> <li class="ss_info" >年级：</li> <li class="ss_info last" > {{content.年级}}</li> </ul>
            <ul class="s_info" > <li class="ss_info classroom" >所属班级：</li> <li class="ss_info" > {{content.所属班级}}</li> <li class="ss_info classroom">所属校区：</li> <li class="ss_info">{{content.所属校区}}</li> <li class="ss_info classroom">是否有学籍：</li> <li class="ss_info last ">{{content.是否有学籍}}</li> </ul>
            <ul class="s_info" > <li class="ss_info classroom " >学籍状态：</li> <li class="ss_info" > {{content.学籍状态}}</li> <li class="ss_info">学历层次:</li> <li class=" ss_info">{{content.学历层次}}</li> <li class="ss_info classroom">学生类别：</li>  <li class="ss_info classroom last">{{content.学生类别}}</li> </ul>
        </div>
        <div class="grades" >
        <ul class="grade"><li class="gg_info" >课程名称</li> <li class="ggs_info" >课程时间</li> <li class="g_info" >课程类别</li> <li class="g_info" >学分</li> <li class="g_info" >成绩</li> <li class="g_info last" >绩点</li> </ul>
        
    </div>
    {% for grade in content.成绩 %}

    <ul class="grade"><li class="gg_info" >{{grade.课程名称}}</li>  <li class="ggs_info" >{{grade.学年学期}}</li> <li class="g_info" >{{grade.课程类别}}</li> <li class="g_info" >{{grade.学分}}</li> <li class="g_info" >{{grade.最终}}</li> <li class="g_info last" >{{grade.绩点}}</li></ul>
    {% endfor %}

    <div class="grades" >
            <ul class="grade"><li class="gg_info" >学年度</li> <li class="ggs_info" >学期</li> <li class="g_info" >必修门数</li> <li class="g_info" >必修总学分</li> <li class="g_info" >平均绩点</li></ul>
    </div>

    {% for point in content.绩点 %}

    <ul class="grade"><li class="gg_info" >{{point.学年度}}</li>  <li class="ggs_info" >{{point.学期}}</li> <li class="g_info" >{{point.必修门数}}</li> <li class="g_info" >{{point.必修总学分}}</li> <li class="g_info" >{{point.必修平均绩点}}</li></ul>
    {% endfor %}

    <div class="grades" >
            <ul class="grade"><li class="gg_info" >类型</li> <li class="ggs_info" >必修门数</li> <li class="g_info" >必修总学分</li> <li class="g_info" >平均绩点</li></ul>
    </div>

    {% for all_point in content.总绩点 %}

    <ul class="grade"><li class="gg_info" >{{all_point.类型}}</li> <li class="ggs_info" >{{all_point.必修门数}}</li> <li class="g_info" >{{all_point.必修总学分}}</li> <li class="g_info" >{{all_point.必修平均绩点}}</li></ul>
    {% endfor %}

{% endblock %}
```

3. 后端部分的改动(这里面能说的就比较多了)(以订阅服务的逻辑为顺序)
- 首先是为了方便管理,需要把订阅的用户数据放在数据库里, 最好是放在另一个数据集合,方便后期处理
- 那么从网页段读取用户输入的内容插入到数据库就有一个小问题了, 万一插入了几个内容一样的数据文档呢, 岂不是浪费服务器资源, 于是想出了以下代码(在`app.py`中)

```python
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
```

```python
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
```

返回状态值这个方法有些老套, 但是我比较熟悉这个方法, 添加订阅数据就这么搞定了

- 接下来是重头戏, 发邮件(我建立了一个技术验证文件夹来实验核心技术)

(1)使用SMTP发送邮件的模板比较好找, 在这里不多介绍, 发送邮件单独封装成一个函数

```python
# 把技术验证文件夹测试成功的发送HTML内容邮件代码做成一个邮件发送函数, 
def send(user_id, passwd, email, content):
    
    # 发件人和收件人
    sender = "13297196312@163.com"
    receiver = email
    
    # 所使用的用来发送邮件的SMTP服务器
    smtpserver = "smtp.163.com"
    
    # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
    username = "13297196312@163.com"
    password = "82324598232929ac"
    
    # 邮件主题(这个邮件主题应该加个颜文字卖卖萌的)
    mail_title = "成绩更新通知邮件"

    # 安排邮件内容
    mail_body = content

    # 邮件内容, 格式, 编码
    message = MIMEText(mail_body, 'html', 'utf-8')
    message['From'] = sender # 发件人
    message['To'] = receiver # 收件人
    message['Subject'] = Header(mail_title, 'utf-8')

    try:
        smtp = smtplib.SMTP_SSL("smtp.163.com",465)
        #print("1")
        #smtp.connect(smtpserver)
        #print("2")
        smtp.login(username, password)
        #print("3")
        smtp.sendmail(sender, receiver, message.as_string())
        #print("4")
        smtp.quit()
        print("发送邮件成功")
    except smtplib.SMTPException:
        print("发送邮件失败")
```

(2)把生成内容的代码单独封装成一个函数, 方便我给用户发点别的东西(马上就知道了)

```python
# 把生成邮件内容单独分离出来作为一个函数, 为密码纠错的功能让步
def words(user_id, passwd):
    # 使用储存成绩的collection
    #client = MongoClient("localhost", 27017)
    #db = client["mydb"]
    #col = db["thc"]

    # 安排邮件内容
    grade = {}
    grade = GetInfo(user_id, passwd)
    content = """
    <style type="text/css">table{text-align: center;border-collapse:collapse;border: 3px solid;}td,th{border-color: pink;border: 1px solid;}</style><table style="text-align: center;"><tr><th>课程名称</th><th>课程时间</th><th>课程类别</th><th>学分</th><th>最终成绩</th><th>绩点</th></tr>
    """

    base = """
    <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></td>
    """

    for cj in grade.get("成绩"):
    #print(grade.get("成绩"))
    #print(cj)
        content=content+base.format(cj["课程名称"],cj["学年学期"],cj["课程类别"],cj["学分"],cj["总评成绩"],cj["绩点"])
    content = content + "</table>"

    extra = """
    <style type="text/css">table{text-align: center;border-collapse:collapse;border: 6px solid;}td,th{border-color: green;border: 2px solid;}</style><table style="text-align: center;"><tr><th>学年度</th><th>学期</th><th>必修门数</th><th>必修总学分</th><th>必修平均绩点</th></tr>
    """
    extra_base = """
    <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></td>
    """
    for jd in grade.get("绩点"):
        extra = extra + extra_base.format(jd["学年度"],jd["学期"],jd["必修门数"],jd["必修总学分"],jd["必修平均绩点"])
    content = content + extra + "</table>"

    another = """
    <style type="text/css">table{text-align: center;border-collapse:collapse;border: 3px solid;}td,th{border-color: pink;border: 1px solid;}</style><table style="text-align: center;"><tr><th>类型</th><th>必修门数</th><th>必修总学分</th><th>必修平均绩点</th></tr>
    """
    another_base = """
    <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></td>
    """
    for zjd in grade.get("总绩点"):
        another = another + another_base.format(zjd["类型"],zjd["必修门数"],zjd["必修总学分"],zjd["必修平均绩点"])
    content = content + another + "</table>"

    return content
```

我先老实交代了,用了苏金鹏的HTML内容自动生成代码,并未获得他的同意,但是我自己尝试自己写一个出来,emmm,最后还是用了他的

(3)接下来是编写更新成绩的代码

- 首先我加入了一段密码纠错的代码, 同时整合了成绩数据自动补全的功能, 上面埋下的伏笔就在这里

```python
# 密码纠错功能(整合自动补全成绩信息数据库功能)(其实也可以封装成一个函数的)
# 先切换一下数据集合
col = db["thc"]
# 实现成绩信息自动补全
info_find = col.find({"user_id":user_id})
if info_find.count() == 0:
    try:
        info_add = func(user_id, passwd)
        col.insert(info_add)
        print("学号为{}的成绩数据添加成功".format(user_id)) # 添加成功表明了学号和密码都是正确的
    except:
        content = """
        <h1>您在订阅服务中输入的学号或密码有误,请返回成绩查询系统重新订阅(本消息只发送一次,这个错误的订阅数据将会被删除)</h1>
        """
        send(user_id, passwd, email, content)
        # 切换数据集合删东西啦啦啦
        col = db["join"]
        target = col.find({"user_id":user_id})
        target_id = target[0]["_id"]
        col.remove({'_id':target_id})
        print("错误订阅数据删除成功")
        continue # 直接去下一次循环咯
        # 接下来利用成绩数据库验证密码
elif info_find.count() == 1:
    col = db["thc"]
    if info_find[0]["passwd"] != passwd:
        content = """
        <h1>您在订阅服务中输入的学号或密码有误,请返回成绩查询系统重新订阅(本消息只发送一次,这个错误的订阅数据将会被删除)</h1>
        """
        send(user_id, passwd, email, content)
        # 切换数据集合删东西啦啦啦
        col = db["join"]
        target = col.find({"user_id":user_id})
        target_id = target[0]["_id"]
        col.remove({'_id':target_id})
        print("错误订阅数据删除成功")
        continue # 直接去下一次循环咯
    elif info_find[0]["passwd"] == passwd:
        print("学号为{}的订阅用户密码验证通过".format(user_id))
```

- 检查邮件更新并发送邮件就是小意思了

```python
# 写一个自动从数据库遍历订阅用户, 并判断成绩是否更新的函数, 有更新就调用发送邮件的函数
def update():
    # 先使用储存订阅用户的数据库
    client = MongoClient("localhost", 27017)
    db = client["mydb"]
    col = db["join"]

    # 遍历所有订阅用户,取出必要的数据
    for info in col.find():
        #print(info)
        user_id = info["user_id"]
        passwd = info["passwd"]
        email = info["email"]

        # 密码纠错功能(整合自动补全成绩信息数据库功能)(其实也可以封装成一个函数的)
        # 先切换一下数据集合
        col = db["thc"]
        # 实现成绩信息自动补全
        info_find = col.find({"user_id":user_id})
        if info_find.count() == 0:
            try:
                info_add = func(user_id, passwd)
                col.insert(info_add)
                print("学号为{}的成绩数据添加成功".format(user_id)) # 添加成功表明了学号和密码都是正确的
            except:
                content = """
                <h1>您在订阅服务中输入的学号或密码有误,请返回成绩查询系统重新订阅(本消息只发送一次,这个错误的订阅数据将会被删除)</h1>
                """
                send(user_id, passwd, email, content)
                # 切换数据集合删东西啦啦啦
                col = db["join"]
                target = col.find({"user_id":user_id})
                target_id = target[0]["_id"]
                col.remove({'_id':target_id})
                print("错误订阅数据删除成功")
                continue # 直接去下一次循环咯
                # 接下来利用成绩数据库验证密码
        elif info_find.count() == 1:
            col = db["thc"]
            if info_find[0]["passwd"] != passwd:
                content = """
                <h1>您在订阅服务中输入的学号或密码有误,请返回成绩查询系统重新订阅(本消息只发送一次,这个错误的订阅数据将会被删除)</h1>
                """
                send(user_id, passwd, email, content)
                # 切换数据集合删东西啦啦啦
                col = db["join"]
                target = col.find({"user_id":user_id})
                target_id = target[0]["_id"]
                col.remove({'_id':target_id})
                print("错误订阅数据删除成功")
                continue # 直接去下一次循环咯
            elif info_find[0]["passwd"] == passwd:
                print("学号为{}的订阅用户密码验证通过".format(user_id))
        
        # 检查成绩更新
        # 再把数据集合切回来
        col = db["thc"]
        # 获取当前最新成绩
        info_new = func(user_id, passwd)
        # 对比成绩信息
        if info_new["成绩"] != info_find[0]["成绩"]:
            # 更新数据库,使用先删除再插入的方法暴力更新
            info_target = col.find({"user_id":user_id})
            info_target_id = target[0]["_id"]
            col.remove({'_id':info_target_id})
            col.insert(info_new)
            # 生成HTML成绩表格
            content = words(user_id, passwd)
            # 发送成绩更新通知邮件
            send(user_id, passwd, email, content)
        elif info_new["成绩"] == info_find[0]["成绩"]:
            print("学号为{}的成绩数据没有更新".format(user_id))
        # 一切都结束了(中二脸),我要回去写文档了(正经脸)
```

- 最后就是让这个update函数定时运行了,没选什么花里胡哨的方案,sleep就是了

```python
# 不,前辈,我还有一件事需要拜托(中二脸) -"我需要定时运行!"
def main():
    # 使用time.sleep来控制成绩更新的间隔时间
    while 1:
        update()
        time.sleep(7200) # 每两小时执行一次, 如果服务器扛不住的话就把时间设置的长一点吧

# 我真的去写文档了
main()
```

4. 鉴于大家的成绩都已经更新完了, 订阅服务`join.py`的代码并没有能够完整的测试, 至少是沿着我的思路来做的, 下面放出技术验证阶段时实验成功的发送成绩邮件截图

![p4]( http://static.zybuluo.com/Mark201802/xk5mdry02qgkffbkg9kppp44/3.png)

- 这里的接收邮箱是我们长大的教育邮箱(我拿来白嫖一些东西用的,比如office365什么的), 本质上是腾讯企业邮箱, table表格的边框被没有渲染出来(Chrome 68 on Ubuntu Mate 18.04)(手机客户端同样)

![p5](http://static.zybuluo.com/Mark201802/940reyghbad9kcuzh3jtgwo3/image_1cjsf6guq1atg8b71crt17aj1gro1k.png)

![p6](http://static.zybuluo.com/Mark201802/9kzlc7pp6gfvmfay5vixhb6y/image_1cjsf90tku3p1t9d3n86p411ci21.png)

- 然后我在发送邮箱里看发件箱的时候画风突变(手机客户端同样), 发送邮箱采用的是网易邮箱, 这锅, 先让腾讯背吧(笑)

---

## 简单说一下这些文件

- `app.py` 主程序, 运行网站就靠它
- `neo_spider.py` 提供爬取成绩的函数
- `join.py` 订阅服务独立组件, 可单独运行, 方便后期的维护和调试
- `templates文件夹` 放HTML文件用的
- `static/css文件夹` 放CSS文件用的

---

## 千万不要看这个介绍!!!这是我一遍写代码一遍记的,基于线性逻辑,可能会看的有点懵

- 本质上是对暑期培训中的成绩查询系统进行添加和修改(`app.py`和静态网页部分根据功能进行了修改添加,数据库的总绩点加了个中括号)
- 看了苏金鹏的github库(#手动滑稽)
- 采用添加订阅服务的方案(支持自定义学号和邮箱)
- 订阅服务是一个后期添加的独立组件, 订阅网页只是通过把学号,密码,邮箱这三个参数插入到数据库里
- 自动发送邮件中使用了苏金鹏的HTML生成代码, 根据这段代码增加了绩点推送功能,并且纠正了原爬虫中的一个小问题(没有加入`all_points = []`)
- 成绩查询页面添加了总绩点(`Ctrl C` + `Ctrl V`)
- `技术验证文件夹`没什么好看的, 只是为了探索SMTP和生成HTML内容用的, 加入`数据库`和`sleep`操作便是`join.py`订阅服务的独立组件
- `订阅功能`里为了加入所有订阅用户都能(被)使用的密码纠错功能, 添加了数据库自动补全功能(后来仔细想了一下,密码输错还是没有学号输错可怕)
- 调试订阅功能?不存在的,成绩早就更新完了

---


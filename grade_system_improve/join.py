from pymongo import MongoClient
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from noe_spider import func
from app import GetInfo
import time

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

# 不,前辈,我还有一件事需要拜托(中二脸) -"我需要定时运行!"
def main():
    # 使用time.sleep来控制成绩更新的间隔时间
    while 1:
        update()
        time.sleep(7200) # 每两小时执行一次, 如果服务器扛不住的话就把时间设置的长一点吧

# 我真的去写文档了
main()
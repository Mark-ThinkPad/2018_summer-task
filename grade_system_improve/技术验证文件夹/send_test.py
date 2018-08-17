import smtplib
from email.header import Header
from email.mime.text import MIMEText
from pymongo import MongoClient
 
# 发件人和收件人
sender = "13297196312@163.com"
receiver = "201703407@yangtzeu.edu.cn"
 
# 所使用的用来发送邮件的SMTP服务器
smtpserver = "smtp.163.com"
 
# 发送邮箱的用户名和授权码（不是登录邮箱的密码）
username = "13297196312@163.com"
password = "82324598232929ac"
 
# 邮件主题
mail_title = "成绩更新通知邮件"
 
# 安排HTML内容
client = MongoClient("localhost", 27017)
db = client["mydb"]
col = db["thc"]
info = col.find({"user_id":"201703407"})
grade = {}
if info[0]["passwd"] == "201703407":
    grade = info[0]
#print(grade)
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

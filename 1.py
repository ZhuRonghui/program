#coding=utf-8
import smtplib
from email.mime.text import MIMEText
msg_from = '1602445598@qq.com'
passwd='eotkcyqzjjkubaaf'
msg_to='1602445598@qq.com'

subject='2018144126朱蓉辉的第一次作业'
content='(Wifi)ip_nat:10.101.9.236;ip:220164.161.128\n(数据)ip_nat:10.83.33.221;ip:172.69.34.157'
msg=MIMEText(content)
msg['subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from,passwd)
    s.sendmail(msg_from,msg_to,msg.as_string())
    print("发送成功")
except(s.esmtp_features,e):
    print("发送失败")
finally:
    s.quit()

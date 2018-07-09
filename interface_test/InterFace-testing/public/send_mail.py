#coding:utf-8
import smtplib
import time

from email.mime.text import MIMEText
from email.header import Header
import os
def send_email():
    to_list=['luyuexin@zjipst.com']
    from_mail='luyuexin@zjipst.com'
    host_addr='mail.zjipst.com'
    username='luyuexin@zjipst.com'
    passwd='Lu123456'

    message=MIMEText(u'接口自动化测试','plain','utf-8')
    message['from']=Header("wo",'utf-8')
    message['To']=Header("ni",'utf-8')
    subject='Python Smtp 邮件测试'
    message['Subject']=Header(subject,'utf-8')

    e=smtplib.SMTP()
    e.connect(host_addr,port=25)
    e.login(username,passwd)
    e.sendmail(from_mail,to_list,message.as_string())
    e.quit()
    
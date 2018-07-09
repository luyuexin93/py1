# coding:utf-8
from email.mime.text import MIMEText
from email.header import Header
import smtplib

msg=MIMEText('hello ,send by Python...','plain','utf-8')
subject='python email test'
msg['Subject']=Header(subject,'utf-8')  
from_addr = 'luyuexin@zjipst.com'
password = 'Lu123456'
to_addr = 'luyuexin@zjipst.com'
smtp_server='mail.zjipst.com'

#server = smtplib.SMTP()
server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.set_debuglevel(1)

server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
#server.connect(smtp_server)
#server.login(from_addr,password)
#server.sendmail(from_addr,[to_addr],msg.as_string())
#server.quit()


#coding:utf-8
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
import os

def send_email(filename):
    to_list=['luyuexin@zjipst.com'] #收件人列表
    from_mail='luyuexin@zjipst.com' #发件人邮箱
    host_addr='mail.zjipst.com'     #stmp 邮件发件服务器
    username='luyuexin@zjipst.com'  #登录名
    passwd='Lu123456'                #密码


    #ps  邮件发送正文html内容 可能不支持javascript功能查看，页面显示不完整 不推荐
    # # 读取hmtl测试报告内容
    # f=open(file,'rb')
    # mail_body=f.read()
    # f.close()

    # 定义邮件头部信息
    message=MIMEMultipart()
    message['from']=Header("python_Auto",'utf-8')  #Header 定义 媒体类型，字符集编码等
    message['To']=Header("luyuexin",'utf-8')
    subject=u'Python Smtp 邮件测试'    #定义邮件主题
    message['Subject']=Header(subject,'utf-8')
    message.attach(MIMEText(u'附件是接口测试执行报告','plain','utf-8')) #定义邮件内容正文文本

    # 采用附件方式发送html报告

    with open(filename, 'rb') as f:
        # MIMEBase表示附件的对象
        mime = MIMEBase('text', 'txt', filename=filename)
        # filename是显示附件名字
        mime.add_header('Content-Disposition', 'attachment', filename=u'接口测试报告.html')
        # 获取附件内容
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        # 作为附件添加到邮件
        message.attach(mime)

    # message.attach(MIMEText(u'接口测试记录', 'plain', 'utf-8'))
    # file = MIMEBase('text','html')
    # file.set_payload(open(filename,'rb').read())
    # file.add_header('Content-Dispostion','attachment')
    # message.attach(file)

# 连接到stmp服务器 登录并发件
    e=smtplib.SMTP()              #创建stmplib连接对象
    e.connect(host_addr,port=25)  #连接stmp发件服务器
    e.login(username,passwd)
    e.set_debuglevel(1)  # 设置set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
    e.sendmail(from_mail,to_list,message.as_string())
    e.quit()

# if __name__=='__main__':
#     send_email()
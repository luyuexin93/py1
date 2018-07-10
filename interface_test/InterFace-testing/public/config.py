#coding:utf-8
import configparser
import os

def get_conf():
    conf_file = configparser.ConfigParser()
    #conffilepath=os.path.join(os.getcwd(),'conf.ini')
    #print(conffilepath)
    project_dir = (os.path.dirname(os.path.dirname(__file__)))  # 获取当前项目目录路径
    file_dir = project_dir + r'/public/'  # 定义测试报告生成目录
    conffilepath = os.path.join(file_dir, 'conf.ini')
    conf_file.read(conffilepath)
    conf={}
    conf['sender'] = conf_file.get("email","sender")
    conf['receiver']=conf_file.get("email","receiver")
    conf['smtpserver'] = conf_file.get("email","smtpserver")
    conf['username'] = conf_file.get("email","username")
    conf['password']=conf_file.get("email","password")
    return conf

if __name__ == "__main__":
    print(get_conf())
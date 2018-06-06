#coding:utf-8
import requests
import json

#get方法
#test_url ='http://www.baidu.com'
#response = requests.get(test_url)
#result = response.text
#print(result)

#post方法

url= "http://host:port/path"
datalist={"usr":"user","passwrod":"password"}
head={"Content-Type":"application/json"}
#通过json.dumps（data）方法将字典转为json格式
response=requests.post(url,data=json.dumps(datalist),headers=head)
#response.encoding ='utf-8'
result = response.text
print(response.headers)
print(result)
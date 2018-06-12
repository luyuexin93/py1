#coding:utf-8
#by python3
import cx_Oracle
#设定连接oracle字符集简体中文
import  os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
#连接数据库 （user/password@ip:port/instance）
conn = cx_Oracle.connect("zjipst110/zjipst110@10.10.10.183:1521/racdb")
cursor = conn.cursor()
sql="select * from jjd_jjd where jjdbh='3301001806124000007'"
result=cursor.execute(sql)

#获取数据表列名，并输出
title=[i[0] for i in cursor.description] #列表生成式 description 包含表字段名 类型长度 是否为空等信息
#打印列名 %-20s 减号表示左对齐，20表示占20字符长度
g= lambda k:"%-20s" %k
title=map(g,title)
for i in title:
    print(i,end='')
print()
#输出查询结果
for i in result.fetchall():
    for k in map(g,i):
        print(k,end='')
    print()
#关闭数据库连接
cursor.close()
conn.close()


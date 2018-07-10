#python 接口自动化 尝试

###依赖包说明
    - requests 模拟http请求 用于接口测试
    - email smtplib 自带 用于收发邮件
    - HTMLtestrunner 配合unittest 生成html报告 需下载
    - unittest 自带 python单元测试库
    - configparser 自带 用于读取.ini配置文件并存到字典


>2018-07-09

 1. 完成HTMLtestrunner email 代码demo 调试
 2. 接口测试框架主体待完成。。
 

HTMLtestrunner 默认Python2 版本 适配python3
[参考](https://www.cnblogs.com/my-blogs-for-everone/p/6058390.html) 

[python接口自动化样例](https://blog.csdn.net/sxyzwq/article/details/62039952?locationNum=1&fps=1)

>2018-07-10

1. 完成基本框架部分，htmltestrunner基本调用testcase下测试集 生成html报告
2. 修改send_mail函数完成html测试报告邮件附件发送
3. 增加引用configparser，读取配置文件conf.ini 实现邮件参数隔离
4. 待完成
   - 接口测试主体 requests及unittest包熟悉，接口代码实现
   - 实现测试报告保存到excel文件
   - 连接数据库后断言结果
   - HTMLtestrunner 生成的html页面 美化。。。（优先级最低）
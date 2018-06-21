# -*- coding:utf-8 -*-
def fact(n):      #doctest ex  文档测试 如果允许测试结果正常 没有输出
    '''
    Calculate 1*2*...*n
    >>> fact(1)            #解释器执行函数
    1
    >>> fact(-1)
    Traceback (most recent call last):
    ...                    #... 表示省略的输出
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n*fact(n-1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
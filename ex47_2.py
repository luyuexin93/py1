# -*- coding:utf-8 -*-

def compare(x,y):
    """
    >>> compare(3,5)
    1
    >>> compare(4,6)
    1
    """
    if x > y:
        print "yes"
        return 0
    else:
        print "No"
        return 1

if __name__=='__main__':
    import doctest
    doctest.testmod()
    
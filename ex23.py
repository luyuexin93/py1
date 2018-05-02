from _ast import Num
from PIL.ImImagePlugin import number
import numbers
i=0
numbers=[]
while i<6:
    print "At the top i is %d" %i
    numbers.append(i)
    i=i+1
    print "Numbers now:",numbers
    print "At the bottom i is %d" %i
    
print "The numbers:"

for num in numbers:
    print num

def MyLoop(x):
    i=0
    n=x
    numbers=[]
#***    
    while i < n:
        numbers.append(i)
        print numbers
        print "at the bottom is %d" %numbers[i]
        i=i+1
        print n,i
    for num in numbers:
        print num
#i < n argument type must be integer        
n=int(raw_input("please input a num: "))
#***
MyLoop(n)


#-*- coding:utf-8 -*-
# ex48_2 only function

# def convert_number(s):
#     try:
#         num=int(s)
#         return True
#          
#     except ValueError:
#             return False
        
def scan(sentence):
    direction=('north','south','east')
    verb=('go','kill')
    stop=('in','of','stop','the')
    nouns=('bear','princess')
    result=[]
    word=sentence
    words=word.split()
    for i in words:
        if i in direction:
            result.append(('direction',i))
        elif i in verb:
            result.append(('verb',i))
        elif i in stop:
            result.append(('stop',i))
        elif i in nouns:
            result.append(('nouns',i))
        else :
            try:
                num=int(i)
                result.append(('num',num))
            except:
                result.append(('error',i))
    return result
    
    
result=scan("north go 99h 88") 
print result         
            
                
                
        
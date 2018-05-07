#-*- coding:utf-8 -*-

class lexicon(object):
    def __init__(self):
        self.direction=('north','south','east')
        self.verb=('go','kill','eat')
        self.stop=('in','of','the')
        self.nouns=('bear','princess')
        self.result=[]
    
    def convert_number(self,s):
        try:
            self.num=int(s)
            return True
        
        except ValueError:
            return False
       
    def scan(self,word):
        self.word=word
        self.words=word.split()
        for i in self.words:
            if i in self.direction:
                self.result.append(('direction',i))
            elif i in self.verb:
                self.result.append(('verb',i))
            elif i in self.stop:
                self.result.append(('stop',i))
            elif i in self.nouns:
                self.result.append(('noun',i))
            else :
                if self.convert_number(i):
                    self.num=int(i)
                    self.result.append(('number',self.num))
                else:
                    self.result.append(('error',i))
        return self.result

# g=lexicon()
# result=g.scan("north 44 999h") 
# print result         
            
                
                
        

class ParserError(Exception):
    pass
# def test(wordlist,num):
#     
#     while wordlist[-1]==int(num):
#         word=wordlist.pop()
#         return word
#     
# print test([9,1,2,3],3)
        
def peek(word_list):
    if word_list:
            word=word_list[0]
            return word[0]
    else:
            return None
   
def match(word_list,expecting):
    if word_list:
        word=word_list.pop(0)
             
        if word[0]==expecting:
            return word
        else :
            return None
    else:
        return None
       
# def skip(word_list,word_type):
#     while peek(word_list) == word_type:
#         if word_list:
#             word=word_list.pop()
#             
#             if word[0]==word_type:
#                 return word
#             else :
#                 return None
#         else:
#             return None 


def skip(word_list,word_type):
    while peek(word_list) == word_type:
         match(word_list,word_type)   
              
#print skip([('stop','go'),('verb','g'),('verb','g')],'verb') 

def parse_verb(word_list):
    skip(word_list,'stop')
    if peek(word_list)=='verb':
        return match(word_list,'verb')
    else:
        raise ParserError("Expected a verb next")

word1=[('stop','g'),('verb','g2'),('verb','p')]
verb = parse_verb(word1)        
print verb  
        
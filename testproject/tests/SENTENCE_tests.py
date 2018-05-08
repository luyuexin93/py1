from nose.tools import *
import sys
sys.path.append('D:/workplace/ex47')
from ex48 import lexicon
import ex49
from ex49 import *

# class Sentence(object):
# #     def __init__(self,subject,verb,object):
# #     #remeber we take ('noun','princess')tuples and convert them
# #         self.subject=subject[1]
# #         self.verb=verb[1]
# #         self.object=object[1]
def setup():
    print "begin test"

def test_Sentence():
    word=Sentence(('noun','dog'),('verb','go'),('direction','down'))
    assert_equal(word.subject,'dog')
    assert_equal(word.verb,'go')
    assert_equal(word.object,'down')
#         
#     def peek(word_list):
#         if word_list:
#             word=word_list[0]
#             return word[0]
#         else:
#             return None

def test_peek():
    
    word1=[('verb','go')]
    word2=[('verb','go'),('direction','down')]
    word3=[]
    assert_equal(peek(word1),'verb')
    assert_equal(peek(word2),'verb')
    assert_equal(peek(word3),None)
#     
#     def match(word_list,expecting):
#         if word_list:
#             word=word_list.pop(0)
#             
#             if word[0]==expecting:
#                 return word
#             else :
#                 return None
#         else:
#             return None
def test_match():
    word1=[('verb','go')]
    word2=[]
    assert_equal(ex49.match(word1,'verb'),('verb','go')) 
    assert_equal(ex49.match(word1,'direction'),None)
    assert_equal(ex49.match(word2,'verb'),None)
#     def skip(word_list,word_type):
#         while peek(word_list) == word_type:
#             match(word_list,word_type) 

def test_skip():
    word1=[('verb','go')]
    word2=[]
    assert_equal(peek(word1),'verb')
    assert_equal(skip(word1,'verb'),None)
               
#     def parse_verb(word_list):
#         skip(word_list,'stop')
#         
#         if peek(word_list)=='verb':
#             return match(word_list,'verb')
#         else:
#             raise ParserError("Expected a verb next")
def test_parse_verb():
    word1=[('stop','g'),('verb','go'),('verb','g')]
    word2=[('stop','g'),('direction','up'),('stop','down')]
    word3=[('verb','go')]
    word4=[('verb','down'),('verb','go')]
    word5=[('direction','down'),('verb','g')]
    assert_equal(parse_verb(word1),('verb','go'))
    assert_raises(ParserError,parse_verb,word2)
    assert_equal(parse_verb(word3),('verb','go'))
    assert_equal(parse_verb(word4),('verb','down'))
    assert_raises(ParserError,parse_verb,word5)

    
   
#     def parse_object(word_list):
#         skip(word_list,'stop')
#         next = peek(word_list)
#         
#         if next == 'noun':
#             return match(word_list,'noun')
#         if next == 'direction':
#             return match(word_list,'direction')
#         else:
#             raise ParserError("Expected a noun or direction ")

def test_parse_object():
    word1 = [('stop','g'),('noun','cake'),('verb','g')]
    word2 = [('stop','g'),('direction','up'),('stop','down')]
    word3 = [('noun','cake')]
    word4 = [('direction','down')]
    word5 = [('verb','down'),('verb','go')]
    word6 = [('direction','down'),('verb','g')]
    assert_equal(parse_object(word1),('noun','cake'))
    assert_equal(parse_object(word2),('direction','up'))
    assert_equal(parse_object(word3),('noun','cake'))
    assert_equal(parse_object(word4),('direction','down'))
    assert_raises(ParserError,parse_object,word5)
    assert_equal(parse_object(word6),('direction','down'))

#     def parse_subject(word_list,subj):
#         verb=parse_verb(word_list)
#         obj=parse_object(word_list)
#         
#         return Sentence(subj,verb,obj)

def test_parse_subject():
    word1=[('verb','go'),('noun','cake'),('direction','right')]
    subj=('noun','jack')
    g=parse_subject(word1,subj)
    assert_equal(g.subject,'jack')
    assert_equal(g.verb,'go')
    assert_equal(g.object,'cake')
    
    
#     def parse_sentence(word_list):
#         skip(word_list,'stop')
#         start=peek(word_list)
#         
#         if start == 'noun':
#             subj=match(word_list,'noun')
#             return parse_subject(word_list,subj)
#         elif start =='verb':
#             # assume the subject is the player then
#             return parse_subject(word_list,('noun','player'))
#         else:
#             raise ParserError("Must start with subject,object,or verb not : %s" %start)

def test_parse_sentence():
    word1=[('verb','go'),('noun','cake'),('direction','right')]
    word2=[('noun','cake'),('verb','go'),('direction','right')]
    word3=[('direction','right'),('noun','cake'),('verb','go')]
    g=Sentence(('noun','player'),('verb','go'),('noun','cake'))
    g2=Sentence(('noun','cake'),('verb','go'),('direction','right'))
    assert_equal(parse_sentence(word1).__dict__,g.__dict__)
    assert_equal(parse_sentence(word2).__dict__,g2.__dict__)
    assert_raises(ParserError,parse_sentence,word3)



         
#         
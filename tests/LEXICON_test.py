from nose.tools import *
import sys
sys.path.append('D:/workplace/ex47')
from ex48 import lexicon

def test_directions():
    word1=lexicon()
    assert_equal(word1.scan("north"),[('direction','north')])
    word2=lexicon()
    result = word2.scan("north south east")
    assert_equal(result,[('direction','north'),
                         ('direction','south'),
                         ('direction','east')])
def test_verbs():
    word1=lexicon()
    assert_equal(word1.scan("go"),[('verb','go')])
    word2=lexicon()
    result = word2.scan("go kill eat")
    assert_equal(result,[('verb','go'),
                         ('verb','kill'),
                         ('verb','eat')])

def test_stops():
    word1=lexicon()
    assert_equal(word1.scan("the"),[('stop','the')])
    word2=lexicon()
    result = word2.scan("the in of")
    assert_equal(result,[('stop','the'),
                         ('stop','in'),
                         ('stop','of')])

def test_nouns():
    word1=lexicon()
    assert_equal(word1.scan("bear"),[('noun','bear')])
    word2=lexicon()
    result = word2.scan("bear princess")
    assert_equal(result,[('noun','bear'),
                         ('noun','princess')])

def test_numbers():
    word1=lexicon()
    assert_equal(word1.scan("1234"),[('number',1234)])
    word2=lexicon()
    result = word2.scan("3 91234")

def test_errors():
    word1=lexicon()
    assert_equal(word1.scan("ASDFADFASDF"),[('error','ASDFADFASDF')])
    word2=lexicon()
    result=word2.scan("bear IAS princess")
    assert_equal(result,[('noun','bear'),
                         ('error','IAS'),
                         ('noun','princess')])
                 
from nose.tools import assert_equal
from nose.tools import assert_raises
from ex48.parser import Sentence, ParserError

def test_init():
    testSen = Sentence()
    assert_equal(hasattr(testSen, 'subject'), False)
    assert_equal(hasattr(testSen, 'verb'), False)
    assert_equal(hasattr(testSen, 'object'), False)
    
def test_peek():
    testSen = Sentence()
    peeked = testSen.peek([('verb', 'run'), ('direction', 'north')])
    assert_equal(peeked, 'verb')
    
def test_peek_empty():
    testSen = Sentence()
    peeked_none = testSen.peek([])
    assert_equal(peeked_none, None)
    
def test_match():
    testSen = Sentence()
    word_list = [('noun', 'dragon'),('verb', 'run')]
    matched = testSen.match(word_list, 'noun')
    
    assert_equal(matched, 'dragon')
    assert_equal(word_list, [('verb', 'run')]) # popped
    
def test_skip():
    testSen = Sentence()
    word_list = [('verb', 'kill'), ('stop', 'a'), ('noun', 'goblin')]
    
    testSen.skip(word_list, 'verb')
    assert_equal(word_list, [('stop', 'a'), ('noun', 'goblin')])
    
def test_skip_multi():
    testSen = Sentence()
    word_list = [('stop','in'),('stop', 'a'),('noun','fortress')]
    
    testSen.skip(word_list, 'stop')
    assert_equal(word_list, [('noun','fortress')])
    
def test_parse_verb():
    testSen = Sentence()
    word_list = [('verb', 'kill'), ('stop', 'an'), ('noun', 'orc')]
    
    testSen.parse_verb(word_list)
    assert_equal(testSen.verb, 'kill')
    
    
def test_parse_verb_exceptions():
    testSen = Sentence()
    word_list = [('noun', 'orc'), ('verb','escapes')]
    
    # with only exception param, assert_raises works as context manager
    # make sure method throws a proper exception:
    with assert_raises(ParserError):
        testSen.parse_verb(word_list)
    
def test_parse_object():
    testSen = Sentence()
    word_list = [('stop', 'an'),('noun', 'orc')]
    
    testSen.parse_object(word_list)
    assert_equal(testSen.object, 'orc')

def test_parse_object_exceptions():
    testSen = Sentence()
    word_list = [('verb', 'yell'), ('stop', 'for'), ('noun', 'help')]
    
    # next function call should raise an exception
    with assert_raises(ParserError):
        testSen.parse_object(word_list)

    
def test_parse_subject():
    testSen = Sentence()
    word_list = [('noun','Aragorn'),('verb', 'kills'), ('stop', 'an'), ('noun', 'orc')]
    
    testSen.parse_subject(word_list)
    assert_equal(testSen.subject, 'Aragorn')
    
def test_parse_subject_exceptions():
    testSen = Sentence()
    # some bullshit value to bypass defaulting to 'player'
    word_list = [('crap', 'rotfl'), ('stop', 'an'), ('noun', 'orc')]
    
    with assert_raises(ParserError):
        testSen.parse_subject(word_list)
    
def test_parse_sentence():
    pass
    
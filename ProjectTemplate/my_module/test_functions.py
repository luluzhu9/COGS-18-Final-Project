"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

import string
from functions import remove_punctuation, prepare_text, end_chat

##
##

def test_remove_punctuation():
    assert callable(remove_punctuation)
    assert remove_punctuation("hEllO,hOware!yOU") == "hellohowareyou"

def test_prepare_text():
    assert callable(prepare_text)
    assert prepare_text("!!!go OD howARE yOU~") == "go od howare you"
    
def test_end_chat():
    assert callable(end_chat)
    assert end_chat("random input") == False
    assert end_chat("nevermind") == True

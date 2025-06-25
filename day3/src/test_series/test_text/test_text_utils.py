# test_text_utils.py

from text_utils import shout

def test_shout_basic():
    assert shout("hello") == "HELLO!"

def test_shout_empty():
    assert shout("") == "!"

def test_shout_numbers():
    assert shout("123abc") == "123ABC!"
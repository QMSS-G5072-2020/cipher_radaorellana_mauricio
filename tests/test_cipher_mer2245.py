from cipher_mer2245 import __version__
from cipher_mer2245 import cipher_mer2245
import pytest
from cipher import cipher

def test_version():
    assert __version__ == '0.1.0'

def test_cipher_single():
    example = 'hello'
    shift = 1
    encrypt = True
    expected = 'ifmmp'
    actual = cipher(example,shift,encrypt)
    assert actual == expected, 'Test not passed'
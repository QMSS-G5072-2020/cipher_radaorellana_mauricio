from cipher_mer2245 import __version__
from cipher_mer2245 import cipher_mer2245
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_cipher_single():
    example = 'hello'
    shift = 1
    encrypt = True
    expected = 'ifmmp'
    actual = cipher_mer2245.cipher(example,shift,encrypt)
    assert actual == expected, 'Test not passed'
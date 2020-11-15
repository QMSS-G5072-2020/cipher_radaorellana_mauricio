def cipher(text, shift, encrypt=True):
    """
    Function that replaces each letter with a number of positions in the alphabet.
    Parameters
    ---
    text: string to encrypt or decrypt
    shift: integer of how many number positions to shift in the alphabet
    encrypt: boolean to encrypt or to decrypt
    Returns
    ---
    string encrypted or decrypted
    Examples
    ---
    from cipher_mer2245 import cipher_mer2245
    >>> cipher(text = 'abc', shift = 1, encrypt = True)
    ['bcd']
    >>> 
    
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
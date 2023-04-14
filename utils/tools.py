import hashlib


def encrypt(words: str, salt: str):
    '''md5 encrypt'''
    encoder = hashlib.md5()
    tow = words.join(salt)
    encoder.update(tow.encode('utf-8'))
    return encoder.hexdigest()

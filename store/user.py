import uuid
import tinydb
import hashlib

def encrypt(words: str, salt: str):
    '''md5 encrypt'''
    encoder = hashlib.md5()
    tow = words.join(salt)
    encoder.update(tow.encode('utf-8'))
    return encoder.hexdigest()

user_db = tinydb.TinyDB('user.json')

samples = [{'id':str(uuid.uuid1), 'username':'admin', 'password': encrypt('admin123','toy')}]

if __name__ == '__main__':
    user_db.insert_multiple(samples)
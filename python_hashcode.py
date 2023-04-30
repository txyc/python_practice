import os
import hashlib
def get_md5(text: str):
    return hashlib.md5(text.encode()).hexdigest()
def get_sha256(text: str):
    return hashlib.sha256(text.encode()).hexdigest()
print(get_md5('666'))
print(get_sha256('666'))


'''
def file_hash(file_path: str, hash_method) -> str:if not os.path.isfile(file_path):print('文件不存在。')return ''h = hash_method()with open(file_path, 'rb') as f:while True:b = f.read(8192)if not b:break	h.update(b)return h.hexdigest()
'''
def str_hash(content, hash_method, encoding = 'UTF-8'):
    return hash_method(content.encode(encoding)).hexdigest()
print(str_hash("123",hashlib.md5))
"""
def file_md5(file_path: str)
str:return file_hash(file_path, hashlib.md5)
def file_sha256(file_path: str) -> str:return file_hash(file_path, hashlib.sha256)
def file_sha512(file_path: str) -> str:return file_hash(file_path, hashlib.sha512)
def file_sha384(file_path: str) -> str:return file_hash(file_path, hashlib.sha384)
def file_sha1(file_path: str) -> str:return file_hash(file_path, hashlib.sha1)
def file_sha224(file_path: str) -> str:return file_hash(file_path, hashlib.sha224)
def str_md5(content: str, encoding: str = 'UTF-8') -> str:return str_hash(content, hashlib.md5, encoding)
def str_sha256(content: str, encoding: str = 'UTF-8') -> str:return str_hash(content, hashlib.sha256, encoding)
def str_sha512(content: str, encoding: str = 'UTF-8') -> str:return str_hash(content, hashlib.sha512, encoding)
def str_sha384(content: str, encoding: str = 'UTF-8') -> str:return str_hash(content, hashlib.sha384, encoding)
def str_sha1(content: str, encoding: str = 'UTF-8') -> str:return str_hash(content, hashlib.sha1, encoding)
def str_sha224(content: str, encoding: str = 'UTF-8') -> str:return str_hash(content, hashlib.sha224, encoding)
"""

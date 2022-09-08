""""
Use codeboard and the standard library hashlib module to compute
the MD5, SHA1 and SHA256 (that's SHA2 with a hash size of  n=256 ) of the string "Hello, world!".


""""
import hashlib

# Your code here.
md5 = hashlib.md5("Hello, world!").hexdigest()
print(md5)#prints : 6cd3556deb0da54bca060b4c39479839

SHA1=hashlib.sha1("Hello, world!").hexdigest()
print(SHA1)#prints : 943a702d06f34599aee1f8da8ef9f7296031d699

SHA256=hashlib.sha256("Hello, world!").hexdigest()
print(SHA256)#prints : 315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3

import os, sys


try:  
    print(os.environ['GITHUB_TOKEN'])
    GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
except KeyError:
    print('Please define the environment variable GITHUB_TOKEN')
    sys.exit(1)

# MyKey_decrypt = eval(input("input MyKey_decrypt :"))
# MyKey_encrypt = eval(input("input MyKey_encrypt :"))


MyKey_encrypt = GITHUB_TOKEN
MyKey_decrypt = GITHUB_TOKEN
for i in GITHUB_TOKEN:
    print(i+"_",end="")
password = 'Geodian0821'


def encrypt(key_decrypt,MyKey_encrypt):
    key_encrypt = ""
    for i, j in zip(key_decrypt, MyKey_encrypt):
        key_encrypt = key_encrypt + str(ord(i) + ord(j)) + " "
    return key_encrypt


def decrypt(key_encrypt,MyKey_decrypt):
    key_decrypt = ""
    for i, j in zip(key_encrypt.split(" ")[:-1], MyKey_decrypt):
        key_decrypt = key_decrypt + chr(int(i) - ord(j))
    return key_decrypt

with open("info.txt",'r')as f:
    password_encrypted = f.readlines()[0][:-1]


password_decrypted = decrypt(password_encrypted,MyKey_decrypt)
with open("info.txt",'w')as f:
    f.write(password_encrypted+'\n'+password_decrypted)
print("password_encrypted : ",password_encrypted)
print("password_decrypted : ",password_decrypted)

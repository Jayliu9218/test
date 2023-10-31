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
MyKey_decrypt = os.environ['GITHUB_TOKEN']
MyKey_encrypt = os.environ['GITHUB_TOKEN']
print(type(GITHUB_TOKEN))
print(len(GITHUB_TOKEN))
temp = ""
for i in GITHUB_TOKEN:
    temp+=i
    print(i,end="")
print(temp)
# MyKey_decrypt = MyKey_encrypt[::-1]

password = '0ASGOI097*&%)_'


def encrypt(key_decrypt,MyKey_encrypt):
    if key_decrypt[0] == '1':
        quit()
    else:
        key_decrypt = key_decrypt[1:]
    key_encrypt = ""
    for i, j in zip(key_decrypt, MyKey_encrypt):
        key_encrypt = key_encrypt + str(ord(i) + ord(j)) + " "
    key_encrypt = '1' + key_encrypt
    return key_encrypt


def decrypt(key_encrypt,MyKey_decrypt):
    if key_encrypt[0] == '0':
        quit()
    else:
        key_encrypt = key_encrypt[1:]
    key_decrypt = ""
    for i, j in zip(key_encrypt.split(" ")[:-1], MyKey_decrypt):
        key_decrypt = key_decrypt + chr(int(i) - ord(j))
    key_decrypt = '0' + key_decrypt
    return key_decrypt


print(11)
print("* "*10)
password_encrypted = encrypt(password,MyKey_encrypt)
password_decrypted = decrypt(password_encrypted,MyKey_decrypt)
with open("info.txt",'w')as f:
    f.write(password_encrypted+'\n'+password_decrypted)
print("password_encrypted : ",password_encrypted)
print("password_decrypted : ",password_decrypted)

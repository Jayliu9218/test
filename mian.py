# MyKey_decrypt = eval(input("input MyKey_decrypt :"))
# MyKey_encrypt = eval(input("input MyKey_encrypt :"))
from uu import Error

from _pytest.monkeypatch import K


MyKey_encrypt = 'asoi()&*)HNB(G2nli34u778whfap;lnaoiuagda)'
MyKey_decrypt = 'asoi()&*)HNB(G2nli34u778whfap;lnaoiuagda)'
# MyKey_decrypt = MyKey_encrypt[::-1]

password = '0ASGOI097*&%)_'


def encrypt(key_decrypt,MyKey_encrypt):
    if key_decrypt[0] == '1':
        Error("Already encrtpted !")
    else:
        key_decrypt = key_decrypt[1:]
    key_encrypt = ""
    for i, j in zip(key_decrypt, MyKey_encrypt):
        key_encrypt = key_encrypt + str(ord(i) + ord(j)) + " "
    key_encrypt = '1' + key_encrypt
    return key_encrypt


def decrypt(key_encrypt,MyKey_decrypt):
    if key_encrypt[0] == '0':
        Error("Already decrtpted !")
    else:
        key_encrypt = key_encrypt[1:]
    key_decrypt = ""
    for i, j in zip(key_encrypt.split(" ")[:-1], MyKey_decrypt):
        key_decrypt = key_decrypt + chr(int(i) - ord(j))
    key_decrypt = '0' + key_decrypt
    return key_decrypt


if MyKey_decrypt:
    password_decrypted = decrypt(password, MyKey_decrypt)
else:
    password_decrypted = ''
    pass


# main
pass

password_encrypted = encrypt(password,MyKey_encrypt)
password_decrypted = decrypt(password_encrypted,MyKey_decrypt)
print("password_encrypted : ",password_encrypted)
print("password_decrypted : ",password_decrypted)

import sys
from crypthonData import crypter

version = "0.0.1"

print('\n', version, '\n')

if(sys.argv[1] == 'encrypt' or sys.argv[1] == 'e'):
    crypter.encrypt(sys.argv[2])
elif(sys.argv[1] == 'decrypt' or sys.argv[1] == 'd'):
    crypter.decrypt(sys.argv[2], sys.argv[3])
else:
    print('''HELP:
    encrypt/e + filePath = encrypt file (Ex: crypthon.exe(or crypthon.py) e file.txt)
    decrypt/d + filePath + keyPath = decrypt file (Ex: crypthon.exe(or crypthon.py) d encryptedFile.cry key.cry)''')

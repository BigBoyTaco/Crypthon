import string, random, pickle, time, os

def encrypt(filePath):
    if(filePath == ''):
        print('no file provided.')
        exit()
    print('encrypting.')
    start_time = time.time()
    with open(filePath, 'r') as f:
        fileContents = f.read()
    
    key = createKey()

    encryptedContents = fileContents.split('\n')
    encryptedLetters = []

    #constructing list of characters that can be encrypted
    chars = []
    for char in string.ascii_letters + string.digits + string.punctuation:
        chars.append(char)
    #loop through every line in file
    for line in encryptedContents:
        #loop through every character in file
        for char in line:
            try:
                index = chars.index(char)
            except:
                if(char == " "):
                    encryptedLetters.append("|__|")
            if(char in chars):
                encryptedLetters.append(key[index])
        encryptedLetters.append('\n')

    try:
        os.makedirs(os.getcwd() + '/output')
    except:
        pass

    with open('output/encryptedFile.cry', 'w') as f:
        for i in encryptedLetters:
            f.write(i + "!__!")
    print('encrypted.')
    end_time = time.time()
    print("encryption time:", end_time - start_time, "(seconds)")
    

def decrypt(filePath, keyPath):
    if(filePath == '' or keyPath == ''):
        print('no file provided.')
        exit()
    
    print('decrypting.')
    start_time = time.time()
    with open(filePath, 'r') as f:
        encryptedContents = f.read()
    with open(keyPath, 'rb') as f:
        key = pickle.loads(f.read())

    #split encrypted file into characters
    encryptedLetters = []

    tmp = ''
    inBlock = False
    vert = 0
    excl = 0
    scr = 0
    for char in encryptedContents:
        if(char == "\n"):
            encryptedLetters.append('\n')
            continue
        if(char == "!"):
            excl += 1
            inBlock = True
        if(excl == 2 and scr == 2 and char == "!"):
            inBlock = True
            encryptedLetters.append(tmp)
            tmp = ''
            scr = 0
            excl = 0
        if(char == "|"):
            vert += 1
            inBlock = True
        if(char == "_"):
            scr += 1
            continue
        if(vert == 2 and scr == 2 and char == "|"):
            inBlock = True
            encryptedLetters.append(tmp)
            encryptedLetters.append(' ')
            tmp = ''
            scr = 0
            vert = 0
        elif(vert > 2 or scr > 2 or char != "_" and char != "|" and char != "!"):
            vert = 0
            scr = 0
            inBlock = False
        if(scr == 2 and char != "|"):
            vert = 0
            scr = 0
            inBlock = False
        if (not inBlock):
            tmp += char

    decryptedContents = []

    chars = []
    for char in string.ascii_letters + string.digits + string.punctuation:
        chars.append(char)

    #loop through every letter in encrypted file
    for char in encryptedLetters:
        if(char in key):
            index = key.index(char)
            decryptedContents.append(chars[index])
        elif(char == ' '):
            decryptedContents.append(' ')
            continue
        elif(char == "\n"):
            decryptedContents.append('\n')

    try:
        os.makedirs(os.getcwd() + '/output')
    except:
        pass

    with open('output/decryptedFile.txt', 'w') as f:
        for char in decryptedContents:
            f.write(char)
    
    print('decrypted.')
    end_time = time.time()
    print('decryption time:', end_time - start_time, "(seconds)")


def createKey():
    keyParts = []
    for char in string.ascii_letters + string.digits:
        keyParts.append(char)
    
    #create key
    key = []

    for char in string.ascii_letters + string.digits + string.punctuation:
        key.append(
            keyParts[random.randint(0, len(keyParts) - 1)]
            + keyParts[random.randint(0, len(keyParts) - 1)]
            + keyParts[random.randint(0, len(keyParts) - 1)]
            + keyParts[random.randint(0, len(keyParts) - 1)]
            + keyParts[random.randint(0, len(keyParts) - 1)]
            + keyParts[random.randint(0, len(keyParts) - 1)]
            + keyParts[random.randint(0, len(keyParts) - 1)]
            + keyParts[random.randint(0, len(keyParts) - 1)])
    
    try:
        os.makedirs(os.getcwd() + '/output')
    except:
        pass

    with open('output/key.cry', 'wb') as f:
        f.write(pickle.dumps(key, protocol=None, fix_imports=True, buffer_callback=None))
    return key

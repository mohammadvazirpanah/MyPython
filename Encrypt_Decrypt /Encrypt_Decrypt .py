import decrypt
import encrypt

while (True) :
    massage = input("Enter en For Encrypt and Enter de For Decrypt and Enter e for Exite :")
    if massage == "en" :
        print (encrypt.encrypt()) 
    elif  massage == "de" :
        print (decrypt.decrypt())
    elif massage == "e" :
        print ("Good Luck")
        break    





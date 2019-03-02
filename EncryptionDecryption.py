#encryption and decryption of a message
#Encryption of a message
import string as srr
def EncryptM(s,key):
    if(len(s)<=0):
        print("Message length is too short foe Encryption ...")
        return
    elif (len(str(key))<4):
        print("Pass-Key is too short")
        return
    else:
        li=[]
        # adding pass-key with every character
        for i in range(0,len(s)):
            a = chr(ord(s[i])+key)
            li.append(a)
        s=""
        for i in range(0,len(li)):
            s=s+li[i]
        del li
        return(s)
#Decryption of a message
def DecryptM(s,key):
    li=[]
    # adding pass-key with every character
    for i in range(0,len(s)):
        a = chr(ord(s[i])-key)
        li.append(a)
    s=""
    for i in range(0,len(li)):
        s=s+li[i]
    del li
    return(s)
#for take message from user with a pass-key of minimum length 4

m = str(input("Enter your message here :\n"))
k = int(input("enter a pass-key : "))
m = EncryptM(m,k) 
D_m = DecryptM(m,k)
print("Encrypted message is :\n",m)
print("according to your key the Decrypted message is :\n",D_m)

import random
length = int(input("Enter the length of password you want: "))
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&?'
pswd = ''
i=1
while(i<=length):
    pswd = pswd + random.choice(char)
    i += 1
fh = open("3_pswdgene.txt","w")
fh.write("The random generated password is: ")
fh.write(str(pswd))
fh.close()
import string
import secrets
Password=""
while True:
    Char=""
    Up=input("You want Uppercase Letter  in your Password?(y/n) : ")
    Lo=input("You want Lowercase Letter in your Password?(y/n)  : ")
    Di=input("You want Digits  in your Password?(y/n)           : ")
    Pu=input("You want Symbols  in your Password?(y/n)          : ")
    if Up.lower() == "y":
        Char += string.ascii_uppercase
    if Lo.lower() == "y":
        Char += string.ascii_lowercase
    if Di.lower() == "y":
        Char += string.digits
    if Pu.lower() == "y":
        Char += string.punctuation
    if Char == "":
        print("Choose atleast one Characher to make password!")
    else:
        break
       
Length=int(input("Enter the lenght of your password  : "))
while Length>0 :
    Password += secrets.choice(Char)
    Length-=1
print(Password)

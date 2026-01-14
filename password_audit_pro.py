
from jinja2.nodes import Break
stored_password = "A@S#D4F%78901234"
attempts=0
while True:
    username=input('Enter username: ').lower()
    password=str(input("enter password"))
    count=len(password)
    symbol=['~','!','@','#','$','%','^','&','*','(',')','_','+']
    letters=any(char.islower() for char in password)
    capital=any(char.isupper() for char in password)
    num=any(char.isdigit() for char in password)
    length=any(char in password for char in symbol)

    if username.lower() in password.lower():
        print("your username can not be your password")
        continue

    if letters and capital and length and num and symbol and count >= 14:
        print("strong password")
        break
    elif letters and capital and length and num:
        print("password is medium")
    else :
        print("weak password, your password should have 1 capital letter, i small letter, atleast of 14 characters, 1 number,1 symbol ")



print("**********************************************************************************************************************************************************")

while True:
    username = input('Enter username: ').lower()
    password=str(input("enter password"))
    if stored_password==password:
        print("logging")
        continue
    else:
        print("try again")
        attempts=attempts+1
        if attempts == 100:
            print("Security ALERT, SHUTTING DOWN")
        elif attempts > 20 and attempts < 99:
            print("Security alert")
        elif attempts > 6 and attempts < 19:
            print("suspicious")
        elif attempts > 1 and attempts < 5:
            print("might forgett")
        else:
            print("safe")


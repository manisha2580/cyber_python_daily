#bulk password auditor
passwords = ["Admin123!", "pass", "Security_2024#", "123456", "Vikas_Pro_99@"]
symbol=["!","@","#","$","%","^","&","*","(",")","_","+","{","}",":","?",">","<","|"]
for password in passwords:
    if password == "pass" or password=="123456789":
        print("Very weak")
    elif len(password)>=14 and any(i in symbol for i in password):
        print(" strong password")
    else:
        print(" weak password")

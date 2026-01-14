# Message encryption
import random
name = "Vikas"
encrypted_name=""
#print("orignal name", name)
for letter in name:
    num=ord(letter)
    secret_num= num + 3
    encryption=chr(secret_num)
    encrypted_name=encrypted_name+encryption
print(f"encripted name of User: {encrypted_name}\n", end="")

print("*"*100)
decrypted_name=""
for let in encrypted_name:
    num=ord(let)
    secret_num= num -3
    decryption=chr(secret_num)
    decrypted_name=decrypted_name+decryption
print(f"decrypted name of User: {decrypted_name}", end="")

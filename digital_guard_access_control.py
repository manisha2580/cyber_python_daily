#"Digital Guard"
  import time
a=input("who are you?")
b=int(input("what is the time right now?"))
c=["Manisha", "Vikas","Nishu", "shubham", "maa","paa"]

if a in c and (b>=9 and b<17):
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

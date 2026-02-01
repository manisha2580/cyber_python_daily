#leap year
def is_leap(year):
    if year%4==0 and (year%400==0 or year%100!=0):
        return True
    else:
        return False
year=int(input("enter year to check if it is leap year or not"))
print(f"Enter the year you want to check",year)
a=is_leap(year)
print(a)

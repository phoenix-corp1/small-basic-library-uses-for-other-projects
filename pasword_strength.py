import re

pw = input("enter the password:")

if(len(pw)>=8):
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',pw))==True):
        print("the password is strong")
    elif(bool(re.match('((\\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',pw))==True):
        print("the password is weak")
else:
    print("you have entered an invalid password")
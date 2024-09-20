#Q3. Write a program that perform Division operation between 2 numbers , use Exception
# handling to handel runtime errors (5)
# E.g user can enter 2 numbers in a,b variables and the program will perform division ans=a/b handel division by 0
# exception
a = int(input("enter the firstg number"))
b = int(input("enter the second number"))

try:
    c = a/b
    print("ans",c)
except:
    print("cant divide by jero")

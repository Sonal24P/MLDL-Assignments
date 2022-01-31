
#Assignment-1

#code-1
for num in range(2000,3201):
    if num%7==0 and num%5!=0:
        print(num,end=",")
print()

#Code-2
Fname=input("Enter your First Name ")
Lname=input("Enter your Last Name ")
print(Lname+" "+Fname)

#Code-3
import math
d=12
v=3/4*math.pi*(d/2)**3
print("The volume of the sphere with diameter {} cm is {}".format(d,v))

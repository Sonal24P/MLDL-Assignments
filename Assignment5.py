#1
def divideWithZero():
    try:
        5/0
    except Exception as e:
        print(e)

a=divideWithZero()


#2
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
l=[i+" "+j+" "+k for i in subjects for j in verbs for k in objects]
for i in l:
    print(i)
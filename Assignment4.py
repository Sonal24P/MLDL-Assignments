#1.1
class takeSides:
    def __init__(self,a,b,c):
        self.side1=a
        self.side2=b
        self.side3=c

class claculateArea(takeSides):
   def __init__(self,*args):
       super(claculateArea,self).__init__(*args)
       self.s=(self.side1+self.side2+self.side3)/2
       self.area=((self.s-self.side1)*(self.s-self.side2)*(self.s-self.side3)) ** 0.5

r=claculateArea(10,10,10)
print(r.area)


#1.2
def filter_long_words(lst,n):
    try:
        if type(lst)==list and type(n)==int:
            new = filter(lambda i: len(i)>n, lst)
        return list(new)
    except:
        print("create a list of words")
        a=[input("Enter a word ") for i in range(5)]
        b=int(input("Enter a number "))
        return filter_long_words(a,b)

l=["apple","Banana","Pomegranate","Mango","Pumpkin"]
a=filter_long_words(l,5)
print(a)


#2.1
def mapLenth(l):
    try:
        if type(l)==list:
            new=map(lambda i:len(i),l)
        return list(new)
    except:
        print("create a list of words")
        a = [input("Enter a word ") for i in range(5)]
        return mapLenth(a)

l1=[ "ab","cde","erty"]
print(mapLenth(l1))


#2.2
def isVovel(val):
    try:
        if len(val)!=1:
            raise Exception(val)
        elif val in ["a","e","i","o","u"]:
            return True
        else:
            return False

    except:
        a=input("Enter a character ")
        return isVovel(a)

val1=isVovel("r")
print(val1)
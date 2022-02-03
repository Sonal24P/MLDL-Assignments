#1.1
def myreduce(func,seq):
    for i in range(len(seq)):
        if i+1<len(seq):
            val=func(seq[i],seq[i+1])
            seq[i+1]=val
    return val

def mul(a,b):
    return a*b

print(myreduce(lambda x,y:x*y,[1,2,3,4]))
print(myreduce(mul,[1,2,3,4]))



#1.2
def myfilter(fun,seq):
    for i in seq:
        if fun(i):
            yield i

def even(num):
    if num%2==0:
        return True
    else:
        return False

a=myfilter(lambda x:x%2==0,[1,2,3,4,5,6,7])
b=myfilter(even,[1,2,3,4,5,6,7])
print(list(a))
print(list(b))



#2
#list1
l1=[k*(i+1) for k in ["x","y","z"] for i in range(4)]
print(l1)

#list2
l2=[i*(k+1) for k in range(0,4) for i in ["x","y","z"]]
print(l2)

#list3
l3=[[i+j] for i in range(2,5) for j in range(3)]
print(l3)

#list4
l4=[[j for j in range(i,i+4) ]for i in range(2,6)]
print(l4)

#list5
l5=[(i,j) for j in range(1,4) for i in range(1,4)]
print(l5)
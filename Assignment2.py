
#Assignment2

#Code-1
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print()
i=5
for i in range(4,0,-1):
    for j in range(0,i):
        print("*",end="")
    i-=1
    print()



#Code-2
word=input("Enter the word ")
rev_word=word[::-1]
print("The reversed word is ",rev_word)
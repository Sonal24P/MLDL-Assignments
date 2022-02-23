import numpy
import numpy as np

def Vander_mat(mat,increasing=False):
    try:
        if type(mat)==list or type(mat)==numpy.ndarray:
            if increasing == True:
                vat = np.asanyarray(mat)
                s = vat.size
                v = np.array([vat] * s).T ** range(s)

            else:
                vat = np.asanyarray(mat)
                s = vat.size
                v = np.array([vat] * s).T ** range(s - 1, -1, -1)
        return v
    except:
        print("Error: Invalid data")
        num = int(input("Enter a number of elements for 1D array: "))
        l = [int(input("Enter a number ")) for i in range(num)]
        l_arr = np.array(l)
        return Vander_mat(l_arr,False)

print(Vander_mat([1,7,8]))





#Moving average
def moving_avg(arr,k):
    try:
        if k<=arr.size and k>0:
            arr=np.ravel(arr)
            new_arr = []
            for i in range(arr.size - k + 1):
                avg = 0
                temp=i
                for j in range(k):
                    avg += arr[temp]
                    temp+=1
                new_arr.append(avg / k)
        return np.array(new_arr)
    except:
        print("Error: Invalid data")
        num = int(input("Enter a number of elements for array "))
        l=[int(input("Enter a number ")) for i in range(num)]
        l_arr=np.array(l)
        while True:
            w = int(input("Enter the window size in the range of {} ".format(l_arr.size)))
            if w in range(l_arr.size + 1):
                break
        return moving_avg(l_arr, w)

a=np.array([[1,5],[4,7],[3,5]])
print(moving_avg(a,3))

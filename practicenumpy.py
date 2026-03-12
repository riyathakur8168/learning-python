#  
# print(np.__version__)

# a = np.arange(5,50,5)
# print(a)

# b = np.full((3,3),9)
# print(b)

# c = np.eye(3)
# print(c)

# d = np.linspace(1,100,10)
# print(d)

# e = np.arange(1,25)
# print(e)
# reshaped_e = e.reshape(4,-1)
# print(reshaped_e)
# print(reshaped_e.reshape(6,-1))

# f = np.random.randint(1,100,(3,3))
# print(f)
# print(f.flatten())

# arr = np.array([5,12,7,20,3,18])
# print(arr%2==0)    # ye sirf check karega number is divisble by 2 or not or return T/F
# print(arr[arr%2==0])   # ye number return kardega jo condition ko satisfy karega

# print(arr[arr>10])

# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# # print(arr)
# # print(arr[0])
# print(arr[:,2])
# print(arr[[0,1,2],[2,1,0]])
# #print(arr[[0,0][1,1][2,2]])

# arr1 = np.array([1,2,3,4])
# arr2 = np.array([12,23,45,123])
# arr3 = np.vstack((arr1,arr2))
# arr31 = np.hstack((arr1,arr2))
# print(arr3)
# print(arr31)

# a = [12,23,45,67]
# arr1 = np.array(a,dtype = int)
# arr2 = np.array([1,2,3,4,5],dtype = int)
# print(arr2)
# print(arr31)

import numpy as np
# arr = np.array([10,20,30,40,50])
# print(arr)

# arr1 = np.array([5,10,15,20])
# print(arr1[0])
# print(arr1[-1])


# arr2 = np.array([2,4,6,8,10])
# a= np.ndim(arr2)
# print(a)
# b = np.size(arr2)
# print(b)

# arzero = np.zeros((3,3))
# print(arzero)

# arones = np.ones((2,4))
# print(arones)

# arrange = np.arange(1,21)
# print(arrange)

# ar = np.array([10,20,30,40,50,60])
# print(ar[1:4])

# print(ar[0:-1:2])

# ar2d = np.array([[1,2,3],
#                  [4,5,6],
#                   [7,8,9]])
# print(ar2d)

# print(ar2d[1,1])

# print(ar2d[1])

# a = np.array([1,2,3,4])
# b = np.array([4,5,6])
# c=np.add(a,b)
# print(c)

# d = np.multiply(a,b)
# print(d)
# re = a.reshape((2,2))
# print(re)
# print(re.flatten())

# agg = np.array([10,20,30,40])
# print(agg.sum())
# print(agg.mean())
# print(agg.max())
# print(agg.min())

# a1 = np.array([1,2,3,4,5,6,7,8,9,10])
# print(a1[a1 % 2 == 0])
# print(a1[a1 % 2 != 0])
# print(a1[a1 > 5])
# print(a1[0:-1:2])
# print(a1[1:-1:2])
# print(a1[5:-1])

# a2 = np.array([[10,20,30],[40,50,60],[70,80,90]])
# print(a2[a2 %2 == 0])
# print(a2[:,[0]])
# print(a2[2])
# print(a2[1,1])

# arandom = np.array(np.random.rand(5,5),dtype = int)
# print(arandom)
# print(arandom.max())
# print(arandom.min())
# print(arandom.mean())
# a = (np.random.rand(5,5) * 10).astype(int)
# print(a)

# a1 = np.random.rand(5,5)
# a2 = a1.astype(int)
# print(a2)

# if a1.all:
#     print(a1[i],"is a even number")
# else:
#     print(a1[i],"is a odd number")

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr[[0,0,2,2],[0,2,0,2]])     #fancy indexing
# b = arr.flatten()
# print(b)
# print(b[0:-1:2])
# arr = b.reshape(3,3)
# print(arr)

# ar = np.array([1,2,3,4,5,6,7,8,9])
# print(ar[ar % 2 == 0])    # print even number using boolean indexing

# ar1 = np.array([[10,20,30],[40,50,60],[70,80,90]])
# # print(ar1[:,[1]]) # print second column using fancy indexing

# ar2 = np.random.rand(3,3)
# ar2[ar2 < 0.5] = 0
# ar2[ar2 >= 0.5] = 1  # print random array based on condition

# print(ar2)

# ar3 = np.random.rand(3,3)
# ar4 = np.where(ar3 > 0.5,0,1)  # apply condition on array and modify using
# print(ar4)                      #using where function

# a = np.array([5,10,15,20,25])
# print(np.square(a))      # print square of 1d array using np.square() function

# b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b[[0,1,2],[0,1,2]])      # print diagonal of the 2d array


# a = np.array([[2,4,6],[1,3,5]])
# print(np.sum(a,axis = 0))
# print(np.sum(a,axis = 1))
# print(np.mean(a,axis = 0))
# print(np.max(a,axis=1))

# b = (np.random.rand(3,3) * 10).astype(int)
# print(np.sum(b,axis = 0))
# print(np.mean(b,axis = 1))

# c = np.array([1,2,3])
# # print(np.cube(c))  # gives error kuki python me cube k liy direct function
# # nhi hai to hume ya to c**3 use karna pdega ya power function to get cube of c
# print(np.power(c,3))
ar = np.array([2,4,6,8])
print(np.sum(np.power(ar,3)))



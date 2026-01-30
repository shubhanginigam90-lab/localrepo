# import numpy as np
# nump_arr = np.array([1,2,3,4,5,6])
# print(nump_arr)

# DIFFERNT DIMENSIONS OF ARRAY
# 1D 
# import numpy as np
# arr_1d=np.array([1,2,3,4,5])
# print(arr_1d)
# arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr_2d)
# arr_3d=np.array([[1,2,3,
#                   4,5,6]])
# print(arr_3d)

# USING ZEROES AND ONES
# zero_arr=np.ones((4,3))
# print(zero_arr)

#USING VALUES
# val_arr=np.full((1,3),6)
# print(val_arr)

# SEQUENCE OF NUMBERS
# arr=np.arange(1,10,2)
# print(arr)

# IDENTITY MATRIX
# arr=np.eye(4)
# print(arr)

# SHAPE AND SIZE
# arr=np.array([[1,2,3,4],[1,2,3]])
# print(arr)
# print(arr.shape)

#QUESTION 4 
# l={
#     "name":"shubhi",
    
#     "age":"12",
#     "surname": "nigam"
# }
# arr=np.array(l)
# print(arr.dtype)

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr.reshape(3,4))
import numpy as np
# l=[1,2,3,4,5,6]
# nump_arr = np.array(l)
# print(nump_arr)
# one_arr=np.ones(4)
# print(one_arr)

# full(shape,value)
# fil_arr=np.full((1,3),6)
# print(fil_arr)

# arange(start,stop,step)
# arr=np.arange(1,10,2)
# print(arr)

# identity matrix
# iden=np.identity(3)
# print(iden)
# print(iden.shape)
# print(iden.size)
# print(iden.ndim)
# print(iden.dtype)
# int_arr=iden.astype(int)
# print(int_arr)
# print(int_arr.dtype)
# print(iden)

# # øperators
# print(iden+2)
# print(iden*2)
# print(iden)

# ARRREGATION FUCTION
# arr=np.full((3,3),4)
# print(arr)
# print(np.sum(arr))

# a=np.var(arr)
# arr=np.array([[[1,3],[4,5],[6,7]],[[3,3],[5,5],[7,7]]])
# print(arr)
# print(arr[(2)])
# arr=np.array([[1,2,3],[2,3,4],[4,5,5]])
# print(arr.shape)
# print(arr.size)
# print(arr.ndim)
# print(arr[::2])
# print(arr)

# FANCY INDEXING
# arr=np.array([1,2,3,4,5,6,7])
# print(arr[[0,2,3]])
# arr=np.array([[[1,2,3,4],[3,4,5,6],[7,5,9,8]]])
# print(arr[2,[0,1,2]])
# print(arr.shape)
# arr=np.array([1,2,3,4,5,6])
# resp=arr.reshape(1,4,3)
# print(resp)

# FALLTEN AND RAVEL
# arr=np.array([[1,2],[3,4]])
# # arr=np.array([[[1,2,3,4],[3,4,5,6],[7,5,9,8]]])
# arr2=arr.ravel()
# arr2[0]=12
# print(arr2)
# print(arr)

# RESHAPING (np.insert(array,index,value,axis=none,1,0))
# inserting a value 

# a=np.insert(arr,2,12,axis=0)
# print(a)
# print(arr)
# a=np.append(arr,[90,1])
# print(a)

# arr=np.array([[1,2,3,4,5,6]])
# arr2=np.array([[9,8,7,6,5,1]])
# print(arr+arr2)
# new_arr=np.concatenate((arr,arr2))
# print(new_arr)

# DELETE (np.delete(array,index,axis=none,0,1))
# arr=np.array([1,2,3,4,5,6])
# arr=np.array([[9,8,7],[6,5,1]])
# arr2=np.delete(arr,[1,2],axis=1)
# print(arr2)

# STACKING AND SPILITTING 
# vstack()--> row wise stack 
# hstack--> col wise stack
arr=np.array([1,2,3,4,5,6]) 
arr2=np.array([7,7,8,9,0,9])
print(np.vstack((arr,arr2)))
print(np.hstack((arr,arr2)))


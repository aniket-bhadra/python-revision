
# marks = {
#    "rohit": 65,
#    "virat": 88
#  }
# name="rohit"

# print(65 in marks)
# print(marks[name])
# print(marks)

# print(type("hello"))

# from math import *
# print(max([5,9,7,8,1,2,3]))


# f=["apple", "chocolate", "pizza", "burger", "tomato"]

# for item in f:
#    print(item)

# i=0;
# while(i<len(f)):
#    print(f[i])
#    i+=1

# binary search practice

# def search(array,target):
#    s=0
#    e=len(array)-1
#    while(s<=e):
#        m=((e-s)//2)+s
#        if(target==array[m]):
#            return m
#        if(target>array[m]):
#            s=m+1
#        if(target<array[m]):
#            e=m-1
#    return -1

# a=[22,33,44,55,66,99]
# target=66
# print(search(a,target))


# recursive
# def search(array,target,s=0,e=False):
#    if(e==False):
#       e=len(array)-1
#    if(s>e):return -1

#    m=((e-s)//2)+s
#    if(target==array[m]): return m
#    if(target>array[m]):
#       return search(array,target,m+1,e)
#    if(target<array[m]):
#       return search(array,target,s,m-1)

# a=[22,33,44,55,66,99]
# target=666
# print(search(a,target))



# reverse original array
# def rever(array):
#    s=0
#    e=len(array)-1
#    while(s<e):
#       temp=array[s];
#       array[s]=array[e];
#       array[e]=temp;
#       s+=1;
#       e-=1;

# a=[22,33,44,55,66,99]
# rever(a)
# print(a)

# recursive
# def rever(array,s=0,e=False):
#    if(e==False):e=len(array)-1
#    if(s>e): return;
#    temp=array[s];
#    array[s]=array[e];
#    array[e]=temp;
#    return rever(array,s+1,e-1)


# a=[22,33,44,55,66,99]
# rever(a)
# print(a)


# bubble sort
# def bubbleSort(array):
#    lastIndex=len(array)-1
#    i=0;
#    while(i<=lastIndex-1):
#       j=0;
#       while(j<=lastIndex-1-i):
#          if(array[j]>array[j+1]):
#             temp=array[j];
#             array[j]=array[j+1];
#             array[j+1]=temp;
#          j+=1;
#       i+=1;

# a=[30,29,28,27,26,25]
# bubbleSort(a);
# print(a)

class Test:
   def __init__():
      pass

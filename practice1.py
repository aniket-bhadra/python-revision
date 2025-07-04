
# # print(range(5))

# # name="tony"
# # print("tss" in name)

# # fruits = ["apple", "banana", "cherry"]

# # for f in fruits:
# #    print(f)


# # name="tony"
# # for t in name:
# #    print(t)

# # for i in range(10):
# #    print(i)

# # i=0
# # while(i<=10):
# #    print(i);
# #    i=i+1;

# # marks = [25, 65, 88]

# # print(marks[-1])
# # print(marks[0:2])

# # for m in marks:
# #    print(m)

# # print(len(marks))
# # i=0

# # while i< len(marks):
# #    print(marks[i])


# # i=0;

# # while i< len(marks):
# #    print(marks[i])


# marks = [25, 65, 88,25]

# # print(marks.count(25))
# # print(marks.index(65))

# # marks.append(66)
# # print(marks)
# # marks.insert(1,0)
# # marks.clear()
# # print(marks)

# # print(a[0])

# obj={
#    "name":"rohit",
#      "age":25
#      }

# obj["name"]="hardik"
# # print(obj)
# a= {25,65,45}
# # print(len(a))


# # from math import sqrt
# # print(sqrt(9))

# # from math import *
# # print(pow(2,8))


# def greet(name):
#    print("hello"+" "+name)

# # greet("rohit")

# # print(2**3)
# # print("k"*3)



# # def result():
# #    n= int(input("enter upper limit"))
# #    type = input("enter type")
# #    sum=0;
# #    i=1;
# #    if(type.lower()=="even"):
# #       while(i<=n):
# #          if(i%2 ==0):
# #             sum=sum+i
# #          i=i+1
# #    else:
# #       while(i<=n):
# #          if(i%2 !=0):
# #             sum=sum+i
# #          i=i+1
# #    return sum

# # print(result())

# a=["virat","rohit","Hardik","pant","rahul"]
# # for name in a:
# #    print(name)

# # i=0;
# # while i< len(a):
# #    print(a[i])
# #    i=i+1

# # i=0;
# # while i<=10:
# #    print(i)
# #    i=i+1

# # for i in range(10):
# #    print(i)


# # abc={
# #    1:2,
# #    4:5
# # }
# # name=3
# # abc[name]=5
# # print(abc)


# # a = ["virat", "rohit", "Hardik", "pant", "rahul"];
# # b = ("virat", "rohit", "Hardik", "pant", "rahul");
# # print("virat" in b)


# # two sum
# def two_sum(array,target):
#    guide={}
#    i=0;
#    while i<len(array):
#       result = target-array[i]
#       if(result in guide):
#          return [guide[result],i]
#       else:
#          guide[array[i]]=i
#       i=i+1

# print(
# two_sum([1,2,3,4,3],6)
# )


# s={25,26,27,28}
# # print(2888 in s)


# def pow2(x,n):
#    result=1
#    while(n>0):
#       if(n%2 !=0):
#          result= result*x
#       x=x*x
#       n=n//2
#    return result

# # print(pow2(2,8))


# # print(type(3))


# arr=[1,2,3]
# first= arr[0]

# s={25,26,25}
# print(s)

arr1=[25,26]
arr2=[66,88]

arr=[arr1,arr2]
f=arr[0]
f.append(999999999)
# print(arr)

arr3=[66,88]
k=arr3[0]
k=888888888888
# print(arr3)



class Test:
   def __str__(self):
      return "im test obj"

obj = Test()
# print(obj)

# for i in range(10):
#    print(i)


# arr=[25,26,78,25]
# print(len(arr)-1)

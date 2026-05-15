#LIST

# a = 11
# a = 12
# a = 13
# a = 14
# a = 15
#for creating list you have to use square brackets([])

#l = [11,12,13,14,15]
 #special power 
 #1- hetrogeneous  nature - means it can store any kind of data type at once
#eg
#l = [12,"hello",12.67,true,print()] 

#2-ordered - every elements a list  has a  designated position 

#3- mutable nature - you can change anything inside the list at any point of time

#4- duplicates - you can store duplicate elements  inside list
#reading a list
# a = [10,20,30,40,50]

# #you will use indexing
# print(a)
# print(a[4],a[-1])

#updating a list
# a = [10,20,30,40,70]

# a[-1] = 50

# print(a)

#delete

# a = [10,20,30,40,50]
# # you can delete a single element and entire list

# del a[-1]
# print(a)


#creating loops on list

# a = [10,20,30,40,50]

# #based on value

# for i in a:
#     print(i)
    

#here you will access all the values 10,20,30....


#based on index
# for i in range(0,len(a)):
#     print(a[i])
#this loop can access your index aswell as your value and it gives more control over your list

#methods 
# a = [1,2,3,4]
# a.append(5)
# print(a)

# l = []
# for i in range(10,51,10):
#     l.append(i)

# print(l)

# a = [10,20,40,50]
# a.insert(2,30)
# print(a)

# a = [10,20,30]

# a.clear()

# print(a)

# a = [10,20,30]

# a.pop(1)

# saved = a.pop(1) #this will remove via index 
# a.remove(10) #this will remove via value
# print(a)


# a = [10,20,30,40,50]

# a.sort()

# print(a)



# a = [10,20,30,40,50]

# a.reverse()

# print(a)




#DAY-2(list problems)


# a = int(input("how many elements you want:"))

# l = []
# for i in range(a):
#     z = int(input("tell your numberrs:"))
#     l.append(z)

# print(l)


# a = eval(input("tell you str"))


# a = [10,20,30,40,50]

# l = []

# for i in range(len(a)-1,-1,-1):
#     l.append(a[i])

# print(l)

# a =[10,20,30,40,50]

# z = len(a)-1

# for i in range(len(a)//2):
#     a[i],a[z] = a[z],a[i]
#     z = z-1

# print(a)


# a = [-1,-3,-4,6,7,4,-2]

# for i in a:
#     if i >=0:
#         print(i)

# for i in a:
#     if i <= 0:
#         print(i)


#SHEET

# a =[1,2,3,4,5]

# print(a)




#DAY-3

##SORTING THE LIST

# a = [27,30,24,68,43,56,67]

# for j in range(len(a)-1):
#     for i in range(0,len(a)-1):
#         if a[i] > a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]

# print(a)


# a = [12,56,23,89,23,1,45,7,8,4,23]

# largest = a[0]
# index = 0
# for i in range(1,len(a)):
#     if a[i] > largest:
#         largest = a[i]
#         index = i

# print(f"largest element is {largest} at index {index}")



###DAY-04


##largest and second largest

# l = [1,16,17,23,2,89,45]
# largest_index = 0
# largest = l[0]
# s_largest = l[0]
# second_largest_index = 0

# for i in range(1,len(l)):
#     if l[i] > largest:
#         s_largest = largest
#         largest = l[i]
#         second_largest_index = largest_index
#         largest_index = i

#     elif l[i]  > s_largest:
#         s_largest = l[i]
#         second_largest_index = i

# print(largest,largest_index)
# print(s_largest,second_largest_index)


# ##for finding smallest and s_smallest -> you will pick greater value
# ##for finding largest and s_largest -> you will pick smaller value
# ##smallest and second_smallest
# l = [1,16,17,23,2,89,45]
# smallest_index = 0
# smallest = 12
# s_smallest = 12
# second_smallest_index = 0

# for i in range(1,len(l)):
#     if l[i] < smallest:
#         s_smallest = smallest
#         smallest = l[i]
#         second_smallest_index = smallest_index
#         smallest_index = i

#     elif l[i]  < s_smallest:
#         s_smallest = l[i]
#         second_smallest_index = i

# print(smallest,smallest_index)
# print(s_smallest,second_smallest_index)



##DAY-05


#check if list is sorted or not 
# l = [1,2,3,4,5,6,7]
# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         print("list is not sorted")
#         break
#     else:
#         print("list is sorted")


##pallindrom
# print(l[len(l)-1])
# l = [2,3,15,15,3,2]
# for i in range(len(l)//2):
#     if l[i] != l[len(l)-1-i]:
#         print("list is not pallindrome")
#         break
#     else:
#         print("list is pallindrome")
        
# 1. take n as input from user
# 2. create  an list of size n
# 3. take input for each element

# n = int(input("tell a number:-"))
# l = []

# for i in range(n):
#     z = int(input("tell your number:_"))
#     l.append(z)
# print(l)


# n = int(input("enter the size of list"))
# list = []
# sum = 0
# for i in range(n):
#     z = int(input("enter the element at index {i}:-"))
#     sum += z
#     n.appeend(z)
# print(list)
# print(sum)


# lst = list(map(int,input("enter elements:").split()))
# print(lst)

#map(data_typr,input)
#split(seperates all the values and digits)
#list(coverts the value in the form of list data structure)

###sabse pahle inputs accept -> har input split hoga -> inputs will be type casted in the form of int -> we sorrted all the int values inside a list


##DAY-06



##rotate a list by k elements
# l = [1,2,3,4,5] #o//p = k=2, [4,5,1,2,3]

# k = 2
# for i in range(k):
#     last = l[-1]
#     for j in range(len(l)-1,0,-1): #j->4,3,2,1
#         l[j] = l[j-1]
#     l[0] = last
# print(l)


#assign all the 0s at the end of the list

# l = [0,1,0,3,12]
# j = 0
# for i in range(len(l)):
#     if l[i] != 0:
#         l[i],l[j] = l[j],l[i]
#         j = j + 1
# print(l)








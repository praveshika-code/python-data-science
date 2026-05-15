#TUPLE
'''
1. tuple are ordered (indexing)
2. tuples can duplicacy
3. are hetrogenous
4. are  immutable'''


# a = 10,20
# print(type(a))
# ---o/p =   <class 'tuple'>


#t = () #empty tuple
# t = (1,2,3,4,5)

# #direct loop:-
# for i in t:
#     print(i)

# #index loop:-
# for i in range(len(t)):
#     print(i,t[i])

# for index,value in enumerate(t):
#     print(index,value)

# print(t[2])
# print(t[1:4])


##METHODS IN TUPLE
'''
1. count() -> we can count occurence of a value
2.index()

'''

# t = (1,2,2,2,3,4,5,3,4)
# print(t.count(2))
# print(t.count(3))

# print(t.index(1))
# print(t.index(2)) #first occurence of 2


# t = (1,2,2,2,3,4,5,3,4)
# print(3 in t) #membership oerator
# print(9 in t)


# TUPLE PACKING AND UNPACKING 
'''t = (1,2,3,4,5)  #this is unpacking
a,b,c,d,e = t

print(a)
print(b)
print(c)
print(d)
print(e)


a = 1,2 #this is are packing '''

#STAR EXPRESSION(*)
# t = (1,2,3,4,5)
# # a,b = 1  # error aayga (bcz element jyada hai)
# # a,*b = t  #nhi aayga (b ke baad ke saare elements collect kar lega)
# a,*b,c = t
# print(a)
# print(b)   #middle value extraction
# print(c)


#MERGE TW0 TUPLES
'''t1 = (1,2,3,4)
t2 = (5,6,7,8)
print(t1+t2)'''


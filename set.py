##SET  -- set are mutable
# 1.unordered(no indexing)
# 2. semi mutable(can add,but cannot change)
# 3. unique element (no duplicates)
# 4. hetrogeneous(can contain different data type)



# a = []
# b = {}
# c = set()


# s = set()
# s = {1,2,3,4,5}
# print(type(s))
# ---o/p = 
# <class 'set'>

# s = {1,2,3,4,5,6,7}


##METHODS IN SET

# 1. add
# 2. update
# 3. remove()
# 4. discard
# 5. pop 
# 6. clear

#1. add() #for adding single element / value
# s = {1,2,3,4,4,5,4}
# s.add(8)
# print(s)

# -----{1, 2, 3, 4, 5, 8}

# #2. update() # for adding multiple elements/values
# s = {7,1,2,3,4,4,5,4}
# s.update([7,8,9])
# print(s)

# ----{1, 2, 3, 4, 5, 7, 8, 9}


# 3. remove()   #if value is not present we will get an error
# s.remove(2)
# print(s)


# 4. discard() #if value is not present we will not get an error
# s.discard(10)
# print(s)


# 5. pop()  #remove smallest element
# s = {8,4,7,6,5}
# s.pop()
# print(s)

# print(s.pop())


#6. clear  #remove all the elements and gives us an empty set
# s.clear()
# print(s)




# 1. Intersection
#2. union
#3. difference
#4. symmetric difference



# s1 = {1,2,3,4}
# s2 = {2,3,4,5}
# print(f"intersection: {s1.intersection(s2)}")
# print(f"union:{s1.union(s2)}")
# print(f"difference s1: {s1.difference(s2)}")
# print(f"difference s2: {s2.difference(s1)}")
# print(f"symmetric difference: {s1.symmetric_difference(s2)}")




# fs = {10,20,30,40,50}       #fs-frozenset
# fs = frozenset(fs)          #frozenset is a function
# # fs.add(60)
# fs.remove(10)
# print(fs)

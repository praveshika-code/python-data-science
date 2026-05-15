### list me values access karne index use karte hai ,dict me keys use karte hai
##itreval - jisse loop chale
# d = {"one":1,"two":2,"three":3}


# d1 = {1:10,2:20,3:30}

# d1[1] =100

# print(d1)

##methods

# print(dict.fromkeys([1,2,3,4,5],10))

# print(d1.gets())

# print(d1.items())

# print(d1.keys())


# print(d1.pop(3))

# print(d1.popitem())

# d1.setdefault(4,40)
# print(d1)



# d1 = {1:10,2:20,3:30}
# d2 = {4:40,5:50,6:60}

# d1.update(d2)

# print(d1)

#.....

# d1 = {1:10,2:20,3:30}
# d2 = {4:40,5:50,6:60}

# for i in d2:
#     print(i)
#     print(d2[i])



# d1 = {1:10,2:20,3:30}
# d2 = {4:40,5:50,6:60}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)


# d1 = {1:10,2:20,3:30}
# d2 = {4:40,5:50,6:60}

# for i in d2:
#     if i in d1.keys():
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)


# l = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,6,6,6]  #count karne ke liye dict ko use karege

# count = 0

# for i in l:
#     if i == 2:
#         count = count + 1

# print(count)


# l = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,6,6,6]  

# d = {}

# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d)  ##o/t = {1: 3, 2: 4, 3: 4, 4: 5, 5: 4, 6: 6}

# print(f"frequency of all elements are {d}")


# a = {1:10,2:20,3:30}
# b = {4:40,5:50,6:70}

# a.update(b)

# print(a)     ##o/t = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 70}




# a = {1:10,2:20,3:30}
# b = {4:40,5:50,6:70}

# for i in b:
#     if i in a.keys():
#         a[i] = a[i] + b[i]
#     else:
#         a[i] = b[i]

# print(a)     ##o/t = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 70}



###day - 03

#--2206. Divide Array Into Equal Pairs


# l = [3,2,3,2,2,2]
# d = {} #3:2,2:4

# for i in l:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)   ##o/t = {3: 2, 2: 4}


# for i in d.values():
#     print(i)  ##o/t = 2____4___

#     if i % 2 == 0:
#         print("notpair")

#     else:
#         print("pair")


###leet code (2206)

# class Solution:
#     def divideArray(self, nums: List[int]) -> bool:
#         d = {}     # count occurence of elements {3:2, 2}
#         for i in nums:
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1

#         for i in d.values():
#             if i % 2 != 0:
#                 return False
#         return True  


###2341  leet code    

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if  i in d:
                d[i] += 1
            else:
                d[i] =1
        pairs = 0
        leftovers = 0
        for i in d.values():
            pairs += i // 2  # calculate pairs we will use //
            leftovers += i % 2  # to calculate leftovers we will use %

        return[pairs,leftovers]
    

##2293 - min max game

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            newNums = []
            for i in range(len(nums)//2):
                if i % 2 == 0: #even index 
                    newNums.append(min(nums[2 * i],nums[2 * i + 1]))
                else:  #odd index
                    newNums.append(max(nums[2 * i],nums[2 * i + 1]))
            nums = newNums
        return nums[0]  











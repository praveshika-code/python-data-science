#rotate a list k time
'''
l = [1,2,3,4,5] 

k = 2
for i in range(k):
    last = l[-1]
    for j in range(len(l)-1,0,-1): #j->4,3,2,1
        l[j] = l[j-1]
    l[0] = last
print(l)'''




#check palindrome list using recursion
#num = [1,2,3,2,1]


    


    



'''
#leetcode
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {} 
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for i in d.values():
            if i % 2 != 0:
                return False
        return True
    '''



'''
#find the first non repeating element

nums = [4,5,1,2,0,4,1,2]

def first_non_repeating(l):
    for i in l:
        if l.count(i) == l:
            return i
    return None
print(first_non_repeating(nums))
'''

"""
# count frequency of each elements

l = [1,2,2,3,3,3]


d = {}

for i in l:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d) 
 """



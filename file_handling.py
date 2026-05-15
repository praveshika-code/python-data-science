# FILE HANDLING 

# file = open("list.py")
# print(file.read())
# file.close()

# MODES
'''
w- write mode (1. agar flie create nhi hai toh create ho jaygi, 2. agar purana data hai to over write ho jayga)
a-append mode
r- read mode
x- create mode

'''

# file = open("gangadhar.txt","x")
# file = open("gangadhar.txt","w")
# file.write("this is gangadhar file")
# file.close()


# file = open("gangadhar.txt" , "a")
# file.write(" this contant is added using a (append) mode")
# file.close()


# file = open("gangadhar.txt" , "r")
# for i in file:
#     print(i)
# file.close()


#WITH STATEMENT (auto close)
# with open("gangadhar.txt","r")as file:
#     print(file.read())


# with open("gangadhar.txt","w")as file:
#     file.write("content overwritten")
#     print("DONE")


# PATHS
# D:\py-23\gangadhar.txt
# from pathlib import Path
# p = Path("gangadhar.txt")
# if p.exists():
#     print("file exist")
# else:
#     print("file does not exist")
#  
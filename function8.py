#FUNCTIONS
# #user defined function

# def greeting():     #defining of the function
#     print("hello good evening!!")

# greeting()  # --> calling of the function

#parameters and arguments

# def addition(a,b): #a and b are parameters
#     print(a + b)

# addition(10,20)


# def palindrome(n):
#     rev = 0 
#     copy = n
#     while n != 0:
#         rev = rev * 10 + n%10
#         n = n//10

#     if copy == rev:
#         print("palindrome")
#     else:
#         print("not palindrome")

        
# palindrome(431)
# palindrome(23455)
# palindrome(3466)
# palindrome(5798)

# def multiply(a,b): #fixed position
#     print(a*b)

# multiply(12,67) #fixed positional arguments

#2nd defult arguments

# def info(name,age):
#     print("your name is {name} and your age is {age}")

# info(age = 19,name = "praveshika")
    
#if you give a value using default argument you always 
#have to give further values using default arguuments

# def info(a,b,c,d,e):
#     print(f"your age is {a,b,c,d,e}")

# info(12,34,e = 67,c = 12,d = 67)

## default parameters

# def info(name,age,id = None):
#     print("info recived")

# info("praveshika",19)


### DAY-17

#def strongnumber(n):


# def hello():
#     print("how are you")

# hello()

#RETURN VS PRINT

# def hello():
#     return"how are you"

# print(hello())


# def agechecker(n):
#     if n >= 18:
#         return True

#     else:
#         return False

# age = int(input("tell your age:-"))

# if agechecker(age):
#     print("you can vote")

# else:
#     ("you can not vote")



# def hello1():
#     hello2()
#     print("hello 1")

# def hello2():
#     hello3()
#     print("hello 2")

# def hello3():
#     hello4()
#     print("hello 3")

# def hello4():
#     print("hello 4")

# hello1()



### without loop rannge write a no.
# def numbers(n):
#     if n == 100:
#         return "done"

#     print(n)
#     numbers(n+1)

# numbers(1)


### TYPES OF DATA STRUCTURE
# list
# Tuple
# Set
# Dict


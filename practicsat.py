#take a digit input from user and reverse it using for loop 
# n = input("enter your digit")
# print(n[::-1])


# n = input("enter your digit")
# digit = ""
# for i in str(n)[::-1]:
#     digit = digit + i 
# print(digit)

# print("hello world\n'*5")


# Fibonacci series upto N terms

# n = int(input("enter your series no.:"))
# a =0 
# b = 1
# for i in range(n):
#     print(a)
#     a , b = b , a + b


# print the largest digit in a number

# n = 4289
# largest = 0
# for i in str(n):
#     a = int(i)
#     if a > largest:
#         largest = a
# print(largest)


# Gussing game
#(user guesses a number until correct)

# import random

# abc = random.randint(1,50)
# for i in range(5):
#     xyz = int(input("enter your number:"))

#     if xyz == abc:
#         print("you won")
#         break

#     if xyz < abc:
#         print("too small go higher")

#     if xyz > abc:
#         print("too high values go for lower")

#     else:
#         print(f"aaaa haar gyii,number hai {abc}")


# Chech whether a number is paillndrom or not

# num = 1234
# if str(num) == str(num) [::-1]:
#     print(f"number{num} is paillndrome")
# else:
#     print(f"number{num} is not paillndrome")

#keep taking input until user enters 0, then print sum

# sum = 0
# while True:
#     n = int(input("enter your number"))

#     if n == 0:
#         break
#     sum += n
#     print(sum)

#reverse a number using while loop

# n = 8934
# rev = 0
# while n > 0:
#     rev = rev + n%10
#     n = n // 10

# print(rev)

#armstrong number or not

n = 153
copy = n

length = len(str(n))

sum = 0
while n > 0:
    digit = n % 10 #3,5,1
    sum += digit**3
    n = n // 10
    if copy == sum:
        print("armstrong number")
    else:
        print("not an armstrong number")

    




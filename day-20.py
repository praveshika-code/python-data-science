###count the number of digits in a number

# def count(n):
    
#     count = 0
#     while n > 0:
#         digit = n % 10
#         count += 1
#         n = n // 10
#     print(f"count of digit is {count}")
# count(256)

### if we use return insidde a function  
##it will act like a mini variable and untill unless we didn't print the variable the output will not be displayed


### find the sum of digits of a number(e.g.,123 -> 6).
# def check_sum(n):
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         sum = sum + digit 
#         n = n // 10
#     return f"sum is {sum}"
# print(check_sum(124))


### check whether a number is armstrong orr not

# n = 153
# sum = 0 
# while n > 0:
#     digit = n % 10
#     power = digit ** 3
#     sum = sum + power
#     n =  n // 10
# if sum == sum:
#     print("armstrong number")
# else:
#     print("not an armstrong  number")
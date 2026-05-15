# #print strings in reverse ,its length,in uppercase,lowercase and copy into another string

# s = "Shery"
# print(s[::-1])
# print(len(s))

# s = "shery"
# print(f"reverse string -> {s[::-1]}")
# print(f"length of string -> {len(s)}")
# print(f"string in upper format -> {s.upper()}")
# print(f"string in lower format -> {s.lower()}")


## Arrange string characters such that lowercase letters should come first

# s = "ShEry"
# updated = ""
# for i in s:
#     if i.islower():
#         updated = updated + i
#     else:
#         updated = updated + i
#     print(updated)

# s = "ShEry"
# lower = ""
# upper = ""
# for i in s:
#     if i.islower():
#         lower = lower + i
#     elif i.isupper():
#         upper = upper + i
#     print(lower + upper)

## Count all letters, digits, and special symbols from a given string
# Given: str1 = "P@#yn26at^&i5ve"
    # Expected Outcome:
    # Total counts of chars, digits, and symbols
    # Chars = 8
    # Digits = 3
    # Symbol = 4

# str1 = "P@#yn26at^&i5ve"
# alpha = 0
# digit = 0 
# special = 0
# for i in str1:
#     if i.isalpha():
#         alpha = alpha + 1
#     elif i.isdigit():
#         digit = digit + 1
#     else:
#         special = special + 1
# print(f"alpha cout:{alpha}")
# print(f"digit cout:{digit}")
# print(f"special cout:{special}")

## Compare two strings without using inbuilt functionsx

# str1 = "hello"
# str2 = "Hello"
# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         print(i)
#     else:
#         print("both strings are of not he same length")

# str1 = "hello"
# str2 = "Hello"
# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         if str1[i] != str2[i]:
#             print("string are not same")
#             break
#         else:
#             print("string are same")


## Count Vowels from given string

# def countVowels():
#     str1 = "Hello"
#     vowels ="aeiouAEIOU"
#     count = 0

#     for i in str1:
#         if i in vowels:
#             count += 1
#     print(f"Total count of vowels are:{count}")
# countVowels()

# def countVowels():
#     str1 = "Hello"
#     vowels ="aeiouAEIOU"
#     count = 0

#     for i in str1:
#         if i in vowels:
#             count += 1
#     return f"Total count of vowels are:{count}"
# print(countVowels())


### reversee a string
# s = "AKIHSEVARP"
# print(s[::-1])
# print(len(s))

# s = "praveshika"
# for i in s[::-1]:
#     print(i)

# s = "praveshika"
# rev = ""
# for i in s[::-1]:
#     rev = rev + i
# print(rev)

### Check string is Pallindrome or not**

# s = "praveshika"
# rev = s[::-1]
# if s == rev:
#     print("f{s} is an palindrome")
# else:
#     print(f"{s} is not palindrome")

# def palindrome(s): 
#     rev = s[::-1]
#     if s == rev:
#         print("f{s} is an palindrome")
#     else:
#         print(f"{s} is not palindrome")
# palindrome("madam")

### count number of vowels and consonants from string


# s = "golmaal"
# vowels = 0
# consonant = 0

# for i in s:
#     if i in "aeiouAEIOU":
#          vowels += 1
#     else:
#         consonant += 1
# print(f"total vowels are: {vowels}")
# print(f"total consonant are: {consonant}")
            
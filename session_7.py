# def hello(name,age):
#   print("Hello "+ name,age)

# hello("Nadia", 22)

# hello(name)

# name= input("What is your name?")

# def hello(name):
#   print("Hello ", name)

# hello(name)

# def hello(name):
#     print("Hello ", name)

# names = ["Alice", "Bob", "Charlie"]
# for name in names:
#   hello(name)

# def area(a,b):
#   print("The area is:", str(a*b))
# area (10,2)

# def print_list(item):
#     print(item)

# items = ["Orange", "Plum", "Carrot"]
# for item in items:
#   print_list(item)

# Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

# def school_elibability(age):
#   if age == 0:
#     print("You're not born yet!")
#   elif age < 11:
#     print("You're too young to go to this school")
#   elif age >= 11 and age <= 16:
#     print("You can can come to this school")
#   else:
#     print("You're too old for school")

# school_elibability(21)


# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers)
# def is_odd(number):
#   if number % 2:
#     return True
#   return False

# data=[1,2,3,4,5,6,7,8,9]

# for item in data:
#   print(is_odd(item))

# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' to 'olleh'

# def reverse_word(word):
#   reverse = word [::-1]
#   print(reverse)

# reverse_word("Nadia")
# reverse_word("Jason")

# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# *****
# ****
# ***
# **
# *


# def print_stars(x):
#   star = ""
#   for y in range(0,x):
#     star += "*"

#   print(star)
  
#   if x > 1:
#     print_stars(x-1)

# print_stars(5)


# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked"

# def padlock(passcode):
#   pin=4441
#   if pin==passcode:
#     return "Unlocked"
#   return "Locked"

# print(padlock(5678))
# print(padlock(4441))


# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20

# def sum_of_multiples(limit):
#   sum=0

#   for i in range(0,limit+1):
#     if i % 3 ==0:
#       sum += i
#     elif i % 5 ==0:
#       sum += i
#   return sum
# print (sum_of_multiples(20))


# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not
# def is_prime(number):
#   for i in range(2, number):
#     if number % i == 0:
#       return False
#     return True
# print (is_prime(23))


# 7. Write a function that checks to see if a string is a palindrome, if it is, it will return True and False if it is not.
# def pall(word):
#   reverse_word=word[::-1]
#   if word == reverse_word:
#     return True
#   return False
# print(pall("abba"))
# print(pall("breakfast"))


# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.

# def pall_sentence(sentence):
#   formatted_sen= sentence.lower()
#   new_sentence=formatted_sen.replace(" ","")
#   rev_sentence=new_sentence[::-1]

#   if new_sentence==rev_sentence:
#     return True
#   return False

# print(pall_sentence("bsdfb khsfh"))
# print(pall_sentence("A nut for a jar of tuna"))


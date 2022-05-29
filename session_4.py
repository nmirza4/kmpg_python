# names = ["Saf", "Nadia", "Zara" ]
# print (names[2])
# names.append ("Eli")
# print(names)

# names [0] = "Laila"
# print (names)

# del(names[2])
# print(names)

# if "Lousie" in names:
#   print ("Lousie is here")
# else:
#   print ("Louise is not here")

# print(len(names))

# names.sort()
# print(names)

# Questions:
# Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list

# food = ["Apples", "Cherries", "Pears", "Pinapple", "Peaches", "Mango"]
# print(food)

# food.append ("Grapes")
# print(food)

# food [2]= "Strawberries"
# print(food)

# del(food[0])
# print(food)

# print(len(food))

# food.sort()
# print(food)

# names = ["Saf", "Nadia", "Zara" ]
# for person in names:
#   print(person)

# for number in range(2000, 2020,4):
#   print(number)

# Section B
# # 1. Loop through the list you created in section A and print each item out
# food = ["Apples", "Cherries", "Pears", "Pinapple", "Peaches", "Mango"]
# for item in food:
#   print(item)

# 2. Print the numbers 1 to 100 (including the number 100)
# for number in range (1,101):
#   print (number)

# 3. Print all odd numbers from 1 to 100

# for number in range (1,101):
#   if number % 2 == 1:
#     print(number)

# # 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip 1916, 1940, 1944)
# for number in range (1896,2022,4):
#   if number != 1916 and number != 1940 and number != 1944:
#     print(number)

# # 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
# numbers = [10, 190, 135, 678, 49,67,58,24,56]
# even = 0
# odd = 0
# for number in numbers:
#   if number % 2 == 0:
#     even += 1
#   else:
#     odd += 1
# print("Even: " + str(even) + " Odd: " + str(odd))

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
# names = ["Mary", "Jesus", "Joseph"]
# print(names)
# for person in names:
#   print("Hello " + person)


# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
# word = ["s", "u","p","e","r","c","a","l","i","f","r","a","g","i","l","i","s","t","i","c","e","x","p","i","a","l","i","d","o","c","i","o","u","s"]
# for letter in word:
#   print (letter)

# word = "supercalifragilisticexpialidocious"
# for letter in word:
#   print (letter)

# # 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
# numbers = [1, 2, 3, 4, 5]
# squared = []

# for number in numbers:
#   squared.append (number ** 2)
# print(squared)

# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.

# names= ["George", "Frank", "Sam", "Lex", "Jason"]
# for person in names:
#   names[0]= "Dr. George"
#   names[1]= "Dr. Frank"
#   names[2]= "Dr. Sam"
#   names[3]= "Dr. Lex"
#   names[4]= "Dr. Jason"
# print(names)



# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz". E.g:

# for number in range (1,101):
#   if number % 3 ==0 and number % 5 ==0:
#     print ("Fizzbuzz")
#   elif number % 3 == 0 :
#     print ("Fizz")
#   elif number % 5 == 0 :
#     print ("Buzz")
#   else:
#     print(number)

# Section A
# 1. Print 10 random numbers
# import random 
# for x in range(1,10):
#   number = random.randint(1,10) 
#   print(number)


# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!"

# guess = None
# while guess != 7 :
#   guess = int(input("Guess a number:\n"))

# print("Wow! Lucky number 7")


#     - Rewrite so that the number being guessed is a random value from 1 to 10
# import random

# guess = None
# while guess != 7:
#   guess = random.randint(1,10)
#   print(guess)

# print("Wow! Lucky number 7!")

# import random

# computer_choice = random.randint(1,10)
# user_choice = 0
# while computer_choice != user_choice:
#   user_choice = int(input("Guess the computer's number:\n"))

# print ("Well done")

# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. E.g. 240cm x 80cm = 19200cm2 = 2m2

# import math 


# width= int(input("Please enter a width length: "))
# height= int(input("Please enter a height length: "))
# area_cm = height * width
# print("The area of this shape in cm is: " + str(area_cm))

# area_m2= (area_cm / 10000)
# print("The area of this shape in m2 is: " + str(area_m2))

# print("The area to the nearest whole number is: " + str(math.ceil(area_m2)))


# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". If they get it wrong, print "Password failure" and then ask them to enter it again. Only allow them to enter the password wrong 3 times before printing "System Locked!"

# user_input = input("Enter your password:\n ")
# password= "qwerty123"
# user_guesses= 0

# if user_input == password:
#   print ("You have successfully logged in")

# while user_guesses < 2:
#   if user_input != password:
#     print ("Password failure.")
#     user_input= input ("What is your password?\n")
#     user_guesses += 1

# print ("System failure")


# 5. Add up all the numbers from 1 to 500 and print the answer

# sum = 0
# x = 0

# while x < 500:
#   x += 1
#   sum += x

# print (sum)


# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. Find the index at which the user entered the number 99

# num_list = []
# numbers = " "
# i = 0
# x = 0

# print ("Pick 10 numbers, one of those must be 99:\n")

# while i < 10:
#   numbers = int(input("Pick a number:\n"))
# num.list.append(numbers)
# i += 1

# while x < len(num_list):
#   if num_list [x] == 99:
#     print ("Number 99 is at index " +str(x))
#   x+= 1


# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36

# i = 0 
# while i < 15:
#   print (i * 18)
#   i += 1

# 8. Print the numbers 1 to 100 (including the number 100) using a while loop
# x = 0
# while x < 100:
#   print (x + 1)
#   x += 1

 

# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a. Above 80 – A
#         b. 60 to 80 – B
#         c. 50 to 60 – C
#         d. 45 to 50 – D
#         e. 25 to 45 – E
#         f. Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

# lesson = None
# print ("Report Card:\n")

# while lesson != "":
#   lesson=input ("Input your lesson?\n")
#   mark = int(input("Input your mark:\n"))
#   if mark > 80:
#     print (lesson + ": A")
#   elif mark <= 80 and mark > 60:
#     print (lesson + ": B")
#   elif mark <= 60 and mark > 50:
#       print (lesson + ": C")
#   elif mark <= 50 and mark > 45:
#       print (lesson + ": D")
#   elif mark <= 45 and mark > 25:
#       print (lesson + ": E")
#   elif mark <25:
#       print (lesson + ": F")

# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
# import random

# entrants = []
# name = None

# while name != "":
#   name = input("Entrant's name:\n")
#   if name != "":
#     entrants.append (name)

# print(random.choice(entrants))



# 11. Create a rock, paper, scissors game which is run against computer. This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again
#     - Expand this so that its best of 3 games

import random

computer_score = 0 
user_score = 0

while computer_score < 3 and user_score < 3: 
  computer_choice = random.choice(["rock", "paper", "scissors"])
  print(computer_choice)
  user_choice = input ("Make your choice - rock, paper or scissors:\n")
  if user_choice == computer_choice:
    print ("Draw")
    computer_score += 1
    user_score += 1
  elif user_choice == "rock" and computer_choice == "paper":
    print ("You lose")
    computer_score += 1
  elif user_choice == "scissors" and computer_choice == "rock":
    print("You lose!")
    computer_score += 1
  elif user_choice == "paper" and computer_choice == "scissors":
    print("You lose")
    computer_score += 1
  elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
    user_score += 1
  elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
    user_score += 1
  elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
    user_score += 1
  else:
    print("Please pick from rock, paper or scissors to participate in the game.")
  

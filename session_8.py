# Questions:
# Section A
# 1. Read the file 'jabberwocky.txt' and print its content to the screen

f = open("jabberwocky.txt","r")
print(f.read())

# 2. Read the file 'austen.txt' and print the amount of lines in the file

f = open("austen.txt","r")
count=0
for line in f:
  count += 1

print(count)


# 3. Each line of the file 'numbers.txt' contains a number, write a script to add up all the values in the file
f = open("numbers.txt","r")
total = 0
for line in f:
  total += int(line)

print(total)



# 1. Ask the user to enter their name and append this to a file called 'register.txt'

# f = open("register.txt", "a")

# name=True
# while name != "":
#   name = input("What is your name?")
#   if name:
#     f.write(name + "\n")

# f.close()


# 2. Create a new file called 'even.txt' that contains only the even numbers from the file 'numbers.txt'
f = open("even.txt", "w")

for line in open ("numbers.txt", "r"):
  number=int(line)
  if number % 2 == 0:
    f.write(line)





# 3. 'secret.txt' contains a secret message. Each number represents the letter of the alphabet where 1 = A, 2 = B ... Z = 26. Work out what the secret message says

alphabet = {
  1: "a",
  2: "b",
  3: "c",
  4: "d",
  5: "e",
  6: "f",
  7: "g",
  8: "h",
  9: "i",
  10: "j",
  11: "k",
  12: "l",
  13: "m",
  14: "n",
  15: "o",
  16: "p",
  17: "q",
  18: "r",
  19: "s",
  20: "t",
  21: "u",
  22: "v",
  23: "w",
  24: "x",
  25: "y",
  26: "z"
  
}
f = open("secret.txt", "r")
word = ""
for line in f:
  secret = int(line)
  word=word +alphabet[secret]

print(word)





# 4. Benford’s law states that the leading digits in a collection of data are probably going to be small. For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected probability is 11.1% (i.e. one out of nine digits). Fake data is usually evenly distributed, where as real data The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data. Work out which of the files contains fake data.
def benford_calc_file(filename):
  f= open(filename,"r")
  benford_calc(f)

def benford_calc(data):
  count = {
    1: "0",
    2: "0",
    3: "0",
    4: "0",
    5: "0",
    6: "0",
    7: "0",
    8: "0",
    9: "0"
  }


for line in data:
  count[line[0]] += 1

for x in range(1,10):
  print(str(x) + " = " + str(count[str(x)]/100+"%")

for x in range (1,4):
  filename="accounts_" + str(x) + ".txt"
  print(filename)
benford_calc_file(filename)

benford_calc(["1","10","30","55"])







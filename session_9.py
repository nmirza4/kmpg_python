def first_last(word="hello"):
  return (word[0], word[-1])
  print("run?")

first, last = first_last()
print(first)
print(last)


def circle(c):
  PI=3.141
  r=c/(2*PI)
  a=PI*(r**2)

  return r,a


radius,area=circle(100)
print(radius,area)






def search_file(path,q):
  f=open(path,"r")

  for n, line in enumerate(f):
    if line.startswith(q):
      print("Line: " + str(n+1) +"-" + line)

search_file("hello.txt","hello")



def save_data(*args):
  f=open("data.txt","w")

  for arg in args:
    f.write(str(arg)+"\n")

  f.close()

save_data("hello",1,"world",2,3,4,5,6)




def save_data(**kwargs):
  f=open("data.txt","w")

  for key in kwargs.items():
    f.write(f"{key}: {value}\n")
    print(f"{key}:------{value}")
    
  f.close()

save_data(fname="Alice", lname="Smith", phone="555-1234")





def calculator(*args, operand= "add"):
  total=args[0]

  for arg in args[1:]:
    if operand in ["add","+", "plus"]:
      total += arg
    elif operand == "*":
      total *= arg
    elif operand == "/":
      total /= arg

  retun total

print (calculator(1,2,3))
print (calculator(1,2,3,4, operand="add"))
print (calculator(5,7,operand="*"))




import csv

def save_data(w, **kwargs):
  w.writerow(kwargs.values())

fields = ["fname", "lname", "phone"]

f=open("data.csv","w")
w=csv.writer(f)

w.writerow(fields)

# save_data(w=w, fname="Alice", lname="Smith", phone= "555-1234")
# save_data(w=w, fname="Jake", lname="Smith", phone= "123456789")

keep_asking= True
while keep_asking:
  data= {}
  for x in fields:
    data[x] = input(x)

  if data["fname"]:
    save_data(w=w, **data)
  else:
    keep_asking=False

f.close()
  

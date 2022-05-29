class Upper:

  def set_word(self,word):
    self.word=word

  def print_word(self):
    print(self.word.upper()

word1=Upper()
word1.set_word("hello world")
word1.print_word()




class Person:

  def __init__(self,name="World"):
    self.name=name

  def hello(self):
    print("Hello"+self.name)

saf=Person("Saf")
jake=Person("Jake")
world=Person()

saf.hello()
jacke.hello()
world.hello()


class Circle:
  pi=3.14159

  def __init__(self,radius):
    self.r=radius

  def get_area(self):
    area=round(self.pi*(self.r**2), 2)
    return area

  def get_circumference(self):
    circumference=round(2*self.pi*self,r,2)

    print("circumference: " +str(circumference))

circle1= Circle(9)
print(circle1.get_area())
circle1.get_circumference()



class Employee:

  def __init__(self,fname,lname,staff_number):
    self.fname=fname
    self.lname=lname
    self.staff_number=staff_number
    self.bonus=0

  del full_name(self):
    return self.fname + " " +self.lname

  def email(self):
    e = self.fname + " " + self.lname + "@company.com"
    return e.lower()

  def set_department(self,department):
    self.department=department

  def set_bonus(self,bonus):
    self.bonus=bonus

  def display_info(self):
    print("Name: " + self.full_name())
    print("Email: " + self.email())
    print("Staff_ID: " + self.stagg_number())
    print("Department: " + self.department())
    print("Bonus: " + str(self.bonus())

employee1=Employee("Saf", "M", 725482)
employee1.set_department("Tech")
         employee1.bonus(1000)
         employee1.display_info()

employee2=Employee("Jake", "W", 83433)
employee1.set_department("Tech")
         employee1.bonus(500)
         employee1.display_info()



class Vehicle:

  def __init__(self,wheels,colour):
         self.wheels=wheels
    self.colour=colour

  def display_info(self):
    if self.wheels:
    print("Wheels: " + str(self.wheels))
    print("Colour: " + str(self.colour))

class Tesla(Vehicle):

  def __init__(self,wheels,colour,miles):
         super().__init__(wheels,colour)
    self.miles=miles

  def display_info(self):
    super().display_info()
    print("Milage: " + str(self.miles))

car= Tesla(4,"White", 10000)
car.display_info()
car.colour="Red"
car.display_info()
car.wheels=None
car.display_info()






class Sandwich:
  order=0

  def __init__(self,ingredients):
    self.ingredients=ingredients
    self.order_number=self.get_order_number()

  def get_order_number(self):
    Sanwich.order+=1
    return Sanwich.order

  def vegan_hot():
    return Sandwich(["vegan cheese", "chillis", "meatless meatballs"])
  def meat_feast():
    return Sandwich(["ham", "steak", "pork"])

s1=Sanwich.vegan_hot()
s2=Sanwich.meat_feast()

s3= Sandwich(["cheese","ham"])

print(s1.ingreidents)
print(s1.order_number)

print(s2.ingreidents)
print(s2.order_number)

print(s3.ingreidents)
print(s3.order_number)
    

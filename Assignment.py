#  List
list.append("black")
print (list)
list.clear()
print (list)

list=["rose","green","orange","blue"]
X=list.copy()
print (X)

list=["rose","green","orange","blue"]
X=list.count("green")
print (X)

list=["rose","green","orange","blue"]
mylist=["red","white"]
list.extend(mylist)
print (list)

list=["rose","green","orange","blue"]
print (list.index("blue"))


list=["rose","green","orange","blue"]
list.insert(2,"violet")
print (list)

list=["rose","green","orange","blue"]
list.pop()
print (list)

list=["rose","green","orange","blue"]
list.remove("rose")
print (list)

list=["rose","green","orange","blue"]
list.reverse()
print (list)

#  Tuple
Tuple=(2,6,8,1,9)
X=Tuple.count(2)
print(X)

Tuple=(3,"hi",4,2)
X=Tuple.index(4)
print(X)


#Dictionary
dict={"name":"chitti","age":30,"mail":"abc.com"}
dict.clear()
print (dict)

dict={"name":"chitti","age":30,"mail":"abc.com"}
X=dict.copy()
print (X)

x = ('key 1', 'key 2', 'key 3')
y = 0
dict = dict.fromkeys(x, y)
print(dict)

dict={"name":"chitti","age":30,"mail":"abc.com"}
X=dict.get("name")
print (X)

dict={"name":"chitti","age":30,"mail":"abc.com"}
X=dict.keys()
print (X)

dict={"name":"chitti","age":30,"mail":"abc.com"}
X=dict.values()
print (X)

dict={"name":"chitti","age":30,"mail":"abc.com"}
X=dict.items()
print (X)


dict={"name":"chitti","age":30,"mail":"abc.com"}
dict.pop("mail")
print (dict)

dict={"name":"chitti","age":30,"mail":"abc.com"}
dict.update({"roll":20})
print (dict)

# string

mess="hi Hello Mycaptin"
X=mess.capitalize()
print (X)

mess="hi Hello Mycaptin"
Y=mess.casefold()
print (Y)

mess="hi Hello Mycaptin"
Y=mess.center(30)
print (Y)

mess="hi Hello Mycaptin"
Y=mess.count("hi")
print (Y)

mess="hi Hello Mycaptin"
Y=mess.encode()
print (Y)

mess="hi Hello Mycaptin"
Y=mess.endswith(".")
print (Y)

mess="hi Hello Mycaptin"
Y=mess.find("hi")
print (Y)

mess="hi Hello Mycaptin"
Y=mess.index("Mycaptin")
print (Y)

mess="hi Hello Mycaptin"
Y=mess.isupper()
print (Y)

mess="hi Hello Mycaptin"
Y=mess.islower()
print (Y)

mess="hi Hello Mycaptin"
Y=mess.split()
print (Y)

mess="hi Hello Mycaptin"
Y=mess.swapcase()
print (Y)

mess="hi Hello Mycaptin"
Y=mess.title()
print (Y)

#  sets

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

fruits = {"apple", "banana", "cherry"}
X=fruits.copy()
print(X)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

# if condition

a=int(input ("enter a value"))
b=int(input ("enter b value"))
if a<b:
 print ("a is smaller than b")
elif a>b:
 print ("b is smaller than a")
elif a==b:
 print ("a and b are equal")

#Loops


# for loop
fruits = ["apple", "mango", "grapes"]
for x in fruits:
  print(x)

#  while loop
i = 3
while i < 9:
  print(i)
  i += 1
# nested loop
Colour = ["red", "green", "red"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


#  calculator

class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=cal(a,b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else: 
        print ("invalid choice")


 #  OR


def cal():
    x = ('1. Add \n2. Sub \n3. Multiply \n4. Divide')
    print(x)
cal()

cal1 = input('Enter your choice: ')

num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number: '))

if cal1 == '1':
    x1 = num1 + num2
    print('Total number: ' + str(x1))
elif cal1 == '2':
    x2 = num1 - num2
    print('Total number: ' + str(x2))
elif cal1 == '3':
    x3 = num1 * num2
    print('Total number: ' + str(x3))
elif cal1 == '4':
    x4 = num1 / num2
    print('Total number: ' + str(x4))
else:
    print("Invalid input")   







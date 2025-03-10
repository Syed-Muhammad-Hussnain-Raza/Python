# Task 1: Print Hello World
print("Hello World")

# Task 2: Variables and Data Types
a = 10
b = 3.64
c = "COMSATS University Islamabad "
d = "Lahore Campus"
e = True

sum = a + b # arithmetic operation
print(sum)

concatenate = c + d # concatenation
print(concatenate)

# Task 3: Conditional Statements
marks = 80 #int(input("Enter your marks: "))
if marks >= 90:
   print("A+")
elif marks >= 80:
   print("A")
elif marks >= 70:
   print("B")
elif marks >= 60:
   print("C")
elif marks >= 50:
   print("D")
else:
   print("Fail")

# Task 4: Loops
for i in range(1, 6):
   print(i, end=" ")
print() # new line

i = 6
while i <= 10:
   print(i, end=" ")
   i += 1
print() # new line

# Task 5: List and Dictionary
list = [1, 2, 3, 4, 5]
print(list)
list.append(6)
list.append(7)
print(list)

list.remove(3)
print(list)

# list.remove(10) # Error
print(list.index(5))

dict = {
   "name": "Syed Muhammad Hussnain Raza",
   "age": 21,
   "city": "Faisalabad"
}

print(dict)
print(dict["name"])
print(dict["age"])
print(dict["city"])

dict.update({"country": "Pakistan"})
print(dict)

# Task 6: Functions
def add(a, b):
   return a + b
def subtract(a, b):
   return a - b
def multiply(a, b):
   return a * b
def divide(a, b):
   return a / b

def calculator(a, b, operator):
   if operator == "+":
      return add(a, b)
   elif operator == "-":
      return subtract(a, b)
   elif operator == "*":
      return multiply(a, b)
   elif operator == "/":
      return divide(a, b)
   else:
      return "Invalid Operator"
   
print("Sum:", calculator(10, 5, "+"))
print("Multiplication:", calculator(10, 5, "*"))

# Task 7: Input and Output
name = input("Enter your name: ")
print("Hello", name)

# Task 8: File Handling
file = open("file.txt", "a+")
file.write("Welcome to First LAB for AI.\n")
file.close()

file = open("file.txt", "r")
print(file.read())
file.close()

# Task 9: Error Handling
try:
   print(10/0)
except ZeroDivisionError:
   print("Division by Zero Error")
except:
   print("Error")
finally:
   print("Finally Block Execution")

# Task 10: Module and Library
import random  # Importing Random Module
print(random.randint(1, 10))  # Generate Random Number between 1 to 10

# Task 11: String Manupulation
string = "Hello World"
string = string.upper()

first = string[0:5] # Hello
last = string[6:] # World

print(first + last)
print(string.replace("WORLD", "Python"))
print("Length of string:", len(string))

print(string.find("WORLD")) # 6th index (starting index where match)
print(string.find("Python")) # -1 (not found)

# Task 12: Basic Algorithms
def factorial(n):
   if n == 0:
      return 1
   return n * factorial(n-1)

print("Factorial of 5:", factorial(5))

# linear searching
def linear_search(arr, key):
   for i in range(len(arr)):
      if arr[i] == key:
         return i
   return -1

# bubble sort
def bubble_sort(arr):
   for i in range(len(arr)):
      for j in range(len(arr)-1):
         if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
   return arr

arr = [5, 3, 8, 1, 2, 9, 4]
key = 8
print("Original array:", arr)
print("Index of", key, "is", linear_search(arr, key))
print("Array after sorting:", bubble_sort(arr))

# Task 13: Object Oriented Programming
class Student:
   name = ""
   age = 0
   roll_no = ""
   def __init__(self, name, age, roll_no):
      self.name = name
      self.age = age
      self.roll_no = roll_no
   
   def set_name(self, name):
      self.name = name

   def display(self):
      print("Name:", self.name)
      print("Age:", self.age)
      print("Roll No:", self.roll_no)

student = Student("Syed Muhammad Hussnain Raza", 21, "FA23-BCS-197")
student.display()

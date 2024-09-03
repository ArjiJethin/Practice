import os

"""str = "Hello World"
print(str[0:12:2])"""

"""
for i in range(0,20):
    if i == 12:
        print("Umm")
        continue
    elif i == 13:
        continue
    elif i == 14:
        print("hehe :)")
        continue
    print(i)
"""

"""
def add(x,y):
    return x+y
result = add(2,3)
print(f"Result: {result}")"""

"""
def adder(*var):
    result = 0
    for i in range(len(var)):
        if var[i] == 0 and (i+1 < len(var) and var[i+1] == 0):
            break
        result += var[i]
    return result

output = adder(1, 2, 3, 0, 5, 56, 6, 7, 7)
print(f"Value: {output}")

"""

"""
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

result = fact(5)
print(f"Factorial: {result}")
"""

"""
add = lambda x, y: x + y
value = add(2, 3)
print(f"Value: {value}")
"""

"""
file = "Text.txt"
with open(file,'r') as f:
    str = f.read()
    print(str)
"""

"""
try:
    os.rename("ttext.txt", "text.txt")
except FileNotFoundError:
    print("File Not Found")
"""

"""
with open("text.txt", 'r') as f1:
    with open("bin.txt", 'w') as f2:
        data = f1.read()
        f2.writelines(data)
#os.remove("bin.txt")
"""

"""
def count_words(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            if line and not line.lstrip().startswith('M'):
                count += 1
    return count

result = count_words("text.txt")
print(f"Number of lines that starts without M: {result}")
"""

"""
class Dog:
    species = "canine"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Sammi", "Husky")
dog2 = Dog("Casey", "Chocolate Lab")

print(f"Dog:  Name: {dog1.name}, Breed: {dog1.breed}, species = {Dog.species}")
print(f"Dog:  Name: {dog2.name}, Breed: {dog2.breed}, species = {Dog.species}")
"""

"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self,other):
        total_marks = self.marks + other.marks
        return Student(f"{self.name} & {other.name}", total_marks)

    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}"

student1 = Student("Mark", 85)
student2 = Student("Phoenix", 90)

combined_student = student1 + student2
print(combined_student)
"""


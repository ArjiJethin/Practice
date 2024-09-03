# ----------------------------------------------------------- Question 1B ------------------------------------------------------------------------

"""
qty = float(input("Enter the amount of items sold: "))
val = float(input("Enter the value of item: "))
discount = float(input("Enter the discount percentage: "))
tax = float(input("Enter the tax: "))
amt = qty*val
disc_amt = (amt*discount)/100
sub_total = amt - disc_amt
tax_amt = (sub_total*tax)/100
total_amt = sub_total+tax_amt
print("******************************BILL********************************")
print(f"Quantity Sold:\t {qty}")
print(f"Price per item:\t {val}")
print("\t\t-----------------------------------------")
print(f"Amount: \t{amt}")
print(f"Discount amt: \t {disc_amt}")
print("\t\t-------------------------------------------")
print(f"Discounted Total: \t {sub_total}")
print(f"Tax: \t{tax_amt}")
print("\t\t-------------------------------------------")
print(f"Total Amount: \t {total_amt}")
"""
# ----------------------------------------------------------- Question 2A ------------------------------------------------------------------------

"""
a = int(input("Enter the coefficient- 'a' : "))
b = int(input("Enter the coefficient- 'a' : "))
c = int(input("Enter the coefficient- 'a' : "))
D = b**2 - (4*a*c)
deno = 2*a

if D > 0:
    print("Real and Unique Roots:-")
    R1 = (-b + D**0.5)/(2*a)
    R2 = (-b - D**0.5)/(2*a)
    print(f"Root 1: '{R1}', Root 2: '{R2}' ")
elif D == 0:
    print("Real and Equal Roots")
    R = -b/(2*a)
    print(f"The roots are {R} & {R}")
else:
    print("Imaginary Roots:-")
    D = D - (2*D)
    Real = -b/(2*a)
    Img = D**0.5/(2*a)
    print(f" Root 1: '{Real}+{Img}i & Root 2: '{Real} - {Img}''")
"""

# ----------------------------------------------------------- Question 2B ------------------------------------------------------------------------

""""
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    if i % 2 == 0:
        term = i**2
    else:
        term = 0
    sum += term
print(f"Sum = {sum}")
"""

# ----------------------------------------------------------- Question 3A ------------------------------------------------------------------------

"""
def increment(y):
    return (lambda x: x+1)(y)


n = int(input("Enter a number: "))
print(f"Number before incrementing: {n}")
n = increment(n)
print(f"Number after incrementing: {n}")
"""

# ----------------------------------------------------------- Question 3B ------------------------------------------------------------------------

"""
from mod import add
a = int(input("Enter a: "))
b = int(input("Enter b: "))
result = add(a,b)
print(f"Result = {result}")
"""

# ----------------------------------------------------------- Question 4A ------------------------------------------------------------------------

"""
message = input("Enter a string: ")
key = int(input("Enter a number: "))
index = 0
while index < len(message):
    letter = message[index]
    print(chr(ord(letter)+key), end="")
    index += 1
"""

# ----------------------------------------------------------- Question 4B ------------------------------------------------------------------------

"""
while 1:
    name = input("Enter your name: ")
    if not name.isalpha():
        print("Invalid Name, please try a gain :(")
    else:
        break
while 1:
    pan_card_no = input("Enter your Pan Card No: ")
    if not name.isalnum():
        print("Invalid PAN No. , please try a gain :(")
    else:
        break
print(f"Please Check, Name: {name} & Pan Card No: {pan_card_no}")
"""

# ----------------------------------------------------------- Question 5A ------------------------------------------------------------------------

"""
with open("text.txt", "r") as f1:
    with open("copy.txt", "w") as f2:
        for line in f1:
            f2.write(line)

print("Contents have been copied")
"""

# ----------------------------------------------------------- Question 5B ------------------------------------------------------------------------

"""
import urllib.request
url = "https://en.wikipedia.org/wiki/Phoenix"
headers = {}
Request = urllib.request.Request(url, headers=headers)
Response = urllib.request.urlopen(Request)
Data = Response.read()
with open("UrlOpen.txt", "w") as f:
    f.write(str(Data))
print("Contents written :)")
"""

# ----------------------------------------------------------- Question 6A ------------------------------------------------------------------------

"""
def count_word_frequency(filename):
    word_frequency = {}
    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.strip(".,?!")
                if word:
                    word_frequency[word] = word_frequency.get(word, 0)+1
    print("Word Frequency:-")
    for word, frequency in word_frequency.items():
        print(f" {word} : {frequency}")

def main():
    filename = input("Enter filename: ")
    count_word_frequency(filename)


if __name__ == "__main__":
    main()
"""

# ----------------------------------------------------------- Question 6A ------------------------------------------------------------------------

def list_methods_demo():
    my_list = [1, 2, 3, 4]
    my_list.append(5)
    print(f"Appended List = {my_list}")
    my_list.extend([5,6,7])
    print(f"Extended List = {my_list}")
    my_list.insert(0,0)
    print(f"Inserted List: {my_list}")
    my_list.remove(7)
    print(f"Removed List = {my_list}")
    popped_element = my_list.pop(-1)
    print(f"Popped Element = {popped_element}")

def tuple_methods_demo():
    my_tuple = (1,2,3,4)
    index = my_tuple.index(3)
    print(f"Index of the number 3: {index}")
    count = my_tuple.count(4)
    print(f"Count of element 4: {count}")

def set_methods_demo():
    my_set = {1,2,3,4,5}
    my_set.add(6)
    print(f"Added Set: {my_set}")
    my_set.remove(6)
    print(f"Removed Set: {my_set}")
    popped_element = my_set.pop()
    print(f"Popped Element: {popped_element}")

def dictionary_methods_demo():
    my_dict = {'a':1, 'b':2, 'c':3}
    value = my_dict.get('b')
    print(f"Value of b: {value}")
    my_dict.update({'d':4})
    print(f"Updated Dictionary: {my_dict}")
    popped_value = my_dict.pop('d')
    print(f"The popped value: {popped_value}")

def main():
    print("List Methods:-")
    list_methods_demo()
    print("\nTuple Methods:-")
    tuple_methods_demo()
    print("\nSet Methods:-")
    set_methods_demo()
    print("\nDictionary Methods:-")
    dictionary_methods_demo()


if __name__ == "__main__":
    main()



    





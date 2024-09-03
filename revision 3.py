"""
import urllib.request
url = "https://en.wikipedia.org/wiki/Phoenix"
headers = {}
Request = urllib.request.Request(url,  headers=headers)
Response = urllib.request.urlopen(Request)
Data = Response.read()
with open("UrlOpen.txt", "w") as f:
    f.write(str(Data))
print("Contents Written")
"""

"""
def count_word_frequency(filename):
    word_frequency = {}
    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.strip("?.,!")
                if word:
                    word_frequency[word] = word_frequency.get(word,0)+1
    print("Word Frequency:-")
    for word, frequency in word_frequency.items():
        print(f" {word} : {frequency}")

def main():
    filename = input("Enter Filename: ")
    count_word_frequency(filename)

if __name__ == "__main__":
    main()
"""

def list_methods_demo():
    my_list = [1,2,3,4]
    my_list.append(5)
    print(f"Appended List: {my_list}")
    my_list.extend([5,6])
    print(f"Extended List = {my_list}")
    my_list.insert(0,0)
    print(f"Inserted List: {my_list}")
    my_list.remove(6)
    print(f"Removed List: {my_list}")
    popped_element = my_list.pop(-1)
    print(f"Popped element: {popped_element}")

def tuple_methods_demo():
    my_tuple = (1,2,3,4)
    index = my_tuple.index(4)
    print(f"Index of the number of 4: {index}")
    count = my_tuple.count(3)
    print(f"Count of element 3: {count}")

def set_methods_demo():
    my_set = {1,2,3,4,5}
    my_set.add(6)
    print("Added Set: ", my_set)
    my_set.remove(6)
    print("removed Set = ", my_set)
    popped_element = my_set.pop()
    print(f"The popped element is {popped_element}")

def dictionary_methods_demo():
    my_dict = {'a':1, 'b':2, 'c':3}
    value = my_dict.get('c')
    print(f"Value of 'c': {value}")
    my_dict.update({'d':4})
    print(my_dict)
    popped_value = my_dict.pop('d')
    print(f"Popped Value: {popped_value}")

def main():
    print("List Methods:- ")
    list_methods_demo()
    print("\nTuple Methods:-")
    tuple_methods_demo()
    print("\nSet Methods:-")
    set_methods_demo()
    print("\nDictionary Methods:-")
    dictionary_methods_demo()


if __name__ == "__main__":
    main()

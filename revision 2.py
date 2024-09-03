"""
with open("Text.txt", "r") as f1:
    with open("copy.txt", "w") as f2:
        for line in f1:
            f2.write(line)

print("Contents have been written :)")
"""

"""
import urllib.request
url = "https://en.wikipedia.org/wiki/Phoenix"
headers = {}
Request = urllib.request.Request(url, headers = headers)
Response = urllib.request.urlopen(Request)
Data = Response.read()
with open("UrlOpen.txt", "w") as f:
    f.write(str(Data))
print("Contents Written! :)")
"""

def count_word_frequency(filename):
    word_frequency = {}
    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.strip("?,:!")
                if word:
                    word_frequency[word] = word_frequency.get(word,0)+1

    print("Word Frequency:-")
    for word, frequency in word_frequency.items():
        print(f"{word} : {frequency}")


def main():
    filename = input("Enter filename: ")
    count_word_frequency(filename)


if __name__ == "__main__":
    main()


def frequency(file_name, word):
    try:
        with open(file_name, "r") as f:
            occurrence = 0
            for line in f:
                occurrence += line.lower().count(word.lower())
        print("Occurrences =", occurrence)
    except FileNotFoundError:
        print("File not found :(")


filename = "../Text.txt"
word_to_find = "Malevolent"
frequency(filename, word_to_find)
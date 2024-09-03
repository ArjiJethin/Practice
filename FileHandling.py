import os

f = open("Text.txt", 'r+')

"""f.write('Hello World\n')
f.write('This is my programme\n')
f.write('Hehe\n')
f.write(':)\n')"""
# print(f.read())
for line in f:
    print(line, end='')
# os.rename("Text.txt", "text.txt")

f.close()
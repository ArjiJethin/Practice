f = open("../Text.txt", "r")
lines = f.readlines()
count = 0
for line in lines:
    if line[0] == 'M' or line[0] == 'm':
        continue
    else:
        count += 1
print("No of Lines",count)
f.close()

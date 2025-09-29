file = open("2.4/responses.csv")

# junk = file.readline()
# data = file.readline()

# print(data)
# datalist = data.split(",")
# print(datalist)
lines = []


for number in file:
    if "3" in number.lower():
        print(number)

for line in file:
    lines.append(line.split(","))
print(lines)


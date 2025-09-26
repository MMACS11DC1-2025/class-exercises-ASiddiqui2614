file = open("2.4/responses.csv")

# junk = file.readline()
# data = file.readline()

# print(data)
# datalist = data.split(",")
# print(datalist)
lines = []


for person in file:
    if "ashar" in person.lower():
        print(person)

for line in file:
    lines.append(line.split(","))
print(lines)


file = open("2.4/responses.csv")

# junk = file.readline()
# data = file.readline()

# print(data)
# datalist = data.split(",")
# print(datalist)
lines = []


for music in file:
    if "rock" in music.lower():
        print(music)

for line in file:
    lines.append(line.split(","))
print(lines)


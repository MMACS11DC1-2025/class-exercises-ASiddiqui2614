file = open("2.4/responses.csv")

# junk = file.readline()
# data = file.readline()

# print(data)
# datalist = data.split(",")
# print(datalist)



for person in file:
    if "ashar" in person.lower():
        print(person)
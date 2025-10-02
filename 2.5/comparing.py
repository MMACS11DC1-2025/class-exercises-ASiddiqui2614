"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
file = open("2.4/responses.csv")
lines = []
ppl = []
nameid = 0
for line in file:
    lines.append(line.lower().split(","))


answer = input("What is your full name? \n").lower().strip()

#finds user id
for person in range(len(lines)):
    if answer == lines[person][1].lower():
        nameid = int(lines[person][0])

#finds whoever is similar to user based on their choice of pet and music preferance
#person is other person. here, we are checking to make sure it's not comparing to user
for person in range(len(lines)):
    if person != nameid:
        simiAmount = 0
        for i in [3, 7]:
            if lines[nameid][i] == lines[person][i]:
                simiAmount += 1
        # print(person)
        # print(simiAmount)
        if simiAmount == 2:
            ppl.append(int(lines[person][0]))


#output
for person in ppl:
    print("You are most similar to " + lines[person][1] + " in terms of your favorite animal and music choice")
    


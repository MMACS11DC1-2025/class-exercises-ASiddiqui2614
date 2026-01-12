"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""

num1 = input("Enter your first number: ")
op = input("Enter your operation: ")
num2 = input("Enter your second number: ")

answer = 0

if op == "+":
    answer = float(num1) + float(num2)
elif op == "/":
    answer = float(num1) / float(num2)
elif op == "*":
    answer = float(num1) * float(num2)
elif op == "-":
    answer = float(num1) - float(num2)
    
print("The answer is " + str(answer))

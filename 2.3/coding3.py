"""
Write a McDoland's program that takes your order and outputs the total cost.

It first asks if you want a burger for $5. It then asks if you want fries for $3. It outputs the total with 14% tax.

The program should accept Yes/No or yes/no.

Example:

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> yes
Your total is $9.12

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> no
Your total is $5.699999999999999

Would you like a burger for $5? (Yes/No)
> no
Would you like fries for $3? (Yes/No)
> yes
Your total is $3.42
"""
burger = input("Welcome to McDonalds, \n Would you like a burger for $5? ")

fries = input("Would you like some fries for $3? ")

burger = burger.lower()
fries = fries.lower()

if burger == "yes" and fries == "yes":
    print("Your total is $3.42")

elif burger == "yes" and fries == "no":
    print("Your total is $5.70")

elif burger == "no" and fries == "yes":
    print("Your total is $3.42")

else:
    print("Okay, have a nice day, bye")
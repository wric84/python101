
# If statements
# An if statement is used to compare things

# variable = input("This is an input that will take a response")
# print(variable)

# Going to ride the coney island roller coaster
# 4' aka 48''
# height = int(input("How tall are you? "))
# # height >= 48
# if height >= 48:
#     print("You may ride")
# else:
#     print("Sorry kid, get lost. Come back next year")

# create a password checker
# username = HotDogWater123
# password = bluepen

# password = "bluepen"

# userLoginInput = input("Enter Password: ")

# one = is equivalent to assigning a value. If we want to compare, then we need to use two ==
# if userLoginInput == password:
#     print("Open Sesame")
# else:
#     print("Access denied!")

# update if statement to while loop so that users can have multiple attempts
# while userLoginInput != password:
#     print("Wrong password - please try again")
#     userLoginInput = input("Enter Password: ")

# print("Open Sesame")

# Check if number is even or odd using the != (not equal to operator):
# number = int(input("Enter a number: "))

# if number % 2 != 0:
#     print("Yay this is an odd number")
# else:
#     print("this is an even number")

# if number % 2 == 0:
#     print("this is an even number")
# else:
#     print("Yay this is an odd number")

# print(5/2)
# print(4/2)
# print(11%3)
# print(11%5)
# print(11%7)
# print(11%2)

# Write a for loop for the value 1-152
# numbers = [1,2,3,4,...]
# for number in range(1, 153):
#     print(number)

# countdown from 10 - 0
# for number in range(10, 0, -1):
#     print(number)
#     # print statement is inside for loop, so it will print each time
#     # print("Blast off!")
# print("Blast off!")

# # Who likes root beer?
# numberOfRootBeers = int(input("Number of bottles of root beer in your fridge: "))

# for i in range(numberOfRootBeers, 1, -1):
#     print(f"{i} bottles of root beer on the wall...")
#     print(f"{i} bottles of root beer")
#     print("take on down, pass it around...")
#     print(f"{i-1} bottles of root beer on the wall")

# What is the sum of 1-427
# total = int(input("Pick a number to add up to: "))

# for number in range(1, total+1):
#     total += number

# print(f"Your total is: {total}!")

# find the largest number
# numberList = [7, 42, 8, 946, -1, 6, 730]

# # first number in this case is 7
# largestNumber = numberList[0] 
# print(largestNumber)

# for number in numberList:
#     # first iteration says "Is 7 larger than 7? if not move on to second iteration, if so... then the new largest number becomes the value we're checking in the list"
#     if number > largestNumber:
#         largestNumber = number

# print(largestNumber)

# Who wants to play.... GUESS THAT NUMBER!
secretNumber = 7

guess = 0

while guess != secretNumber:
    guess = int(input("Guess the secret number: "))

print("You got it!")
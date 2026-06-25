# print("Hello World")
# print("My name is Colton")

# # ctrl+/ is how we make a comment
# # this is a string example
# learner = "Optimus Prima"
# print(learner)

# # this is a number/integer example
# ideal_number_of_pets = 2
# print(ideal_number_of_pets)

# # This is a float/decimal example
# how_much_is_a_banana = 9.99
# print(how_much_is_a_banana)

# # This is an example of a Boolean True/False
# is_our_pets_vaccinated = True
# print(is_our_pets_vaccinated)

# print(type(learner))
# print(type(ideal_number_of_pets))
# print(type(how_much_is_a_banana))
# print(type(is_our_pets_vaccinated))

# is_it_a_number = 333
# is_this_a_number = "333"

# print(type(is_it_a_number))
# print(type(is_this_a_number))

# statement = "The number of pets I want is 2 dogs"

# puppy_name = "Buddy"
# what_is_buddys_age = 3
# how_old_is_colton = 21.5
# is_line_36_true = True
# zipcode = "100001"

# # ctrl+/
# # print(statement)
# # print(statement)
# # print(statement)
# # print(statement)

# # print(5+3)
# # print(5*3)
# # print(5-3)
# # print(5/3)

# # print(10/5)
# # print(7/3)
# # print(12/4)
# # print(99/8)

# # Example of a modulo
# print(10%3)
# print(10/3)
# print(10%5)

# # Show an example of an exponent "power to the 5th"
# print(2**5)
# print(2**2)
# print(32**73)

# find the area of a rectangle
# length = input("What is the length")
# length = int(input("What is the length?"))
# # width = 20
# width =int(input("What is the width? "))

# area = length * width

# print(f"Your total area is {area}")

# Find the tax amount
# price = 10
# tax = price * 0.08

# print(f"The tax on the item given is: {tax}")

# # # Find the average
# avg = (10+10+10)/3
# print(f"The average from the measurements given is {avg}")

# # Ask the user their favorite color
# fav_color = input("What is your favorite color?")

# # print(fav_color)
# print(f"Your favorite color is {fav_color}")

# This is a comment to test multiple inputs
# print("This","is","What","They","Are","Talking","About")

# print(12, 24, -2, sep=':')
# print('but', 'not', 'including', sep='**')
# print('but', 'not', 'including', sep='')

# create a receipt
customerName = input("Enter customer's name: ")
itemPrice = float(input("What is the cost of the item: "))
quantity = int(input("Enter quantity: "))
totalCost = itemPrice*quantity
roundedCost = round(totalCost,2)

print("Receipt")
print("--------------------")
# customer Name
print(f"Customer: {customerName}")
# the price of what they purchased
print(f"Item price: ${itemPrice}")
# The quantity of the product they purchased
print(f"Quantity: {quantity}")
# The total cost
print(f"Total Cost: ${roundedCost}")

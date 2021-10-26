# Part 1

# Take the following lists

dogs = ["fido", "spot", "lucky"]

cats = ["fluffy", "snowball", "garfield"]

# And combine them into a list called pets.

dogs.extend(cats)
pets = dogs

# Part 2

# Using the same lists from above,
# create a dictionary called my_pets
# that has the keys of 'dogs' and 'cats'
# with the values being the appropriate
# lists.


# Improve this! You already have these lists built, no need to type them again
my_pets = {
        'dogs': pets[:3],
        'cats': pets[3:]
        }

print(my_pets)

# Part 3

# Prove you can use the pets list to print
# "I only own spot and snowball"

print(f"I only own {pets[1]} and {pets[4]}")

# Part 4

# Prove you can use the my_pets dict to print
# "I want to adopt fido and garfield too" 

print(f"I want to adopt {my_pets['dogs'][0]} and {my_pets['cats'][2]} too")

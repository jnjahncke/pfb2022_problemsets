#!/usr/bin/env python3

# Dictionary of my favorite things
fave = {"food" : "cheese",
		"dessert" : "ice cream",
		"animal" : "dog",
		"book" : "The Circle",
		"tree" : "magnolia"}

# Print favorite book
print("Favorite book:",fave['book'])

# Print my absolute favorite thing
fav_thing = "dessert"
print("My absolute favorite thing:",fave[fav_thing])

# Print favorite tree
print("My favorite tree:",fave["tree"])

# Add favorite organism to the dictionary
fave["organism"] = "mus musculus"
# Make organism the value of `fav_thing`
fav_thing = "organism"
print("My absolute favorite thing:",fave[fav_thing])

# Take "thing" from input and print out the favorite
print(f'\nPick a category: {list(fave.keys())}')
fav_thing = input("Which of my favorite things do you want to know? ")
while fav_thing not in fave:
	print(f"""I don't have a favorite {fav_thing}.
Try something else.""")
	print(list(fave.keys()))
	fav_thing = input("Which of my favorite things do you want to know? ")
print(f'My favorite {fav_thing}: {fave[fav_thing]}')

# Ask the user to input a category and the favorite in that category
# Change that item in the dictionary
print(f'\nPick a category: {list(fave.keys())}')
usrcategory = input("Enter a category: ")
while usrcategory not in fave:
	print(f"""I don't have a favorite {usrcategory}.
Try something else.""")
	print(list(fave.keys()))
	usrcategory = input("Enter a category: ")
usrthing = input(f"What is your favorite {usrcategory}? ")
fave[usrcategory] = usrthing

# Change favorite organism
fave["organism"] = "c. elegans"

print("\nOur favorite things:")
# Use a for loop to print out each key and value of the dictionary
[print(f'{i:<12}	{fave[i]:<12}') for i in fave]

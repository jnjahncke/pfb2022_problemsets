#!/usr/bin/env python3

# Print numbers 1 to 100
x = 1
while x < 101:
	print(x)
	x += 1

print('\n\n')
# Calculate the factorial of 1000
x = 1
fact = 1
while x < 1000:
	fact = fact*x
	x += 1
print(fact)


print('\n\n')
# Iterate through list
for x in [101,2,15,22,95,33,2,27,72,15,52]:
	if x%2 == 0:
		print(x)

print('\n\n')
# Sort, then iterate
# Print each element
# Calculate a cumulative sum of even values and another of odd values
# Print only the final two sums
even = 0
odd = 0
for x in [101,2,15,22,95,33,2,27,72,15,52]:
	print(x)
	if x%2 == 0:
		even = even + x
	else: 
		odd = odd + x
print(f'Sum of even numbers: {even}')
print(f'Sum of odds: {odd}')



print('\n\n')
# Print every number between 0 and 99
for x in range(0,100):
	print(x)

print('\n\n')
# Print every number between 1 and 100
for x in range(1,101):
	print(x)

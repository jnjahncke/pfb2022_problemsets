#!/usr/bin/env python3
import sys
import time

print("This program checks if a number is positive or negative. If positive, it checks if the number is greater or equal to 50. If greater or equal to 50 it checks if it is divisible by 3.")

time.sleep(1) # sleep for 2 seconds

a = int(sys.argv[1]) # get integer input from user
 
# generate empty messages
message = ""
message50 = ""
message_even = ""
message3 = ""

# test integer
# test if positive or negative
if a > 0:
	message = "it is a positive number"
	# if positive, check if less than or greater than 50
	if a < 50:
		message50 = "that is less than 50"
		# if less than 50, check if even or odd
		if a%2 == 0:
			message_even = "and is even"
			print(message, message50, message_even)
		else:
			message_even = "and is odd"
			print(message, message50, message_even)
	elif a > 50:
		message50 = "that is greater than 50"
		# if greater than 50, check if divisible by 3
		if a%3 == 0:
			message3 = "and divisible by 3"
			print(message, message50, message3)
		else:
			print(message, message50)
	else:
		message50 = "that is equal to 50"
		print(message, message50)
elif a < 0:
	message = "negative"
	print(message)
else:
	message = "zero"
	print(message)


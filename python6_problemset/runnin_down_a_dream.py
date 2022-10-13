#!/usr/bin/env python3

# Open Python_06.txt
# Uppercase each line
# Print each line to the STDOUT

with open("Python_06.txt", "r") as file_object, open("Python_06_uc.txt", "w") as file_object_output:

	for line in file_object:
		line = line.rstrip()
		line = line.lower() + "\n"
		file_object_output.write(line)


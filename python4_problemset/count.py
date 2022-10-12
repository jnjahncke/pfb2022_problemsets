#!/usr/bin/env python3

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

# Print every number from a to b, including b
for x in range(a, b+1):
	print(x)

print('\n\n')
# Same as above, but only print if the number is odd
for x in range(a, b+1):
	if x%2 != 0:
		print(x)


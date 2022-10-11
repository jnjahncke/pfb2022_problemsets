#!/usr/bin/env python3
import sys

a = sys.argv[1]

try:
	if type(int(a)) == int:
		b = int(a)
	else:
		b = a
except:
	try:
		if type(str(a)) == str:
			b = str(a)
		else:
			b = a
	except:
		try:
			if type(bool(a)) == bool:
				b = bool(a)
			else:
				b = a
		except:
			b = a

if bool(b) == True:
	print(b, "is True")
else:
	print(b, "is not True")

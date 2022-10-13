#!/usr/bin/env python3

A = {3, 14, 15, 9, 26, 5, 35, 9}
B = {60, 22, 14, 0 , 9}
print(f'Set A: {A}')
print(f'Set B: {B}')


# Find the intersection
print(f'Intersection: {A & B}')

# Find the difference
print(f'Difference (A only): {A - B}')
print(f'Difference (B only): {B - A}')

# Find the union
print(f'Union: {A|B}')

# Find the symetrical difference
print(f'Symmetrical Difference: {A^B}')

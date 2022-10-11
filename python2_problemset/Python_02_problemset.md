Python 2 Problem Set -- Operators, Truth, Logic
===================

### Part 1: Use Interpreter

A. Use the Interactive Interpretor to test to see if you can find an ['ATG' in](https://github.com/prog4biol/pfb2022#membership-operators) the following DNA string:

```
GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA
```

B. How about 'TTT'?

C. If you didn't already save the DNA string to a variable, do that now and redo [1 and 2](https://github.com/prog4biol/pfb2022#membership-operators).

D. In the interpretor use `bool` to test a variety of values like '', 0, 0.0, FALSE, false, True, true, 'True', 'False' to see if they evalue to True or False.

E. Quit Interpreter

### Part 2: Use Text Editor

1. Using a text editor, write a script that 
    - Assigns a value to a variable
    - Has a [if/else statment](https://github.com/prog4biol/pfb2022#logic-control-statements) in which:
       - It prints out a confirmation of truth if the value is true
       - It prints out "Not True" if the value is not true. 

2. Make sure to commit your changes along the way. You can wait until the end to push them to your remote repo, if you like, or you can do it now. 



3. Create a script that has a [if/else statement](https://github.com/prog4biol/pfb2022#if-statement) that (remember to write a little bit at a time and test it)
    - Test to see if a number is positive or negative
    - print "positive" if it is positive
    - print "negative" if it is negative
    - save it and run it.
4. Add an [elif](https://github.com/prog4biol/pfb2022#ifelif) to test if the number is equal to 0. Save it and run it.

5. Add nested tests to your last script
    - if it is positive, in addition to printing "positive"
    - test if it is smaller than 50
    - save it and run it    
            
6. Add more nested tests to your script.
    - if it is smaller than 50
    - test if the number is even
    - if it is smaller than 50 and even, print "it is an even number that is smaller than 50"
    - save it and run it
         
7. Add more nested tests.  
    -  if it is larger than 50,  
    -  test if the number is divisible by 3  
    -  if the number is larger than 50 and divisible by 3, print "it is larger than 50 and divisible by 3"  
    -  save it and run it

8. In your previous nested loops, test the number 50. What prints to the screen? Is it the correct response? If not, you have a semantic error and need to alter your code to be correct with any number.  

9. Write a new script that does all the testing in 7-11, but gets the value being tested from the command line and stores it in a variable. Add in a print statement that reminds the user what number is being tested. [Remember `sys` in the notes](pfb2022#command-line-parameters-a-special-built-in-list). 

10. ADD/COMMIT/PUSH

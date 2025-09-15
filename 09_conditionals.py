"""
Conditionals
By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:

Conditional execution: a block of one or more statements will be executed if a certain expression is true
Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.
If Condition
In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.
"""

# syntax
#if condition:
#    this part of code runs for truthy conditions
#Example: 1

a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
#As you can see in the example above, 3 is greater than 0. The condition was true and the block code was executed. However, if the condition is false, we do not see the result. In order to see the result of the falsy condition, we should have another block, which is going to be else.

#If Else
#If condition is true the first block will be executed, if not the else condition will run.

# syntax
#if condition:
#    this part of code runs for truthy conditions
#else:
#     this part of code runs for false conditions
#Example:

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

    a = 3
print('a is positive') if a > 0 else print('a is negative') # first condition met, 'A is positive' will be printed
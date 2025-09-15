"""
Exception Handling
Python uses try and except to handle errors gracefully. A graceful exit (or graceful handling) of errors is a simple programming idiom - a program detects a serious error condition and "exits gracefully", in a controlled manner as a result. Often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this makes our application more robust. The cause of an exception is often external to the program itself. An example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device. Graceful handling of errors prevents our applications from crashing.

We have covered the different Python error types in the previous section. If we use try and except in our program, then it will not raise errors in those blocks.

Try and Except

try:
    code in this block if things go well
except:
    code in this block run if things go wrong
"""
#Example:

try:
    print(10 + '5')
except:
    print('Something went wrong')

#In the example above the second operand is a string. 
# We could change it to float or int to add it with the number to make it work. 
# But without any changes, the second block, except, will be executed.

#Example:

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')

#Something went wrong
#In the above example, the exception block will run and we do not know exactly the problem. 
# To analyze the problem, we can use the different error types with except.

#In the following example, it will handle the error and will also tell us the kind of error raised.

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

"""Enter your name:Asabeneh
Year you born:1920
Type error occured
In the code above the output is going to be TypeError. Now, let's add an additional block:
"""
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
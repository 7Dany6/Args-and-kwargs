"""
Functions have a flexible syntax in Python.
We will find out what allows functions to accept a varying number of arguments and how to unpack iterable objects when calling a function.

The structure of a function:
def func(positional_args, defaults, *args):
    pass
So, even at first glance there is nothing intricate. Let's see some bright examples of applying args.
"""

#TASK1
"""
Declare a function sq_sum() that calculates the squares for arguments passed into it and returns their sum.

print(sq_sum(1, 2, 2, 4))  # 25.0
print(sq_sum(1.5))         # 2.25
print(sq_sum(1, 10, 10))   # 201.0
Your function is not supposed to print anything, just return the calculated sum.
"""
#SOLUTION
def sq_sum(*args):
    return sum([number**2 for number in args])

#TASK2
"""
Imagine that you were instructed to write a congratulatory letter, mentioning all the employees of the IT department in it. 
You know for sure that the department has one tester, one project manager, but you don't know exactly how many developers are there.

Define a function congratulations() that lists the names of everyone in the letter.
If the project manager is Alice, the tester is Mike, and the developers are Roman and Victoria, then the printed congratulation should look like this:

Happy New Year! Take care of yourself and your loved ones!
For:
Alice
Mike
Roman
Victoria
Pay attention to the order of names. First mention a project manager, then a tester, and then developers. 
Each name should be on a separate line!

Note that you do not need to call a function, just implement it.

You don't need to work with the input: the names of the employees are meant to be passed to the function as arguments.
"""
#SOLUTION
def congratulations(project_manager, tester, *developers):
    print("Happy New Year! Take care of yourself and your loved ones!", 'For:', project_manager, tester, sep='\n')
    for developer in developers:
        print(developer)

#TASK3
"""
Imagine that you are a teacher whose students recently wrote a test. 
However, you do not know exactly how many students were in the class at the time of writing. 
Based on the marks you have, you should calculate the average mark for this test.

Define the average_mark() function that returns the average value. 
The function should take a varying number of integers as positional arguments.

Round the result to one decimal place.

You are not supposed to call the function, just implement it.
"""
#SOLUTION
def average_mark(*args):
    return round(sum(args) / len(args), 1)

#TASK4
"""
Jackie earned €1,000, and now he wants to put these savings in the bank for several months. 
However, he has not yet decided on the exact term for the contribution.

Suppose that the bank that Jackie chose has offers for different amounts of time. 
The interest rates also change from month to month. 
So, let's say he decides to put money for three months, and the bank sets interest rates of 5%, 7% and 4%. 
The actual algorithm will be as follows:

Amount after the first month: €1,000 * 1.05 = €1,050
Amount after the second month: €1,050 * 1.07 = €1,123.5
Amount after the third month: €1,123.5 * 1.04 = €1,168.44

Thus, the final amount will be equal to €1,168.44. Round the value to two decimal places!

Your task is to correct the errors in the definition of the final_deposit_amount() function and implement it. 
The function should calculate and return the amount of money that Jackie will receive at the end. 
Note that we use interest rates as positional arguments to the function. 
We also have a keyword-only argument amount. 
You do not need to call a function, just implement it.
"""
#SOLUTION
def final_deposit_amount(*interest, amount=1000):
    for percent in interest:
        amount *= percent / 100 + 1
    return round(amount, 2)

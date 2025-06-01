In Python, control flow dictates the order in which statements are executed. It is managed through conditional statements, loops, and function calls.
Conditional Statements
if statement: Executes a block of code if a condition is true.
Python

    x = 10
    if x > 0:
        print("x is positive")
elif statement: Checks an additional condition if the preceding if condition is false.
Python

    x = -5
    if x > 0:
        print("x is positive")
    elif x < 0:
        print("x is negative")
else statement: Executes a block of code if all preceding if and elif conditions are false.
Python

    x = 0
    if x > 0:
        print("x is positive")
    elif x < 0:
        print("x is negative")
    else:
        print("x is zero")
Loops
for loop: Iterates over a sequence (list, tuple, string, range).
Python

    for i in range(5):
        print(i)
This prints numbers from 0 to 4.
while loop: Repeats a block of code as long as a condition is true.
Python

    count = 0
    while count < 5:
        print(count)
        count += 1
This also prints numbers from 0 to 4.
Loop Control Statements
break: Terminates the loop prematurely.
Python

    for i in range(10):
        if i == 5:
            break
        print(i)
This prints numbers from 0 to 4 and then exits the loop.
continue: Skips the current iteration and proceeds to the next.
Python

    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)
This prints only the odd numbers from 1 to 9.
pass: Does nothing. It is often used as a placeholder.
Python

    for i in range(5):
        if i == 2:
            pass
        else:
            print(i)
This prints numbers 0, 1, 3, and 4, skipping 2 without any action.
Additional Notes
Loops can be nested within each other.
The range() function generates a sequence of numbers.
Control flow is essential for creating dynamic and flexible programs.

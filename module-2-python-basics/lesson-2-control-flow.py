"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [Alonzo, Joab P.]
Date: [September 25, 2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[Control flow is used to tell a program what to do depending on the situation.
In our everyday life, we always make a decision.

For example: 
If i got home early. I will play basketball.
If i got home late. I will take a rest.

Python can also make a decision by using if, elif, and else.
The "If" statement checks the condition, if the condition is true,
python will run the code in side the if statement.

The "elif" statement means "else if".
It is used when we want to check another condition.

The "else" statement is used when none of the previous conditions are true.

This conditional statement allows the program to make a decision instead of doing 
it again and again.]


============================================
KEY VOCABULARY
============================================
- condition: This is a situation that python checks to see if it is true or false.
- if / elif / else: If used to check the first condition.
elif means else if it checks another condition when the previous condition is false.
- comparison operator: A symbol used to compare two values.
- boolean expression: An expression that result is either true or false.
- >:
  Greater than.
- <:
  Less than.
- ==:
  Equal to.
- >=:
  Greater than or equal to.
- <=:
  Less than or equal to.
- !=:
  Not equal to.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
#My example is simple program based on what i would do when i get home. I used this simple example for us to understand it easily.

time = "early"

if time == "early":
    print("I will play basketball.")
elif time == "late":
    print("I will take a rest.")
else:
    print("I will decide what to do.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[One mistake i want to avoid is getting confused in = and ==.
i use = when i want to store value in a variable, while == is use to 
check if the two values are equal.
For example:

arrival = "early" stores "early" in the variable.

arrival == "early" checks if the value is "early".

I also need to always remember that putting a colon after if, elif, and else is important.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""

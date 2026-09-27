"""
Module 2 — Lesson 4: Functions
Student: [Alonzo, Joab P.]
Date: [September 27, 2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[A function is a group of code that does a specific job. We make a function when we want to use the same code more than once.

Instead of writing the same code again and again, we can put it inside a function and we can call it if we need it. ]


============================================
KEY VOCABULARY
============================================
- Function: Code that has a specific job.
- Parameter: A value that a function can receive.
- Argument: The value that we give to parameter.
- Return: Send a the result back
- Call: Using or running a function.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yzourself — not copied from class.
"""

# --- your code example goes here ---
"""
============================================
MY OWN EXAMPLE(S)
============================================
"""

def check_attendance(status):
    if status == "present":
        return "Student is present."
    else:
        return "Student is absent."


result = check_attendance("present")

print(result)



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[One mistake that i want to avoid is forgetting to give a value when calling the function, The function needs a status,
"present", to give the correct result.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""

# Here is the organized version of your original text, formatted clearly for easy reading and copying:
#
# ---
#
# ### **Create Your Own Python Decorator**
#
# #### **Objective**
#
# Create your own decorator function to measure the amount of seconds that a function takes to execute.
#
# #### **Expected Output**
#
# * `1695050908.1985211`
# * `fast_function run speed: 0.33974480628967285s`
# * `slow_function run speed: 2.9590742588043213s`
#
# ---
#
# ### **Calculating Time**
#
# * The `time.time()` function will return the current time in seconds since January 1, 1970, 00:00:00.
# * Try running the starting code to see the current time printed. If you run the code after a while, you'll see a new time printed.
#
# **Example:**
#
# * **First run:** `1598524371.736911`
# * **Second run:** `1598524436.357875`
# * **Time difference:** `Second run - First run = 64.62096405029297` (approx. 1 minute)
#
# ---
#
# ### **Instructions**
#
# Given the above information, complete the code exercise by printing out the time it takes to run the `fast_function()` vs the `slow_function()`. You will need to complete the `speed_calc_decorator()` function.

import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):
    def decorator_function():
        print(f"{function.__name__} run speed:")

        function()

        print(time.time())

    return decorator_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
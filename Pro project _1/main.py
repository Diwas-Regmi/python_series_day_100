# Coding challenge part 5
# Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.
# Refer next lecture for solution
def divide_two_num(a,b):
    try:
        print(f"{a} / {b} = {a/b}")
    except ZeroDivisionError:
        print("Error : You cannot divide any number by zero try again")


divide_two_num(5,2)

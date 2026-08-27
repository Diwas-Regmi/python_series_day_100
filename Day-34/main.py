# so there are two type hint here one is inside "check("here")"
# another one is after the function made which is "def check(age) "->" which means type hint of the function

def check(age:int)->bool:
    if age > 18:
        can_drive = True

    else:
        can_drive = False

    return can_drive # if i return anything except boolean the compiler warns and underlines the line showing expected boolean but got other datatype instead

if check(19): # if check("nineteen"): the compiler warns and underlines the code showing expected int but got str insted
    print("You can go")
else:
    print("You are under custody")

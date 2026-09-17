# first class-objects, can be passed around as arguments eg int/str/float etc

def multiply(n1,n2):
    return n1*n2
def sum(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2

def calculate(calc_func, n1,n2):
    return calc_func(n1,n2)


result_1 = calculate(sum,6,3)
result_2 = calculate(subtract,6,3)
result_3 = calculate(multiply,6,3)
print(result_1)
print(result_2)
print(result_3)
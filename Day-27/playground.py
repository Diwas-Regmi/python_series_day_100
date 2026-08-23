# def add(*args):
#     total = sum(args)
#
#     print(total)
# add(90,8)
#
def calculate(n, **kwargs):
    return n + kwargs["add"]

print(calculate(4,add = 4))


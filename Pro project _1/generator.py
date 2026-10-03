# def func():
#     counter = 0
#     while counter <=10:
#         yield counter
#         counter +=1
#
# print(list(func()))

def even_generators(x:int):
    for i in range(1,x+1):

        if i % 2 == 0:
            yield i
print(list(even_generators(6)))
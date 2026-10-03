# numbers = [1,2,3,4,5,6,7.8,9]
# def odd(x):
#     if x %2 == 1:
#         return x
#
# odd_num = list(filter(odd,numbers))
# print(odd_num)
# can be done with lambda function as well

numbers = [1,2,3,4,5,6,7.8,9]

odd_num = list(filter(lambda x: x%2 == 1, numbers))
print(odd_num)
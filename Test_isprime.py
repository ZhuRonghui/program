# # 求2到100之间的素数
# from math import sqrt
#
# i, j = 2, 2
# while i <= 100:
#     j = 2
#     while j <= sqrt(i):
#         if i % j == 0:
#             break
#         j += 1
#     else:
#         print(i, end=" ")
#     i += 1

def addMe(x):
    return x ** x


r = lambda x,y:x**2+y
print(r(2,4))
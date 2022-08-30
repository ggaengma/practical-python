# a = 'test'
# b = "test"
# c = '''test
# test'''
# d = '\''
# e = '\"'
# f = '\\'

# a = 'Hello world'
# b = a[0]  # H
# c = a[4]  # o
# d = a[-1]  # d
# e = a[:5]  # Hello
# f = a[6:]  # world
# g = a[3:8]  # lo wor

# s = 'Hello'
# len(s)
#
# a = 'Hello' + 'world'
# b = 'say' + a
# t = 'e' in s
# f = 'x' in s
# g = 'hi' not in s
#
# rep = s * 5


# def sum_count(n):
#     """
#     정수 1 부터 엔까지 합을 반환
#     """
#     total = 0
#     while n > 0:
#         total += n
#         n -= 1
#     return total

# a = sum_count(100)
# print(a)
#
#
#
# import math
#
# x = math.sqrt(10)
#
# import urllib.request
# u = urllib.request.urlopen('https://www.python.org/')
# data = u.read()

# with open('Work/Data/portfolio.csv', 'rt') as f:
#     for line in f:
#         fields = line.split()
#         try:
#             shares = int(fields[1])
#         except ValueError:
#             print("Couldn't parse", line)
#


# raise RuntimeError('Shitttt!!!')

def greeting(name):
    """Issue a greeting"""
    print('Hello', name)


greeting('Joo')
















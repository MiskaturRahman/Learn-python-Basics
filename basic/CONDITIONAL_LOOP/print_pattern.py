#  Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


n = 10
for i in range(0, n):
    for j in range(i):
        print('*', end="")
    print('')

for i in range(10, 0, -1):
    for j in range(i):
        print('*', end="")
    print('')

count = 0
while (count < 3):
    count = count + 1
    print("hello web")
else:
    print('Hello darkweb')

# range
n = 4
for i in range(0, n):
    print(i)

# list iteration
print('list iteration')
l = ['hello', 'misk', 'bd']
for i in l:
    print(i)

# string iteration
print('string iteration')
s = 'MISK'
for i in s:
    print(i)

# dictionary iteration
d = dict()
d['misk'] = 123
d['asshole'] = 456
for i in d:
    print('%s %d' % (i, d[i]))

# tuple iteration
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# iteration by index
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])

# print all letter except 'e', 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('current letter: ', letter)


# break
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
print('current letter: ', letter)


# python code to demonstrate working of enumerate()

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)


# initializing list
questions = ['name', 'color', 'shape']
answers = ['apple', 'red', 'a circle']

for questions, answers in zip(questions, answers):
    print('what is your {0}? I am {1}.'.format(questions, answers))


# python code to demonstrate working of iteritems(),items()

d = {"geeks": "for", "only": "geeks"}
print("The key value pair using iteritems is: ")
for i, j in d.items():
    print(i, j)


# python code to demonstrate working of items()

king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya',
        'Modi': 'The Changer'}
for key, value in king.items():
    print(key, value)

# initializing list
lis = [1, 3, 5, 6, 2, 1, 3]

# reversed list
print('The list in reversed order is: ')
for i in reversed(lis):
    print(i, end=' ')
print('\r')

# using sorted() to print the list in sorted order

print('the list in sorted order is: ')
for i in sorted(lis):
    print(i, end=' ')
print('\r')

# using set(), sorted() to print list
print('the list in sorted list without duplicates: ')
for i in sorted(set(lis)):
    print(i, end=' ')
print('\r')

# initializing list
basket = ['guave', 'orange', 'apple', 'pear',
          'guava', 'banana', 'grape']
for fruit in sorted(set(basket)):
    print(fruit)

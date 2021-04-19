'''prints A 
B B 
C C C 
D D D D 
E E E E E '''

num = 65
n = 5
for i in range(0, 5):
    for j in range(0, i + 1):
        ch = chr(num)

        print(ch, end=' ')

    num += 1
    print('')


'''prints
A 
B C 
D E F 
G H I J 
K L M N O '''

num = 65
n = 5
for i in range(0, 5):
    for j in range(0, i + 1):
        ch = chr(num)

        print(ch, end=' ')

        num += 1
    print('')


'''prints
A
@ ?
> = <
; : 9 8
7 6 5 4 3 '''

num = 65
n = 5
for i in range(0, 5):
    for j in range(0, i + 1):
        ch = chr(num)

        print(ch, end=' ')

        num -= 1
    print('')

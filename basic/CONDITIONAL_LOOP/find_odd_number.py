x = int(input("enter minimum number: "))
y = int(input("enter maximum number: "))

i = x
if i % 2 == 1:
    while i <= y:
        print(i)
        i+=2
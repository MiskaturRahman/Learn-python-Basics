# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6
# Digits 2

string = input("insert a string: ")
digit = letter = 0
for count in string:
    if count.isdigit():
        digit += 1
    elif count.isalpha():
        letter += 1
    else:
        pass

print("letters in string", letter)
print("digit is string", digit)

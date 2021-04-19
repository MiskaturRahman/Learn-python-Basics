# Count the number of even and odd numbers from a series of numbers
# Input
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4
# Number of odd numbers : 5

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

count_odd = 0
count_even = 0

for count in numbers:
    if count % 2:
        count_even += 1
    else:
        count_odd += 1

print("number of even: ", count_even)
print("number of odd: ", count_odd)

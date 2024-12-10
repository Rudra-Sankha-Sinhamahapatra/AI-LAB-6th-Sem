# Program to find the sum of the digits of a number
number = int(input("Enter a number: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10  # Extract the last digit
    sum_of_digits += digit
    number //= 10  # Remove the last digit

print("The sum of the digits is:", sum_of_digits)

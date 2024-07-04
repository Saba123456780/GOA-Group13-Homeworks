"for loop"


# 1) Print all integers from 0 to 20 inclusive.

for i in range(21):
    print(i, end=' ')
print()

# 2) Print the first 10 natural numbers.

for i in range(1, 11):
    print(i, end=' ')
print()

# 3) Print even numbers separately and odd numbers separately from 0 to 100 inclusive.

print("Even numbers:")
for i in range(0, 101, 2):
    print(i, end=' ')
print("Odd numbers:")
for i in range(1, 101, 2):
    print(i, end=' ')
print()

# 4) Enter a number to the user and then using a for loop output the sum of all the numbers up to this number (for example, if he enters 10, output the sum of all the numbers up to 10, for example).

num = int(input("Enter a number: "))
sum_numbers = 0
for i in range(1, num + 1):
    sum_numbers += i
print("Sum of numbers up to  is: ", sum_numbers)

# 5) Write an algorithm that prints multiples of 5 (numbers divisible by 5) from 1 to 50 inclusive

print("Multiples of 5 from 1 to 50:")
for i in range(1, 51):
    if i % 5 == 0:
        print(i, end=' ')
print()

"while loop"

# 1) Print even numbers up to 20.

print("Even numbers up to 20:")
num = 0
while num <= 20:
    if num % 2 == 0:
        print(num, end=' ')
    num += 1
print()


# 2) calculate the sum of numbers from 1 to 10.

total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"Sum of numbers from 1 to 10 is: {total}")


# 3) Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct number is 7.

guess = 0
while guess != 7:
    guess = int(input("Guess the number between 1 and 10: "))
print("You guessed it right! The number is 7.")

# 4) Write a while loop that processes a list of numbers, doubling each number, and prints the new list.

numbers = [3, 8, 15, 20]
index = 0
while index < len(numbers):
    numbers[index] *= 2
    index += 1
print("Doubled list:", numbers)

# 5) Write a while loop that repeatedly asks the user to enter a password until the correct password "password123" is entered.

password = ""
while password != "password123":
    password = input("Enter the password: ")
print("Correct password entered!")


"if else"

# 1) Write an if-else statement that prints "Good morning!" if the current hour is less than 12 and "Good afternoon!" otherwise.

import datetime
current_hour = datetime.datetime.now().hour
if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")

# 2) Write an if-else statement that checks if a number is even or odd. If the number is even, print "Even"; otherwise, print "Odd."

num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3) Create an if-else statement to check if the temperature is above 30 degrees. If it is, print "It's hot outside!"; otherwise, print "It's not too hot."

num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4) Create an if-else statement that determines if a person is a teenager. If the age is between 13 and 19 (inclusive), print "You are a teenager!"; otherwise, print "You are not a teenager."

temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")



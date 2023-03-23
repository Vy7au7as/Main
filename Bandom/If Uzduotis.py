import math

def f(x, case):
    if case == 1:
        if -3 <= x <= 0:
            return math.exp(-x)
        elif 0 < x <= 1:
            return 5*x - 7
        else:
            return math.sqrt(x+1)
    elif case == 2:
        if -4 <= x <= 0:
            return math.cos(x)
        elif 0 <= x <= 4:
            return 1/(x+5)**3
        else:
            return math.sqrt(x**2 - 25)
    elif case == 3:
        if -5 <= x <= 0:
            return x + 2*x**2
        elif 0 < x < 3:
            return x*1 + 4
        else:
            return math.sqrt(2*x**2 - 35)
    elif case == 4:
        if -1 <= x <= 0:
            return math.cos(x**2)
        elif 0 < x < 1:
            return 4*x**2 + 3
        else:
            return math.sqrt(x**2 - x - 4)
    elif case == 5:
        if -2 <= x <= 0:
            return 3.2*x**2
        elif 0 <= x <= 1:
            return math.sin(x+1)**2
        else:
            return 2/(3*x**2 - 1)
    elif case == 6:
        if -3 <= x <= 0:
            return 1/(x-5)
        elif 0 < x <= 5:
            return (x+3)**2
        else:
            return math.sqrt(x+5)
    elif case == 7:
        if -5 <= x <= 0:
            return 1/x**2
        elif 0 <= x <= 2:
            return math.sin(x+1)
        else:
            return math.sqrt(2*x-8)

print(f(-2, 5))   # Output: 12.8

print('=========Patobulinti 4 užduotį----------')

# import random
# import sys
#
# Prompt the user to input a number
# user_num = int(input("Enter a number from -10 to 10: "))
#
# Check if the input number is within the range of -10 to 10
# if user_num < -10 or user_num > 10:
#     print("Error: Input number is not within the range of -10 to 10.")
#     sys.exit()
#
# Generate a random number between -10 and 10
# random_num = random.randint(-10, 10)
#
# Compare the two numbers
# if user_num > random_num:
#     result = user_num - random_num
#     print(f"The user's number {user_num} is larger than the random number {random_num}.")
#     print(f"Result: {result}")
# elif user_num < random_num:
#     result = user_num + random_num
#     print(f"The random number {random_num} is larger than the user's number {user_num}.")
#     print(f"Result: {result}")
# else:
#     print(f"The user's number {user_num} is equal to the random number {random_num}.")
print('===========Šaknies traukimas kol skaičius pozityvus====')
# import math
#
# while True:
#     num = int(input("Please enter a positive number: "))
#     if num < 0:
#         print("Negative number entered. Exiting program.")
#         break
#     root = math.sqrt(num)
#     print("The square root of", num, "is", root)
#print("Game over.")
print('=================')
import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < number:
        print("The number is higher. Try again.")
    else:
        print("The number is lower. Try again.")


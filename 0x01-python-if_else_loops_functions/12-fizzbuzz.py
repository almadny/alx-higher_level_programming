#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            if i == 100:
                print("FizzBuzz")
            else:
                print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            if i == 100:
                print("Fizz")
            else:
                print("Fizz", end=' ')
        elif i % 5 == 0:
            if i == 100:
                print("Buzz")
            else:
                print("Buzz", end=' ')
        else
            if i == 100:
                print(i)
            else:
                print(i, end=' ')

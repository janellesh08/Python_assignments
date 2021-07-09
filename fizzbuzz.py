n1= int(input("Is your number Fizz, Buzz, or FizzBuzz? Enter it here!"))


def fizz_buzz(n1):
    if n1 % 3 == 0:
        print("Fizz")
    elif n1 % 5 == 0:
        print("Buzz")
    elif n1 % 3 == 0 and n1 % 5 == 0:
        print("FizzBuzz")

fizz_buzz(n1)

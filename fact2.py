num = int(input("Enter a number to get the factorial: "))


def fact(num):
    answer = 1
    for i in range(1, num + 1):
        answer = answer * i
    print(f"The factorial for this number is {answer}")

fact(num)
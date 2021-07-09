n1 = int(input("What's your first number?"))
o1 = input("Should I add, subtract, mulitply or divde? Enter your operation (+, -, *, /)")
n2 = int(input("What's your second number?"))


def calculate(n1, o1, n2):
    if o1 == "+":
        result = n1 + n2
    elif o1 =="-":
        result = n1 - n2
    elif o1 =="*":
        result = n1 * n2
    elif o1 =="/":
        result = n1/n2
    print(result)


calculate(n1, o1, n2)



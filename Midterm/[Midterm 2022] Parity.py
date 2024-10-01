"""[Midterm 2022] Parity"""
def main():
    """Start"""
    num1 = str(input())
    text = str(input())
    num2 = 0
    for i in num1:
        if i == "1":
            num2 += 1
    if num2 % 2 == 0 and text == "Even":
        print(num1+"0")
    elif num2 % 2 != 0 and text == "Even":
        print(num1+"1")
    elif num2 == 0 and text == "Even":
        print(num1+"0")
    elif num2 % 2 == 0 and text == "Odd":
        print(num1+"1")
    elif num2 % 2 != 0 and text == "Odd":
        print(num1+"0")
    elif num2 == 0 and text == "Odd":
        print(num1+"1")

main()

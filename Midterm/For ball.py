"""Forge Ball"""
def main():
    """Start"""
    text = str(input())
    num1 = 1
    for i in text:
        if i == "A" and num1 == 1:
            num1 = 2
        elif i == "A" and num1 == 2:
            num1 = 1
        elif i == "B" and num1 == 2:
            num1 = 3
        elif i == "B" and num1 == 3:
            num1 = 2
        elif i == "C" and num1 == 1:
            num1 = 3
        elif i == "C" and num1 == 3:
            num1 = 1
    print(num1)

main()

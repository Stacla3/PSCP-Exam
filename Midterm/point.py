"""Point"""
def main():
    """Start"""
    num1 = float(input())
    num2 = num1%4
    if num2 == 0:
        print(1)
    elif num2 == 1:
        print(7)
    elif num2 == 2:
        print(9)
    elif num2 == 3:
        print(3)

main()

"""Tuple's Sad life"""
def main():
    """Start"""
    num1 = str(input())
    num2 = num1.split()
    num3 = tuple(num2)
    num4 = str(input())
    num5 = num3.index(num4)
    num6 = num3.count(num4)
    for _ in range(num6):
        for _ in range(num6):
            print(num5, end= " ")
        print()

main()

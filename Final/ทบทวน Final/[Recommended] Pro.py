"""[Recommended] Pro"""
def main():
    """Start"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    if num4 < num1:
        print(num4*num3)
    elif num4 % num1 == 0:
        print((((num4//num1)*num2)*num3))
    elif num4 % num1 != 0:
        print((((num4//num1)*num2)*num3)+((num4-((num4//num1)*num1))*num3))
main()

"""Triangle I"""


def main():
    """Start"""
    num1_ = float(input())
    num2_ = float(input())
    num3_ = float(input())
    lily = (num1_**2) + (num2_**2)
    tulip = (num1_**2) + (num3_**2)
    rose = (num3_**2) + (num2_**2)
    if num3_ > num2_ and num3_ > num1_:
        if lily == (num3_**2) or (lily >= (num3_**2)-0.01 and lily <= (num3_**2)+0.01):
            print("Yes")
        else:
            print("No")
    elif num2_ > num3_ and num2_ > num1_:
        if tulip == (num2_**2) or (tulip >= (num2_**2)-0.01 and tulip <= (num2_**2)+0.01):
            print("Yes")
        else:
            print("No")
    elif num1_ > num3_ and num1_ > num2_:
        if rose == (num1_**2) or (rose >= (num1_**2)-0.01 and rose <= (num1_**2)+0.01):
            print("Yes")
        else:
            print("No")
    else:
        print("No")


main()

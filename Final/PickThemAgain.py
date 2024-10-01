"""PickThemAgain"""
def main():
    """Start"""
    num1 = str(input())
    num2 = num1.split(" ")
    num3 = []
    for i in num2:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            num3.append(i)
    if len(num3) == 0:
        print("Nope")
    else:
        num3.reverse()
        for i in num3:
            print(i)

main()

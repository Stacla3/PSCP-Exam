"""PickThemAgain"""
def main():
    """Start"""
    num1 = str(input())
    num2 = num1.split(" ")
    num3 = []
    num4 = []
    for i in num2:
        inttt = int(i)
        if inttt % 3 == 0:
            num3.append(inttt)
        elif inttt % 5 == 0:
            num3.append(inttt)
    num3.reverse()
    for j in num3:
        if j == float:
            num4.append(j)
            if len(num4) == len(num3):
                print("Nope")
            else:
                print(j)
        else:
            print(j)

main()

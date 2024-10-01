"""[Recommended] ScaledMatrix"""
def main():
    """Start"""
    num1 = int(input())
    num2 = int(input())
    list1 = []
    list2 = []
    num4 = 0
    for i in range(num1*num2):
        num3 = float(input())
        list1.append(num3)
    maxx = max(list1)
    minn = min(list1)
    for i in list1:
        result = (i-minn)/(maxx-minn)
        list2.append(result)
    for i in list2:
        num4 += 1
        if num4 % num2 == 0:
            print("%.2f" %round(i, 2))
        else:
            print("%.2f" %round(i, 2), end=" ")
main()

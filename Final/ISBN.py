"""ISBN"""
def main():
    """Start"""
    text = str(input())
    neww = text.replace("-", "")
    num1 = 11
    list1 = []
    for i in neww[:-1]:
        num1 -= 1
        num3 = num1*int(i)
        list1.append(num3)
    result = ((-1)*sum(list1)) % 11
    if text[-1] == "X" and result == 10:
        print("Yes")
    elif result == int(text[-1]):
        print("Yes")
    else:
        if result == 10:
            print("No", "X")
        else:
            print("No", result)
main()

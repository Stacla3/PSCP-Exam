"""[Recommended] Tax"""
def main():
    """Start"""
    num1 = int(input())
    num2 = int(input())
    result = 0
    dict1 = {6 : 0.9, 7 : 0.8, 8 : 0.7, 9 : 0.6}
    if num2 == 0:
        print("%.2f" %0)
    else:
        if num2 >= 1 and num2 <= 600:
            result = num2*0.5
        elif num2 >= 601 and num2 <= 1800:
            result = 300 + ((num2-600)*1.5)
        elif num2 > 1800:
            result = 300 + 1800 + ((num2-1800)*4)
        if num1 < 6:
            neww = result
            print("%.2f" %neww)
        elif num1 >= 6 and num1 <= 9:
            neww = result*dict1[num1]
            print("%.2f" %neww)
        elif num1 >= 10:
            neww = result*0.5
            print("%.2f" %neww)
main()

"""[Midterm 2021 + Recommend] Century"""
def main():
    """Start"""
    import math
    num1 = int(input())
    for _ in range(num1):
        text = str(input())
        if "B.E." in text:
            text = text.replace("B.E. ", "")
            num3 = int(text)
            num3 = num3 - 543
            if num3 % 100 == 0 and num3 > 0:
                print("%.0f" %(num3/100))
            elif num3 % 100 != 0 and num3 > 0:
                print(math.ceil(num3/100))
            elif num3 == 0:
                print("1")
            elif num3 < 0:
                print("ERROR")
        elif "A.D." in text:
            text = text.replace("A.D. ", "")
            num3 = int(text)
            if num3 % 100 == 0 and num3 > 0:
                print("%.0f" %(num3/100))
            elif num3 % 100 != 0 and num3 > 0:
                print(math.ceil(num3/100))

main()

"""[Midterm 2022 + Recommend] Coke"""
def main():
    """Start"""
    price = int(input())
    fabottle = int(input())
    newbottle = int(input())
    want = int(input())
    num1 = 0
    num2 = 0
    num3 = want
    result1 = price*want
    if fabottle == 0:
        print(result1)
    else:
        while True:
            if fabottle > 0:
                neww = want / fabottle
                num1 += 1
                num2 += newbottle
                if want < fabottle:
                    break
        print(neww)

main()

"""ScaledMatrix"""
def main():
    """Start"""
    num1, num2 = int(input()), int(input())
    list1, list2, list3 = [], [], []
    num3 = 0
    for _ in range(num1*num2):
        number = float(input())
        list1.append(number)
    minn, maxx = min(list1), max(list1)
    for i in list1:   #แปลงเป็นค่าScale0-1
        num3 += 1
        result = "%.2f" %(round((i-minn)/(maxx-minn), 2))
        list2.append(result)
        if num3 == num2:
            list3.append(list2)
            num3 = -1
            num3 += 1
            list2 = []
    for i in list3:
        print(str(i).strip("[]").replace(",", "").replace("'", ""))
main()

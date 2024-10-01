"""Seeker"""
def main():
    """Start"""
    text = str(input())
    strr = ""
    list1 = []
    num1 = 0
    for i in text:
        if not i.isnumeric():
            i = ","
        strr += i
    neww = strr.split(",")
    for i in neww:
        if i.isnumeric():
            list1.append(i)
    for i in list1:
        num1 += int(i)
    print(num1)
main()

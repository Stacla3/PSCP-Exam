"""[Recommended] Helloooo"""
def main():
    """Start"""
    text = str(input())
    list1 = []
    list2 = []
    list3 = []
    neww = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    num1 = 0
    num2 = 0
    strr = ""
    for i in text:
        list1.append(i)
    list1.reverse()
    for i in list1:
        num1 += 1
        if i in neww:
            list3.append(num1)
            break
    if len(list3) > 0:
        for i in list1:
            num2 += 1
            if num2 == list3[0]:
                i *= 4
            list2.append(i)
        list2.reverse()
        for i in list2:
            strr += i
        print(strr)
    else:
        print(text)
main()

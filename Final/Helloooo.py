"""Helloooo"""
def main():
    """Start"""
    text = str(input())
    num1 = -1
    num2 = -1
    list1 = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    list2 = []
    strr = ""
    for i in text:
        num1 += 1
        if i in list1:
            list2.append(num1)
    if len(list2) == 0:
        print(text)
    else:
        for i in text:
            num2 += 1
            if num2 == list2[-1]:
                i *= 4
            strr += i
        print(strr)
main()

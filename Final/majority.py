"""majority"""
def main():
    """Start"""
    num1, num2 = int(input()), int(input())
    set1 = set()
    list1, list2, list3 = [], [], []
    for _ in range(num2):
        num3 = str(input())
        list1.append(num3)
    for i in list1:
        set1.add((i, list1.count(i)))
    for i in set1:
        if i[-1] >= (num2/2):
            list2.append((i[0], i[-1]))
        else:
            list3.append((i[0], i[-1]))
    sortt = sorted(list2, key=lambda x: x[-1])
    sortt2 = sorted(list3, key=lambda x: x[-1])
    if len(sortt) >= 1:
        for i in sortt:
            i = i
        print(i[0], i[1])
    else:
        num1 = ""
        print(0, sortt2[-1][-1], num1)
main()

"""Discount"""
def main():
    """Start"""
    list1 = []
    while True:
        price = str(input())
        if price == "ENTER":
            break
        if price.isnumeric():
            list1.append(int(price))
    if len(sorted(list1)) <= 5:   #หาผลรวมระคาหนังสือตามตาราง
        print(sum(sorted(list1)))
    elif len(sorted(list1)) >= 6 and len(sorted(list1)) < 12:
        print(sum(sorted(list1)[1:]))
    elif len(sorted(list1)) >= 12 and len(sorted(list1)) < 20:
        print(sum(sorted(list1)[2:]))
    elif len(sorted(list1)) >= 20 and len(sorted(list1)) < 25:
        print(sum(sorted(list1)[4:]))
    else:
        print(sum(sorted(list1)[len(list1)//5:]))
main()

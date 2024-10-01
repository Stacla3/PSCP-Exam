"""Scout"""
def main():
    """Start"""
    num1 = int(input())
    num2 = 0
    num3 = 0
    list1 = []
    for _ in range(num1):
        text = str(input()).split()
        amount = str(input()).split()
        for i in sorted(amount):
            num2 += int(i)
            num3 += 1
            if num2 <= int(text[-1]) and num3 <= int(text[1]):
                list1.append(num3)
        print(list1[-1])
        list1 = []
        num3 = 0
        num2 = 0

main()

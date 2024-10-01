"""Olympic"""
def calcu(x):
    return x[1], x[2]
def main():
    """Start"""
    num1 = int(input())
    list1 = []
    num2 = 0
    num4 = 0
    num5 = 0
    for _ in range(num1):
        text = str(input())
        neww = text.find(" ")
        result = text[neww+1:].split()
        for i in result:
            num2 += int(i)
        list1.append((text[:neww], list(result), num2))
        num2 = 0
    sortt = sorted(list1, key=lambda x: (x[0]))
    sortt1 = sorted(sortt, key=calcu, reverse=True)
    for i in range(len(sortt1)):
        num5 += 1
        num4 += 1
        if sortt1[i-1][1] == sortt1[i][1]:
            num4 -= 1
        elif num5 != num4:
            num4 = num5
        if num4 == 0:
            num4 = 1
        print(num4, sortt1[i][0], sortt1[i][1][0], sortt1[i][1][1], sortt1[i][1][2], sortt1[i][2])
    list1 = []
main()

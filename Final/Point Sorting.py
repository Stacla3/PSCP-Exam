"""Point Sorting"""
def cal(num):
    """calculate"""
    result = int(num[0]) + int(num[1])   #เรียงตัวตามลำดับ
    return result, -int(num[-1])
def main():
    """output"""
    list1 = []
    num1 = int(input())
    for _ in range(num1):
        num2 = int(input())
        for _ in range(num2):
            text = str(input()).split()
            list1.append(text)
        sortt = sorted(list1, key=cal)
        for i in sortt:
            print(i[0], i[1])
        list1 = []
main()

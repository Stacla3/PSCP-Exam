"""MultiplyMatrixPQR"""
def main():
    """Start"""
    nump, numq, numr, num3, num4 = int(input()), int(input()), int(input()), 0, 0
    list1, list2, list3, list4, list5, list6 = [], [], [], [], [], []
    for _ in range(nump):
        for _ in range(numq):
            list1.append(int(input()))
        list2.append(list1)
        list1 = []
    for _ in range(numq):
        for _ in range(numr):
            list3.append(int(input()))
        list4.append(list3)
        list3 = []
    for i in range(nump):   #แถวคูณกับหลักตามสูตรการคูณ Matrix เช่น -5*4, -5*1
        for j in range(numr):
            for k in range(numq):
                list5.append(list2[i][k]*list4[k][j])
    for i in list5:
        num3 += 1
        num4 += i
        if num3 == numq:
            list6.append(num4)
            num3 = -1
            num3 += 1
            num4 = 0
    for i in list6:
        num3 += 1
        if num3 % numr == 0:
            print(i)
        else:
            print(i, end=" ")
main()

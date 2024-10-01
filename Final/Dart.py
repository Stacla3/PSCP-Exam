"""Dart"""
def main():
    """Start"""
    import math
    num1 = int(input())
    list1 = []
    count1 = 0
    for i in range(num1):
        text = str(input()).split()
        list1.append(text)
    for i in range(len(list1)):   #หาว่าระยะห่างจากจุด2จุดเพื่อหาคะแนน
        result = math.sqrt(((int(list1[i][0])-0)**2)+((int(list1[i][1])-0)**2))
        if result <= 2:
            count1 += 5
        elif result > 2 and result <= 4:
            count1 += 4
        elif result > 4 and result <= 6:
            count1 += 3
        elif result > 6 and result <= 8:
            count1 += 2
        elif result > 8 and result <= 10:
            count1 += 1
    print(count1)
main()

"""Runner"""
def main():
    """Start"""
    distance = float(input())
    amount = int(input())
    list1, list2, list3, list4, list5 = [], [], [], [], []
    num1 = 0
    for i in range(1, amount+1):
        detail = str(input()).split()
        list1.append(detail)
    for i in range(len(list1)): # คำนวนหาคนใช้เวลาน้อยสุด
        num1 += 1
        result = num1, list1[i][0], ((distance - int(list1[i][-1]))/(int(list1[i][0])))
        neww = ((distance - int(list1[i][-1]))/(int(list1[i][0])))
        list2.append(result)
        list3.append(neww)
    minn = min(list3)
    for i in list2: # หาคนที่ใช้เวลาน้อยสุด
        if minn == i[-1]:
            neww1 = i[0], int(i[1])
            list4.append(neww1)
            list5.append(int(i[1]))
    if len(list4) == 1:
        for i in list4:
            print(i[0])
    else:
        maxx = max(list5) # ถ้าคนที่มีเวลาเท่ากัน : หาคนที่มีความเร็วกว่า
        for i in list4:
            if i[1] == maxx:
                print(i[0])

main()

"""Classify"""
def main():
    """Start"""
    list1, list2, list3, list4 = [], [], [], []
    set1, set2 = set(), set()
    while True: # เก๋บค่ามาเป็น list
        text = str(input())
        if text == "END":
            break
        list1.append(text[0:4])
    for i in sorted(list1): # ลองทำให้เป็นแบบ output
        result = sorted(list1).count(i)
        neww = i[0:2]+" "+i[2:4]+" "+str(result)
        set1.add(neww)
    for i in range(len(sorted(set1))-1): # ใส่ "--" ตรงตัวที่มีเลขข้างหน้าเหมือนกันยกเว้นตัวแรก
        if sorted(set1)[i][0:2] == sorted(set1)[i+1][0:2]:
            list2.append(sorted(set1)[i+1])
            set2.add(sorted(set1)[i+1])
    for i in list2: # นำตัวที่เป็นตัวซ้ำแยกออกมาเป็น set เพื่อให้ง่ายต่อการแปลงค่าและลบค่าเก่า
        result = i[0:2]+"*"+i[2:]
        list3.append(result)
    sortt3 = sorted(set1-set2)
    summ = sorted(sortt3 + list3)
    for i in summ: # แปลงค่าเป็น "--" ตัวที่มี "*" อยู่
        if "*" in i[0:3]:
            i = "--"+i[3:]
        list4.append(i)
    for i in list4: # ลบ 0 ออก
        if i[3] == "0":
            result = i[0:3]+""+i[4:]
            print(result)
        else:
            print(i)

main()

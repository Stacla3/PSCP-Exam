"""SMS"""
def main():
    """Start"""
    pumm = {2 : "ABC", 3 : "DEF", 4 : "GHI", 5 : "JKL",\
             6 : "MNO", 7 : "PQRS", 8 : "TUV", 9 : "WXYZ"}
    num1, list1 = int(input()), []
    neww, count = "", 0
    for _ in range(num1):
        num2 = int(input())
        num3 = int(input())
        if num2 == 1: # ลบคำออกถ้า num2 เป็น 1 ตามจำนวนครั้ง num3
            del list1[-num3:]
        elif num3 <= len(pumm[num2]): # ถ้าจำนวนครั้งที่กดปุ่ม <= len(ตัวอักษรปุ่ม)
            list1.append(pumm[num2][num3-1])
        else:
            for _ in range(num3): # คำนวนหาถ้าจำนวนครั้งที่กดปุ่ม > len(ตัวอักษรปุ่มห)
                count += 1
                if count % (len(pumm[num2])+1) == 0:
                    count = 0
                    count += 1
            list1.append(pumm[num2][count-1])
            count = 0
    if len(list1) == 0: # ไม่มีตัวอักษรที่พิมพ์
        print("null")
    else:
        for i in list1:
            neww += i
        print(neww)

main()

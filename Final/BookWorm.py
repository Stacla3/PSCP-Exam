"""BookWorm"""
def main():
    """Start"""
    amount = abs(int(input()))
    list1, list2 = [], []
    num1, num2 = 0, 0
    for _ in range(amount):
        miniute = abs(float(input()))
        book = int(input())
        for _ in range(book):
            timeread = abs(float(input()))
            list1.append(timeread) # เก็บค่านาทีที่อ่านหนังสือแต่ละเล่ม
        sortt = sorted(list1) # นำมาเรียงจากมากไปน้อยเพื่อคำนวนหาได้ง่าย
        for i in sortt:
            num1 += i
            num2 += 1
            if num1 <= miniute: # ถ้าน้อยกว่าหรือเท่ากับนาทีที่กำหนด เก็บค่าจำนวนครั้งมา
                list2.append(num2)
        print(int(len(list2)))
        list1, list2 = [], []
        num1, num2 = 0, 0

main()

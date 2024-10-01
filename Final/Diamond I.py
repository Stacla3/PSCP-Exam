"""Diamond I"""
def main():
    """Start"""
    deep = int(input())
    wigth = int(input())
    list1, list2, list3 = [], [], []
    for _ in range(deep): # นำค่าของเพชรมาเก็บเป็น list
        num1 = str(input())
        result = num1.split()
        list1.append(result)
    print(list1)
    for i in range(wigth): # เก็บค่า list เฉพาะตัวแนวดิ่ง
        for j in list1:
            list2.append(int(j[i]))
        print(list2)
        result = sum(list2) # หาผลรวมของแนวดิ่งแต่ละ list
        list3.append(result) # เก็บค่า list ใหม่ ที่มีผลรวมของเพชรที่อยู่ในแนวดิ่ง
        list2 = []
    diamond = max(list3) # หาค่ามากสุด
    print(diamond)
main()

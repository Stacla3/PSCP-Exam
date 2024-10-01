"""Cat Parade"""
def main():
    """start"""
    list1 = []
    dict1 = dict()
    while True:
        text = str(input())
        result = text.split(", ")
        list1.extend(result)
        if text == "END":
            break
        if text == "IT'S A DOG": # ถ้ามีหมาให้ลบคำตัวสุดท้ายออก
            del list1[-2:]
    list1.remove("END")
    for i in list1: # หาตำแหน่งของแมวและนับจำนวนแมว
        neww = (list1.index(i)+1)
        result = list1.count(i)
        dict1.update({i : str(neww)+" "+str(result)})
    for i, j in dict(sorted(dict1.items(), key=lambda x: x[0])).items():
        print(i, j)

main()

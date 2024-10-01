"""CUTE CAT FOX"""
def catfox():
    """EIEIEI"""
    num3, dictt, num6, num5 = int(input()), dict(), 0, 0 #ตัวแปล
    for _ in range(num3): # แปลงเป็น Dict
        num1 = str(input()).strip("{}").split(" : ")
        result, result1 = num1[0].strip('"'), num1[1].strip('"')
        neww = {result : result1}
        dictt.update(neww)
    if "Fubuki" not in dictt.keys() and "Fox01" not in dictt.values():
        dictt.update({'Fubuki' : 'Fox01'})
    if "Garfield" not in dictt.keys() and "Cat01" not in dictt.values():
        dictt.update({'Garfield' : 'Cat01'})
    for i in dictt.values(): # นับแมวและจิ้งจอก
        if "Cat" in i:
            num6 += 1
        elif "Fox" in i:
            num5 += 1
    print("Cat : "+str(num6))
    print("Fox : "+str(num5))
    for i, j in dict(sorted(dictt.items(), key=lambda x: x[-1])).items():
        print(i+" : "+j)
catfox()

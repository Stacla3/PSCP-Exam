"""CaesarV1"""
def caesar(number, text):
    """Start"""
    strr1 = "abcdefghijklmnopqrstuvwxyz"
    neww = ""
    for i in text:   #คำนวนหาตัวที่เปลี่ยนโดยใช้strr1และstrr2
        if i in strr1:
            result1 = strr1.index(i)+number
            if result1 > 25 or result1 < -25:
                while result1 > 25:
                    result1 -= 26
                while result1 < -25:
                    result1 += 26
            neww += strr1[result1]
        elif i in strr1.upper():
            result2 = strr1.upper().index(i)+number
            if result2 > 25 or result2 < -25:
                while result2 > 25:
                    result2 -= 26
                while result2 < -25:
                    result2 += 26
            neww += strr1.upper()[result2]
        else:
            neww += i   #เก็บค่าตัวอื่นมาด้วยโดยไม่แปลง
    return neww
print(caesar(int(input()), str(input())))

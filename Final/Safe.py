"""Safe"""
def main():
    """Start"""
    text1, text2 = str(input()).upper(), str(input()).upper()
    list1, list2, list3 = [], [], []
    for i in range(len(text1)):   # เปรียนเทียบค่าAscillว่าหมุนลงกับหมุนขึ้นอันไหนน้อยกว่ากัน
        if ord(text1[i]) < ord(text2[i]):
            list1.append(abs(ord(text1[i]) - ord(text2[i])))
            list2.append(abs((ord(text1[i])+26)-ord(text2[i])))
        elif ord(text1[i]) > ord(text2[i]):
            list1.append(abs(ord(text1[i]) - ord(text2[i])))
            list2.append(abs((ord(text1[i])-26)-ord(text2[i])))
        else:
            list1.append(0)
            list2.append(0)
    for i in range(len(list1)):   # อันไหนจำนวนครั้งหมุนน้อยสุดเอาอันนั้นและหาค่ารวม
        if list1[i] <= list2[i]:
            list3.append(list1[i])
        else:
            list3.append(list2[i])
    print(sum(list3))

main()

"""KABATA"""
def main():
    """Start"""
    num1 = int(input())
    set1 = set()
    for _ in range(num1):
        text = str(input()).replace("a", "a%")  #ใช้replaceเช็คให้แยกตัวง่ายขึ้น
        neww = text.split("%")
        if len(neww) > 1:
            for i in range(len(neww)-1):  #หาตัวว่าไม่ใช้ภาษาkabata
                if neww[i].isalpha():
                    if neww[i] != "ta" and neww[i] != "ba" and neww[i] != "ka" and neww[i] != "kka":
                        set1.add(neww[i])
                    if neww[i] == "ba" and neww[i+1] == "ka":
                        set1.add(neww[i])
                    if neww[i] != "ba" and neww[i+1] == "kka":
                        set1.add(neww[i])
            if set1 == set():
                print("yes")
            else:
                print("no")
            set1 = set()
        else:
            print("no")
main()

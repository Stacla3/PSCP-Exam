"""PrasomSib"""
def main():
    """Start"""
    text = input()
    num1, num2 = 0, 0
    for i in range(len(text)):   #ดูทุกตัวที่ติดกันว่าบวกกันเท่ากับ10เป๊ะมั้ย
        for j in text[i:]:   #บวกกันทุกตัวที่ติดกันได้เท่ากับ10เป๊ะมั้ย
            num1 += int(j)
            if num1 == 10:
                num2 += 1
        num1 = 0
    print(num2)
main()

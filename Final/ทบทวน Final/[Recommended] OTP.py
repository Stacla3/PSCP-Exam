"""[Recommended] OTP"""
def main():
    """Start"""
    dict1 = dict()
    num1, num2 = 0, 0
    while True:
        text = str(input())
        if text == "0":
            break
        for i in text:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in dict1:
            if dict1[i] == 2:
                num1 += 1
            elif dict1[i] == 3:
                num2 += 1
        if len(text) == 4 and num1 == 1:
            print("Valid")
        elif len(text) == 6 and num1 == 2 or len(text) == 6 and num2 == 1:
            print("Valid")
        elif len(text) == 8 and num1 == 3 or len(text) == 8 and num2 == 2:
            print("Valid")
        else:
            print("Invalid")
        dict1, num1, num2 = dict(), 0, 0
main()

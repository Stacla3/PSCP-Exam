"""OTP"""
def main():
    """Start"""
    dict1 = dict()
    count1, count2 = 0, 0
    while True:
        text = str(input())
        if text == "0":
            break
        for i in text:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i, j in dict1.items():
            if j == 2:
                count1 += 1
            elif j == 3:
                count2 += 1
        if len(text) == 4 and count1 == 1:
            print("Valid")
        elif len(text) == 6 and count2 == 1 or len(text) == 6 and count1 == 2:
            print("Valid")
        elif len(text) == 8 and count1 == 3 or len(text) == 8 and count2 == 2:
            print("Valid")
        else:
            print("Invalid")
        count1, count2, dict1 = 0, 0, dict()
main()

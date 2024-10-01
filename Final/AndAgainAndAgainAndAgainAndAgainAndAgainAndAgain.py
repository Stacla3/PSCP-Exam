"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main():
    """Start"""
    text = str(input())
    num1 = text.split()
    result = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    list1 = []
    num2 = 0
    strr = ""
    for i in num1:
        for j in i:
            if j in result:
                num2 += 1
        if num2 >= 2:
            list1.append(i)
        num2 = 0
    if len(list1) == 0:
        print("Nope")
    else:
        for i in sorted(list1):
            for j in i:
                if str(j).isalpha():
                    strr += j
            print(strr)
            strr = ""

main()

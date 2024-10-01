"""RockPaperScissor"""
def main():
    """Start"""
    text = str(input())
    num1 = 0
    num2 = 0
    for i in range(0, len(text), 2):
        text1 = text[i:i+2]
        if text1 == "RP":
            num2 += 1
        elif text1 == "PR":
            num1 += 1
        elif text1 == "SP":
            num1 += 1
        elif text1 == "PS":
            num2 += 1
        elif text1 == "RS":
            num1 += 1
        elif text1 == "SR":
            num2 += 1
        else:
            num1 += 0
            num2 += 0
    if num1 > num2:
        print("A", "win", str(num1)+"-"+str(num2))
    elif num1 < num2:
        print("B", "win", str(num2)+"-"+str(num1))
    elif num1 == num2:
        print("DRAW", num1 or num2)

main()

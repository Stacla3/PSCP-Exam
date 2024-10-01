"""[Recommend] Blackjack"""
def main():
    """start"""
    num1 = int(input())
    for _ in range(num1):
        num6 = 0
        text = str(input())
        if text.isnumeric():
            num2 = int(text)
        elif text == "J" or text == "Q" or text == "K": 
            num3 = 10
        elif text == "A":
            num4 = 1
            num5 = 11
    if num2 + num5 == 21 or num3 + num5 == 21 and num6 != 21 and num1 != 3:
        print(num2 + num5 or num3 + num5)
    elif num1 == 3:
        print(num3 + num3 +num3 or num2 + num2 + num2 or num2 + num2 + num3 or num2 + num3 + num3)
    else:
        print(num2 + num2 or num2 + num3 or num3 + num3)

main()

"""[Recommend] Harshad Number"""
def main():
    """Start"""
    text = 0
    num1 = []
    num2 = ""
    for i in range(1, 11):
        text = int(input())
        if text <= 10:
            print("Yes")
        else:
            text1 = str(text)
            num2 = text1
            num1 = num2
            print(num1)

main()

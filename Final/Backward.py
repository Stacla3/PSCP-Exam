"""Backward"""
def main():
    """Start"""
    text = 0
    num1 = []
    while True:
        text = str(input())
        if text == "NULL":
            break
        num1.append(text)
    num1.reverse()
    for i in num1:
        print(i)

main()

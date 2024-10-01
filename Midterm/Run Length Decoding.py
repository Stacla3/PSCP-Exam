"""Run Length Decoding"""
def main():
    """Start"""
    text = str(input())
    num1 = 0
    for i in text:
        if i.isnumeric():
            num2 = int(i)
            num1 -= 1
            if text[num1:num1].isnumeric():
                num2 = int(text[num1:num1+2])
        elif not i.isnumeric():
            num3 = str(i)
    print(num2*num3)

main()

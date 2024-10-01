"""LineSorting"""
def main():
    """Star"""
    num1 = int(input())
    num2 = []
    for _ in range(num1):
        text = str(input())
        num2.append(text)
    num3 = sorted(num2, key=len)
    for i in num3:
        print(i)

main()

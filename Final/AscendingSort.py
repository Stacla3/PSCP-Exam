"""AscendingSort"""
def main():
    """Start"""
    num1 = []
    for _ in range(5):
        text = int(input())
        num1.append(text)
    num2 = sorted(num1)
    for i in num2:
        print(i)

main()

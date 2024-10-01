"""[Recommended] Area"""
def main():
    """Start"""
    num1 = int(input())
    num2 = 0
    for i in range(num1):
        text = str(input())
        for i in text:
            if i != " ":
                num2 += 1
    print(num2)
main()

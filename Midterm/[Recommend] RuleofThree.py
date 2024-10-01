"""[Recommend] RuleofThree"""
def main():
    """Start"""
    num1 = int(input())
    num2 = 0
    for _ in range(num1):
        text1 = float(input())
        text2 = float(input())
        num2 += 1
        result1 = text2 / text1
        print(result1)

main()

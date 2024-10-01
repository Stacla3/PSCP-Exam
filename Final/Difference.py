"""Difference"""
def main():
    """Start"""
    num1 = int(input())
    num2 = int(input())
    set1 = set()
    set2 = set()
    for _  in range(num1):
        num3 = int(input())
        set1.add(num3)
    for _ in range(num2):
        num4 = int(input())
        set2.add(num4)
    result = sorted(set1 - set2)
    for i in result:
        print(i, end=" ")

main()

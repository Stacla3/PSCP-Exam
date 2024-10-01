"""Duplicate I"""
def main():
    """Start"""
    num1 = int(input())
    num2 = int(input())
    set1 = set()
    set2 = set()
    for _ in range(num1):
        text1 = str(input())
        set1.add(text1)
    for _ in range(num2):
        text2 = str(input())
        set2.add(text2)
    result = sorted(set1.intersection(set2), reverse=True)
    if len(result) == 0:
        print("Nope")
    else:
        for i in result:
            print(i)

main()

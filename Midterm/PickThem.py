"""PickThem"""
def main():
    """Start"""
    num1 = str(input())
    import json
    num2 = json.loads(num1)
    num3 = []
    for i in num2:
        if i % 2 == 0:
            num3.append(i)
    if len(num3) == 0:
        print("Nope")
    else:
        for i in num3:
            print(i)

main()

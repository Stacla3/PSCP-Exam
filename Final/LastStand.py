"""LastStand"""
def main():
    """Start"""
    num1 = input()
    import json
    num2 = json.loads(num1)
    for i in num2:
        print(str(i)[-1])

main()

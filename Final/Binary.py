"""Binary"""
def main():
    """Start"""
    num1 = abs(int(input()))
    num2 = [num1]
    num3 = []
    result = 0
    while num1 > 1:
        num1 //= 2
        num2.append(num1)
    result = sorted(num2)
    for i in result:
        if i % 2 == 0:
            i = 0
        else:
            i = 1
        num3.append(i)
    for i in num3:
        print(i, end="")

main()
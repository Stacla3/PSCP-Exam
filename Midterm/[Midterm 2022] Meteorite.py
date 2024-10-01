"""Metro"""
def main():
    """Start"""
    num1 = float(input())
    num2 = int(input())
    num3 = float(input())
    num4 = 1
    num5 = 0
    result = (num1/num2)
    if num1 < num3:
        print("0")
    elif result < num3:
        print("1")
    else:
        while True:
            if result >= num3:
                result /= num2
                num5 += 1
                num4 = (num4 + (num2**num5))
                if result < num3:
                    print((num4))
                    break

main()

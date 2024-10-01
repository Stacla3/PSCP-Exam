



























































"""[Midterm 2022] Calculator"""
def main():
    """Start"""
    num1 = int(input())
    num2 = ""
    if num1 == 1:
        print(num1)
    else:
        for i in range(1, num1+1):
            num2 += str(i)+"+"
        print(len(num2))

main()

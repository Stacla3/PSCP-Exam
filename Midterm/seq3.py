"""Seq3"""
def main():
    """Start"""
    num1_ = int(input())
    num2_ = 2
    for _ in range(num1_):
        for i in range(num1_):
            print(num2_+i, end=" ")
            num2_ += 1
        print()

main()

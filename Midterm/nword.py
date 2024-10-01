"""N world"""
def main():
    """start"""
    num1 = int(input())
    for i in range(num1):
        for j in range(num1):
            if i == j or j == 0 or j == num1 - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

main()

"""[Recommended] PongYa"""
def main():
    """Start"""
    num1 = int(input())
    if num1 % 3 == 0 or str(num1)[-1] == "3":
        print("PONG")
    else:
        print(num1)
main()

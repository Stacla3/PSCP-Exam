"""PongYa"""
def main():
    """Start"""
    num1 = int(input())
    if num1 % 3 == 0:
        print("PONG")
    elif str(num1)[-1] == "3":
        print("PONG")
    else:
        print(int(num1))
 
main()

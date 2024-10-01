"""Left Arrow"""
def main():
    """Start"""
    num1 = int(input())
    num2 = int(input())
    for i in range(num2//2):
        print(" "*i+"*"*num1)
    print(" "*(num2//2)+"*"*num1)
    for i in range((num2//2)+1,0,-1):
        print(" "*(i)+"*"*num1)
main()

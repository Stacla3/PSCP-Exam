"""Diginity"""
def main():
    """Start"""
    text = 1
    num = ""
    while text != 0:
        text = int(input())
        if text < 10:
            print(text)
        else:
            for i in str(text):
                num1 = int(i)
                num1 += num1
            if num1 < 10:
                print(num1)
main()

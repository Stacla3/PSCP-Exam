"""Turnstile"""
def main():
    """Start"""
    text = str(input())
    num1 = 0
    while text != "END":
        if text == "C":
            text = str(input())
            if text == "P":
                num1 += 1
        else:
            text = str(input())
    print(num1)

main()

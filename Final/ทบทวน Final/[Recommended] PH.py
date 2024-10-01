"""[Recommended] PH"""
def main():
    """Start"""
    num1 = float(input())
    if num1 < 0 or num1 > 14:
        print("error")
    elif num1 < 7:
        print("acidic")
    elif num1 == 7:
        print("neutral")
    elif num1 > 7:
        print("akaline")
main()

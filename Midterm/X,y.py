"""Quadant"""
def main():
    """Start"""
    lily = int(input())
    tulip = int(input())
    if lily > 0 and tulip > 0:
        print("Q1")
    elif lily < 0 and tulip > 0:
        print("Q2")
    elif lily < 0 and tulip < 0:
        print("Q3")
    elif lily > 0 and tulip < 0:
        print("Q4")
    elif lily != 0 and tulip == 0:
        print("X")
    elif lily == 0 and tulip != 0:
        print("Y")
    elif lily == 0 and tulip == 0:
        print("O")

main()

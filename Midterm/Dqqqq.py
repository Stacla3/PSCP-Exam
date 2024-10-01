"""Surpising"""
def main():
    """Start"""
    num1_ = float(input())
    num2_ = float(input())
    second = min(num1_ - num2_, num2_)
    lowscore = num1_ - num2_ - second
    if lowscore - num2_ > 2:
        print("Surprising")
    elif lowscore - num2_ <= 2:
        print("Not surprising")

main()

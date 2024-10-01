"""Surprising"""
def main():
    """Start"""
    total = float(input())
    highscore = float(input())
    second = min(total - highscore, highscore)
    lowscore = total - highscore - second
    if highscore - lowscore > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()

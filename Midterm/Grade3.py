"""Grade3"""
def main():
    """Start"""
    score = float(input())
    if score > 100 or score < 0:
        print("ERR")
    elif score >= 95 and score <= 100:
        print("A")
    elif score >= 90 and score < 95:
        print("B+")
    elif score >= 85 and score < 90:
        print("B")
    elif score >= 80 and score < 85:
        print("C+")
    elif score >= 75 and score < 80:
        print("C")
    elif score >= 70 and score < 75:
        print("D+")
    elif score >= 65 and score < 70:
        print("D")
    elif score >= 60 and score < 65:
        print("F+")
    elif score < 60:
        print("F")

main()

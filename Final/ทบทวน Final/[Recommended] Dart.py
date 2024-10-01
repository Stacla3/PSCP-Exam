"""[Recommended] Dart"""
def main():
    """Start"""
    num1 = int(input())
    countscore = 0
    for _ in range(num1):
        score = str(input()).split()
        result = ((int(score[0])**2)+(int(score[-1])**2))**0.5
        if result <= 2:
            countscore += 5
        elif result <= 4:
            countscore += 4
        elif result <= 6:
            countscore += 3
        elif result <= 8:
            countscore += 2
        elif result <= 10:
            countscore += 1
    print(countscore)
main()

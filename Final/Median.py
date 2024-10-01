"""Median"""
def main():
    """Start"""
    import math
    num1 = int(input())
    num2 = []
    for _ in range(num1):
        text = int(input())
        num2.append(text)
    result = math.ceil((len(num2))/2)
    if len(num2) % 2 == 0:
        print("%.1f" %((num2[result] + num2[result-1])/2))
    else:
        print("%.1f" %(num2[result-1]))

main()

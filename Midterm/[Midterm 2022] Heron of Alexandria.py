"""[Midterm 2022] Heron of Alexandria"""
def main():
    """Start"""
    import math
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    result = (num1 + num2 + num3)/2
    print("%.3f" %(math.sqrt(result*(result-num1)*(result-num2)*(result-num3))))

main()

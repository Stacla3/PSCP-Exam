"""PlanC"""
def ascend(num2_, num3_, num4_):
    """Start1"""
    if num2_ <= num3_ and num2_ <= num4_ and num3_ <= num4_:
        print("%.2f" %num2_+", "+"%.2f" %num3_+", "+"%.2f" %num4_)
    elif num2_ <= num3_ and num2_ <= num4_ and num3_ >= num4_:
        print("%.2f" %num2_+", "+"%.2f" %num4_+", "+"%.2f" %num3_)
    elif num3_ <= num2_ and num3_ <= num4_ and num2_ <= num4_:
        print("%.2f" %num3_+", "+"%.2f" %num2_+", "+"%.2f" %num4_)
    elif num3_ <= num2_ and num3_ <= num4_ and num2_ >= num4_:
        print("%.2f" %num3_+", "+"%.2f" %num4_+", "+"%.2f" %num2_)
    elif num4_ <= num2_ and num4_ <= num3_ and num3_ <= num2_:
        print("%.2f" %num4_+", "+"%.2f" %num3_+", "+ "%.2f" %num2_)
    elif num4_ <= num2_ and num4_ <= num3_ and num3_ >= num2_:
        print("%.2f" %num4_+", "+"%.2f" %num2_+", "+ "%.2f" %num3_)
def descend(num2_, num3_, num4_):
    """Start2"""
    if num2_ >= num3_ and num2_ >= num4_ and num3_ >= num4_:
        print("%.2f" %num2_+", "+"%.2f" %num3_+", "+"%.2f" %num4_)
    elif num2_ >= num3_ and num2_ >= num4_ and num3_ <= num4_:
        print("%.2f" %num2_+", "+"%.2f" %num4_+", "+"%.2f" %num3_)
    elif num3_ >= num2_ and num3_ >= num4_ and num2_ >= num4_:
        print("%.2f" %num3_+", "+"%.2f" %num2_+", "+"%.2f" %num4_)
    elif num3_ >= num2_ and num3_ >= num4_ and num2_ <= num4_:
        print("%.2f" %num3_+", "+"%.2f" %num4_+", "+"%.2f" %num2_)
    elif num4_ >= num2_ and num4_ >= num3_ and num3_ >= num2_:
        print("%.2f" %num4_+", "+"%.2f" %num3_+", "+"%.2f" %num2_)
    elif num4_ >= num2_ and num4_ >= num3_ and num3_ <= num2_:
        print("%.2f" %num4_+", "+"%.2f" %num2_+", "+"%.2f" %num3_)
def main():
    """Start"""
    num1_ = input()
    num2_ = float(input())
    num3_ = float(input())
    num4_ = float(input())
    if num1_ == "Ascend":
        ascend(num2_, num3_, num4_)
    elif num1_ == "Descend":
        descend(num2_, num3_, num4_)

main()

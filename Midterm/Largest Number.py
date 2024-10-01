"""NUMBER"""
def main():
    """Start"""
    num1_ = int(input())
    num2_ = int(input())
    num3_ = int(input())
    num1_ = str(num1_)
    num2_ = str(num2_)
    num3_ = str(num3_)

    lily = num1_ + num2_ + num3_
    lily1 = num1_ + num3_ + num2_
    lily2 = num2_ + num1_ + num3_
    lily3 = num2_ + num3_ + num1_
    lily4 = num3_ + num2_ + num1_
    lily5 = num3_ + num1_ + num2_
    if int(lily) >= int(lily1) and int(lily) >= int(lily2) and int(lily) >= int(lily3)\
          and int(lily) >= int(lily4) and int(lily) >= int(lily5):
        print(int(lily))
    elif int(lily1) >= int(lily2) and int(lily1) >= int(lily3)\
          and int(lily1) >= int(lily4) and int(lily1) >= int(lily5):
        print(lily1)
    elif int(lily2) >= int(lily3) and int(lily2) >= int(lily4) and int(lily2) >= int(lily5):
        print(int(lily2))
    elif int(lily3) >= int(lily4) and int(lily3) >= int(lily5):
        print(int(lily3))
    elif int(lily4) >= int(lily5):
        print(int(lily4))
    else:
        print(lily5)

main()

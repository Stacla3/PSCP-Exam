"""Zombie"""
def align():
    """Star"""
    num1_ = int(input())
    text1 = str(input())
    text2 = str(input())
    space = (num1_- len(text2))
    if text1 == "left":
        print(text2.ljust(num1_))
    elif text1 == "right":
        print(text2.rjust(num1_))
    elif text1 == "center" and space % 2 == 0:
        print(text2.center(num1_))
    elif text1 == "center" and space % 2 != 0:
        print(" "*(space - (space//2))+text2+" "*(space//2))

align()

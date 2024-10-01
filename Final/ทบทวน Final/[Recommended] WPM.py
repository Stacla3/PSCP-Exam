"""[Recommended] WPM"""
def calcu(num1):
    """Start"""
    if num1 < 11:
        return "Very Slow"
    elif num1 >= 11 and num1 <= 20:
        return "Slow"
    elif num1 >= 21 and num1 <= 30:
        return "Average"
    elif num1 >= 31 and num1 <= 40:
        return "Fast"
    elif num1 > 40:
        return "Very Fast"
def calcu2(num1):
    """Start"""
    if num1 < 26:
        return "Very Slow"
    elif num1 >= 26 and num1 <= 35:
        return "Slow/Beginner"
    elif num1 >= 36 and num1 <= 45:
        return "Intermediate/Average"
    elif num1 >= 46 and num1 <= 65:
        return "Fast/Advanced"
    elif num1 >= 66 and num1 <= 80:
        return "Very Fast"
    elif num1 > 80:
        return "Insane"
def main():
    """Start"""
    text = str(input())
    num1 = int(input())
    new1 = calcu(num1)
    new2 = calcu2(num1)
    if text == "Kids":
        print(new1)
    elif text == "Adults":
        print(new2)
main()

"""NumDays"""
def main():
    """Start"""
    date1 = int(input())
    month1 = int(input())
    date2 = int(input())
    month2 = int(input())
    amount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result1 = 0
    result2 = 0
    for i in amount[:month1]:
        result1 += i
    for i in amount[:month2]:
        result2 += i
    if date1 > amount[month1-1] or date2 > amount[month2-1]:
        print("Impossible")
    else:
        neww2 = abs((result1-(amount[month1-1]-date1)) - (result2-(amount[month2-1]-date2)))
        print(neww2)
main()

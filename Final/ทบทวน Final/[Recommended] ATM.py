"""[Recommended] ATM"""
def main():
    """Start"""
    money = int(input())
    while True:
        text = str(input())
        neww = text.split()
        if text == "END":
            break
        if neww[0] == "D":
            money += int(neww[1])
        elif neww[0] == "W":
            money -= int(neww[1])
        if money <= 0:
            money = 0
    print(money)
main()

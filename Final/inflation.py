"""Inflation"""
def main():
    """Docstring"""
    money = float(input())*100
    year = int(input())
    for _ in range(year):
        money = int(money)+((int(money)*381)//10000)
    print("%d.%02d" % (money//100, money%100))
main()

"""Compound Interest"""
def main():
    """Start"""
    money = int(input())
    dokk = float(input())
    year = int(input())
    for _ in range(1, year+1):
        money *= 1+(dokk/100)
    print("%.2f" %money)

main()

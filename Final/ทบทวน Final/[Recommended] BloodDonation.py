"""[Recommended] BloodDonation"""
def main():
    """Start"""
    ages = int(input())
    weight = int(input())
    donate = int(input())
    num1 = 0
    if ages == 17 or ages >= 60 and ages <= 70:
        books = str(input())
    if ages < 17 or ages > 70:
        num1 += 1
    if weight < 45:
        num1 += 1
    if donate == 0 and ages > 55:
        num1 += 1
    if ages == 17 and books != "True":
        num1 += 1
    if ages >= 60 and ages <= 70 and books != "True":
        num1 += 1
    if num1 > 0:
        print("No")
    else:
        print("Yes")
main()

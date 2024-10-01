"""BloodDonation"""
def main():
    """Start"""
    ages = int(input())
    weight = int(input())
    count = int(input())
    if ages == 17 or ages >= 60 and ages <= 70:
        check = str(input())
    if ages < 17 or ages > 70:
        print("No")
    elif weight < 45:
        print("No")
    elif count == 0 and ages > 55:
        print("No")
    elif ages == 17 and check == "False":
        print("No")
    elif ages >= 60 and ages <= 70 and check == "False":
        print("No")
    else:
        print("Yes")
main()

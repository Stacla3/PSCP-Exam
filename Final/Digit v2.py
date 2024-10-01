"""Digit v2"""
def main():
    """Start"""
    text = str(input()).split()
    set1 = {1}
    for i in text:
        if "ty" in i:
            num1 = 2
            set1.add(num1)
        elif i == "hundred":
            num1 = 3
            set1.add(num1)
        elif i == "thousand":
            num1 = 4
            set1.add(num1)
        elif "teen" in i:
            num1 = 2
            set1.add(num1)
        elif i == "eleven" or i == "twelve" or i == "ten":
            num1 = 2
            set1.add(num1)
    maxx = max(set1)
    print(maxx)
main()

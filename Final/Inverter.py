"""Inverter"""
def main():
    """Start"""
    text = str(input())
    strr = ""
    for i in text:
        if i == "0":
            i = "1"
        elif i == "1":
            i = "0"
        strr += i
    print(strr.lstrip("0"))
main()

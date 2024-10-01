"""[Recommended] Inverter"""
def main():
    """Start"""
    coder = str(input())
    neww = ""
    for i in coder:
        if i == "0":
            i = "1"
        elif i == "1":
            i = "0"
        neww += i
    print(neww.lstrip("0"))
main()

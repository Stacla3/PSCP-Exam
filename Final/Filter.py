"""Filter"""
def main():
    """Start"""
    import json
    num1 = str(input())
    num2 = json.loads(num1)
    num3 = dict(num2)
    num4 = int(input())
    num5 = []
    num6 = sorted(num3.items(), key=lambda x:x[0])
    num7 = dict(num6)
    for i, j in num7.items():
        if j >= num4:
            num5.append(j)
            print(i+"\t"+"%.2f" %j)
    if len(num5) == 0:
        print("Nope")

main()

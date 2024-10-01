"""Impostor"""
def main():
    """Start"""
    listt, num3, num6 = [], dict(), 0
    import json
    while True:
        text = str(input())
        if text == "Start":
            break
        num1 = json.loads(text)
        num2 = dict(num1)
        num3.update(num2)
    num4 = sorted(num3.items(), key=lambda x: x[0])
    num5 = dict(num4)
    while True:
        text1 = str(input())
        if text1 == "End":
            break
        listt.append(text1)
    for i, j in num5.items():
        if i not in listt:
            if j == "Impostor":
                num6 += 1
    print(num6, "Impostor Remains")
    print("***Alive***")
    for i, j in num5.items():
        if i not in listt:
            print(i+" : "+j)
    print("***Dead***")
    for q, r in num5.items():
        if q in listt:
            print(q+" : "+r)

main()

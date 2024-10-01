"""Easy Histogram"""
def main():
    """Start"""
    text, dictt = str(input()), {}
    for i in text:
        if i != " ":
            if i in dictt:
                dictt[i] += 1
            else:
                dictt[i] = 1
    for i in sorted(dictt, key=lambda x: (str(x).lower(), x.swapcase())):
        print(i+" = "+str(dictt[i]))

main()

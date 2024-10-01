"""Easy Histogram"""
def main():
    """Start"""
    text = str(input())
    dictt = {}
    strr = ""
    newwstr = ""
    check = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    for i in text:
        if i != " ":
            if i in dictt:
                dictt[i] += 1
            else:
                dictt[i] = 1
    for i in dictt.keys():
        newwstr += i
    for i in check:
        if i in newwstr:
            strr += i
    for i in strr:
        print(i+" = "+str(dictt[i]))

main()

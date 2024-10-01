"""DATA SPIKE"""
def main():
    """START"""
    pre1 = int(input())
    pre2 = int(input())
    pre3 = int(input())
    pre4 = int(input())
    pre5 = int(input())
    pre6 = int(input())
    pre7 = int(input())
    pre8 = int(input())
    if pre1 > pre2 and pre1 > pre3 and pre1 > pre4 and pre1 > pre5 and \
        pre1 > pre6 and pre1 > pre7 and pre1 > pre8:
        print(pre1)
    elif pre2 > pre3 and pre2 > pre4 and pre2 > pre5 and \
        pre2 > pre6 and pre2 > pre7 and pre2 > pre8:
        print(pre2)
    elif pre3 > pre4 and pre3 > pre5 and pre3 > pre6 and \
        pre3 > pre7 and pre3 > pre8:
        print(pre3)
    elif pre4 > pre5 and pre4 > pre6 and pre4 > pre7 and pre4 > pre8:
        print(pre4)
    elif pre5 > pre6 and pre5 > pre7 and pre5 > pre8:
        print(pre5)
    elif pre6 > pre7 and pre6 > pre8:
        print(pre6)
    elif pre7 > pre8:
        print(pre7)
    else:
        print(pre8)

main()

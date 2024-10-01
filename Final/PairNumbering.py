"""PairNumbering"""
def main():
    """Start"""
    import json
    list1 = json.loads(str(input()))
    list2 = json.loads(str(input()))
    num1 = int(input())
    dict1, dict2 = {}, {}
    set1, set4 = set(), set()
    list3, list4 = [], []
    result = 0
    for i in sorted(list1):
        if i <= num1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
    for i in sorted(list2):
        if i <= num1:
            if i not in dict2:
                dict2[i] = 1
            else:
                dict2[i] += 1
    for i in dict1:
        for j in dict2:
            if i + j == num1:
                set1.add(i)
                set4.add(j)
                result += 1
    for i, o in dict1.items():
        if o > 1 and i in set1:
            list3.append(o-1)
    for j, k in dict2.items():
        if k > 1 and j in set4:
            list4.append(k-1)
    if len(list3) == 0 and len(list4) != 0:
        for i in list4:
            result += i
        print(result)
    elif len(list4) == 0 and len(list3) != 0:
        for i in list3:
            result += i
        print(result)
    elif len(list4) != 0 and len(list3) != 0:
        for i in list3:
            result += i
        for j in list4:
            result += j
        print(result)
    elif len(list3) == 0 and len(list4) == 0 or result == 0:
        print(result)
main()

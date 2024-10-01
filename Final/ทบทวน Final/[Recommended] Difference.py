"""[Recommended] Difference"""
def main():
    """Start"""
    import json
    list1 = list(json.loads(str(input())))
    list2 = list(json.loads(str(input())))
    copy1 = list1.copy()
    dict1 = dict()
    for i in list1:
        if i in list2:
            copy1.remove(i)
            list2.remove(i)
    if copy1+list2 == []:
        print("ONAJI DAYO!")
    else:
        for i in copy1+list2:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in sorted(dict1):
            print(i, dict1[i])
main()

"""[Super Recommended] Reachability"""
def main():
    """Start"""
    import json
    list1 = str(input()).replace("'", "\"")
    want = str(input())
    neww = dict(json.loads(list1))
    list1 = []
    dict1 = dict()
    for i in neww:
        if i in dict1:
            dict1[i] += [neww[i]]
        else:
            dict1[i] = [neww[i]]
main()

"""Matrix_MN"""
def main():
    """Start"""
    num1 = int(input())
    num2 = int(input())
    list1 = []
    list2 = []
    for _ in range(num1):
        for _ in range(num2):
            num3 = int(input())
            list1.append(num3)
        list2.append(list1)
        list1 = []
    for i in range(len(list2)):
        result = str(list2[i]).strip("[]")
        neww = result.replace(",", "")
        print(neww)
 
main()

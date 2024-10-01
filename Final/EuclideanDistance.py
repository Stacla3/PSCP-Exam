"""EuclideanDistance"""
def main():
    """Start"""
    import math
    num1 = int(input())
    list1 = []
    count1 = 0
    for _ in range(num1):
        text = str(input()).split()
        list1.append(text)
    for i in range(len(list1)-1):
        result = math.sqrt(((int(list1[i+1][0])-int(list1[i][0]))**2)\
                           +((int(list1[i+1][1])-int(list1[i][1]))**2))
        count1 += result
    print("%.2f" %count1)
main()

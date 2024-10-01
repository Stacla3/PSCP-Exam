"""WordSequence II"""
def main():
    """Start"""
    text1 = str(input())
    text2 = str(input())
    result = max(len(text1), len(text2))
    for i in range(result+1):
        print(text2[0:i]+text1[i:])

main()

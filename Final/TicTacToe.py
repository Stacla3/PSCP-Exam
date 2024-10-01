"""TicTacToe"""
def main():
    """Start"""
    text1 = str(input())
    text2 = str(input())
    text3 = str(input())
    neww = text1+text2+text3
    num2 = 0
    dict1 = dict()
    for i in neww:
        result = neww.find(i)
        print(result)
main()

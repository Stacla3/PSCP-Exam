"""[Recommended] TicTacToe"""
def main():
    """Start"""
    text1, text2, text3, = str(input()), str(input()), str(input())
    neww = text1+text2+text3
    if neww[0] == "X" and neww[1] == "X" and neww[2] == "X" \
        or neww[3] == "X" and neww[4] == "X" and neww[5] == "X"\
        or neww[6] == "X" and neww[7] == "X" and neww[8] == "X":
        print("X WIN")
    elif neww[0] == "O" and neww[1] == "O" and neww[2] == "O" \
        or neww[3] == "O" and neww[4] == "O" and neww[5] == "O"\
        or neww[6] == "O" and neww[7] == "O" and neww[8] == "O":
        print("O WIN")
    elif neww[0] == "X" and neww[3] == "X" and neww[6] == "X" \
        or neww[1] == "X" and neww[4] == "X" and neww[7] == "X"\
        or neww[2] == "X" and neww[5] == "X" and neww[8] == "X":
        print("X WIN")
    elif neww[0] == "O" and neww[3] == "O" and neww[6] == "O" \
        or neww[1] == "O" and neww[4] == "O" and neww[7] == "O"\
        or neww[2] == "O" and neww[5] == "O" and neww[8] == "O":
        print("O WIN")
    elif neww[0] == "X" and neww[4] == "X" and neww[8] == "X" \
        or neww[2] == "X" and neww[4] == "X" and neww[6] == "X":
        print("X WIN")
    elif neww[0] == "O" and neww[4] == "O" and neww[8] == "O" \
        or neww[2] == "O" and neww[4] == "O" and neww[6] == "O":
        print("O WIN")
    else:
        print("DRAW")
main()

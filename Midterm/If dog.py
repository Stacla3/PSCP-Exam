"""IF"""
def main():
    """start"""
    height = int(input())
    if height > 180:
        print("You're hit the door edge.")
    elif height <= 180:
        print("Nothing happens.")

main()

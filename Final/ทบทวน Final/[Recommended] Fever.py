"""[Recommended] Fever"""
def main():
    """Start"""
    fever = float(input())
    if fever >= 36 and fever < 38:
        print("No Fever")
    elif fever >= 38 and fever < 39:
        print("Mild Fever")
    elif fever >= 39 and fever < 40:
        print("High Fever")
    else:
        print("Very High Fever")
main()

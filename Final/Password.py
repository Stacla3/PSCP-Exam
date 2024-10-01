"""Password"""
def main():
    """Start"""
    import hashlib
    neww = hashlib.sha512()
    neww.update(input().encode("ASCII"))
    result = neww.hexdigest()
    print(result.upper())

main()

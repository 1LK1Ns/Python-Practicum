def is_palindrome(x):
    if isinstance(x, int):
        x = str(x)
    if x == x[::-1]:
        return True
    return False
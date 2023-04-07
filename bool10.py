def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    import math
    a = math.sqrt(a)
    return (a/1)==(a//1)
print(main(10))
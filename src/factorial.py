def fact(n):
    """Return factorial of n (non-negative integer)."""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

if __name__ == "__main__":
    print(f"fact(5) = {fact(5)}")

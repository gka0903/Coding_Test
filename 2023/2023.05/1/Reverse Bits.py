def reverse_bits(n: int) -> int:
    result = 0
    for i in range(32):
        # Shift the current result to the left
        result <<= 1
        # Check if the least significant bit of n is 1
        if n & 1 == 1:
            result |= 1
        # Shift n to the right
        n >>= 1
    return result

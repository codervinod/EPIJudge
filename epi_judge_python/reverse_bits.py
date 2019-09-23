from test_framework import generic_test

def reverse_bit_brute(x, num_bits):
    y=0
    for _ in range(num_bits):
        y = y | (x & 1)
        x = x >> 1
        y = y << 1

    return y >> 1

CACHE_REV_BITS = dict()

def cache_reverse_bits():
    if CACHE_REV_BITS:
        return
    for i in range(1<<16):
        CACHE_REV_BITS[i] = reverse_bit_brute(i,16)

def reverse_bits(x):
    # TODO - you fill in here.

    y= (CACHE_REV_BITS[x & 0xFFFF] << 48) | (
            CACHE_REV_BITS[x >> 16 & 0xFFFF] << 32) | (
            CACHE_REV_BITS[x >> 32 & 0xFFFF] << 16) | (
        CACHE_REV_BITS[x >> 48 & 0xFFFF])

    return y


if __name__ == '__main__':
    cache_reverse_bits()

    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))

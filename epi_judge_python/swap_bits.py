from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    i_bit = x >> i & 1
    j_bit = x >> j & 1
    if i_bit != j_bit:
        bit_mask = (1 << i) | (1 << j)
        x = x ^ bit_mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))

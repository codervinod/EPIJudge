from test_framework import generic_test

CACHED_PARITY = dict()


def parity_brute(x):
    p = 0
    while x:
        if x & 1 == 1:
            p ^= 1
        x = x >> 1
    return p


def compute_cache():
    if CACHED_PARITY:
        return
    for x in range(1 << 16):
        CACHED_PARITY[x] = parity_brute(x)


def parity(x):
    # TODO - you fill in here.
    p = (CACHED_PARITY[x & 0xFFFF]) ^ (
            CACHED_PARITY[(x >> 16) & 0xFFFF]) ^ (
            CACHED_PARITY[(x >> 32) & 0xFFFF]) ^ (
            CACHED_PARITY[(x >> 48) & 0xFFFF])
    return p


if __name__ == '__main__':
    compute_cache()

    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))

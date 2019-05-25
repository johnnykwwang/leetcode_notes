def count_bits_1(x):
    c = 0
    while x:
        c += x & 1
        x >>= 1
    return c

def count_bits_2(x):
    c = 0
    while x:
        x &= (x-1)
        c += 1
    return c

print count_bits_2(1048575)

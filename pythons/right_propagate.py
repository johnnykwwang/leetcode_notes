
def right_propagate(x):
    # x=01010000 --> return 01011111

    x_without_right_bit = x & (x-1)
    right_bit = x & ~(x-1)
    right_propogate = ( right_bit << 1 ) - 1

    return x_without_right_bit + right_propogate

def test_if_power_of_2(x):
    return x&(x-1) == 0

print test_if_power_of_2(32)

# print right_propagate( 0x50 ) == 0x5F

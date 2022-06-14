from cmath import inf


def count_bits(n):
    num = n
    binary = []
    while num != 0:
        if num % 2 == 0:
            binary.insert(0, "0")
            num = num//2
        else:
            binary.insert(0, "1")
            num = num//2
    
    return binary.count("1")


print(count_bits(123))

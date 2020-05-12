def print_formatted(number):
    decimal = number
    width = len(bin(decimal)[2:])
    for i in range(1, decimal + 1):
        print(' '.join(map(lambda x: x.rjust(width), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))


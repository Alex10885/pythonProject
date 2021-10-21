n = int(input())

bin_num = bin(n)
oct_num = oct(n)
hex_num = hex(n)

print(bin_num[2:], oct_num[2:], hex_num[2:].upper(), sep='\n')

def print_formatted(number):
    
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]

        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

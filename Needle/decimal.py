
def decimal(num):
    # assuming that the coming num is a valid integer here
    print "0x" + ChangeHexInt(num), "Binary: " + ChangeBinInt(num)


def ChangeHexInt(n):
    if n == 0:
        return '0'
    else:
        hex_num = ''
        hex_digits = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
        rem = n % 16
        quot = n / 16
        hex_num += hex_digits[quot]
        while rem >= 16:
            hex_num += hex_digits[quot]
            rem %= 16
            quot /= 16
        hex_num += hex_digits[rem]
        return hex_num


def ChangeBinInt(n):
    if n == 0:
        return '0'
    else:
        bin_num = ''
        rem = n % 2
        quot = n / 2
        bin_num += str(rem)
        while quot > 1:
            quot /= 2
            rem %= 2
            bin_num += str(rem)
        bin_num += str(quot)
        return bin_num[::-1]


if __name__ == '__main__':
    import sys
    decimal(sys.argv[0])

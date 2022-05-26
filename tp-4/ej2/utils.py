
def print_pattern(pattern, length):
    aux = pattern.reshape(length, length)
    str = ''
    for i in range(5):
        for j in range(5):
            str = str + ('* ' if aux[i][j] == 1 else '  ')
        str = str + '\n'
    print(str)


def sign(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0
# ====================================================================

def code_bits(f):
    bits = bin(int.from_bytes(f, 'big'))[2:]

    while len(bits) % 8 != 0:
        bits = '0' + bits

    return bits


def decode_bits(f):
    bits = int(f, 2)
    byte = bits.to_bytes((bits.bit_length() + 7) // 8, 'big')

    return byte


# ====================================================================

def str_to_list(s):
    res = []
    for i in s:
        res += [int(i)]
    return res


def list_to_str(l):
    res = ''
    for i in l:
        res += str(i)
    return res


def scrambler(b):
    res = []
    a = str_to_list(b)

    for i in range(len(a)):
        if i >= 3:
            if i >= 7:
                res.append(a[i] ^ res[i - 3] ^ res[i - 7])
            else:
                res.append(a[i] ^ res[i - 3])
        else:
            res.append(a[i])

    return list_to_str(res)


def descrambler(b):
    res = []
    a = str_to_list(b)

    for i in range(len(a)):
        if i >= 3:
            if i >= 7:
                res.append(a[i] ^ a[i - 3] ^ a[i - 7])
            else:
                res.append(a[i] ^ a[i - 3])
        else:
            res.append(a[i])

    return list_to_str(res)


# ====================================================================

def paritet(a):
    n = 0

    for i in a:
        if i == '1':
            n = n + 1

    return 2 * n - len(a)


def coding(a):
    temp_par = 1
    res = ''
    i = 0

    table5b_6b = {'00000': ['100111', '011000'],
                  '00001': ['011101', '100010'],
                  '00010': ['101101', '010010'],
                  '00011': ['110001', '110001'],
                  '00100': ['110101', '001010'],
                  '00101': ['101001', '101001'],
                  '00110': ['011001', '011001'],
                  '00111': ['111000', '000111'],
                  '01000': ['111001', '000110'],
                  '01001': ['100101', '100101'],
                  '01010': ['010101', '010101'],
                  '01011': ['110100', '110100'],
                  '01100': ['001101', '001101'],
                  '01101': ['101100', '101100'],
                  '01110': ['011100', '011100'],
                  '01111': ['010111', '101000'],
                  '10000': ['011011', '100100'],
                  '10001': ['100011', '100011'],
                  '10010': ['010011', '010011'],
                  '10011': ['110010', '110010'],
                  '10100': ['001011', '001011'],
                  '10101': ['101010', '101010'],
                  '10110': ['011010', '011010'],
                  '10111': ['111010', '000101'],
                  '11000': ['110011', '001100'],
                  '11001': ['100110', '100110'],
                  '11010': ['010110', '010110'],
                  '11011': ['110110', '001001'],
                  '11100': ['001110', '001110'],
                  '11101': ['101110', '010001'],
                  '11110': ['011110', '100001'],
                  '11111': ['101011', '010100']}

    table3b_4b = {'000': ['1011', '0100'],
                  '001': ['1001', '1001'],
                  '010': ['0101', '0101'],
                  '011': ['1100', '0011'],
                  '100': ['1101', '0010'],
                  '101': ['1010', '1010'],
                  '110': ['0110', '0110'],
                  '111': ['1110', '0001']}

    while len(a) > i:
        temp = a[i: i + 3]
        temp1 = a[i + 3: i + 8]

        if temp_par == 1:
            index = 1
        else:
            index = 0

        s = table5b_6b[temp1][index]

        temp_par += paritet(s)

        if temp_par == 1:
            index = 1
        else:
            index = 0

        s0 = table3b_4b[temp][index]

        temp_par += paritet(s0)

        i += 8
        res += s + s0

    return res


def decoding(a):
    res = ''
    i = 0

    table5b_6b = {'100111': '00000',
                  '011000': '00000',
                  '011101': '00001',
                  '100010': '00001',
                  '101101': '00010',
                  '010010': '00010',
                  '110001': '00011',
                  '110101': '00100',
                  '001010': '00100',
                  '101001': '00101',
                  '011001': '00110',
                  '111000': '00111',
                  '000111': '00111',
                  '111001': '01000',
                  '000110': '01000',
                  '100101': '01001',
                  '010101': '01010',
                  '110100': '01011',
                  '001101': '01100',
                  '101100': '01101',
                  '011100': '01110',
                  '010111': '01111',
                  '101000': '01111',
                  '011011': '10000',
                  '100100': '10000',
                  '100011': '10001',
                  '010011': '10010',
                  '110010': '10011',
                  '001011': '10100',
                  '101010': '10101',
                  '011010': '10110',
                  '111010': '10111',
                  '000101': '10111',
                  '110011': '11000',
                  '001100': '11000',
                  '100110': '11001',
                  '010110': '11010',
                  '110110': '11011',
                  '001001': '11011',
                  '001110': '11100',
                  '101110': '11101',
                  '010001': '11101',
                  '011110': '11110',
                  '100001': '11110',
                  '101011': '11111',
                  '010100': '11111'}

    table3b_4b = {'1011': '000',
                  '0100': '000',
                  '1001': '001',
                  '0101': '010',
                  '1100': '011',
                  '0011': '011',
                  '1101': '100',
                  '0010': '100',
                  '1010': '101',
                  '0110': '110',
                  '1110': '111',
                  '0001': '111'}

    while len(a) > i:
        temp = a[i: i + 6]
        temp1 = a[i + 6: i + 10]

        s0 = table5b_6b[temp]
        s = table3b_4b[temp1]

        res += s + s0
        i += 10

    return res

# ====================================================================

def code_4b_3t(a):
    res = ''
    table4b_3t = {'0000': '+0+',
                  '0001': '0-+',
                  '0010': '+-0',
                  '0011': '00+',
                  '0100': '-+0',
                  '0101': '0++',
                  '0110': '-++',
                  '0111': '-0+',
                  '1000': '+00',
                  '1001': '+-+',
                  '1010': '++-',
                  '1011': '+0-',
                  '1100': '+++',
                  '1101': '0+0',
                  '1110': '0+-',
                  '1111': '++0'}

    i = 0
    while len(a) - 3 > i:
        index = a[i] + a[i + 1] + a[i + 2] + a[i + 3]

        res += table4b_3t[index]
        i += 4

    return res


def decoding_4b_3t(a):
    res = ''
    table4b_3t = {'000': 'н/д',
                  '+0+': '0000',
                  '0-0': '0000',
                  '0-+': '0001',
                  '+-0': '0010',
                  '00+': '0011',
                  '--0': '0011',
                  '-+0': '0100',
                  '0++': '0101',
                  '-00': '0101',
                  '-++': '0110',
                  '--+': '0110',
                  '-0+': '0111',
                  '+00': '1000',
                  '0--': '1000',
                  '+-+': '1001',
                  '---': '1001',
                  '++-': '1010',
                  '+--': '1010',
                  '+0-': '1011',
                  '+++': '1100',
                  '-+-': '1100',
                  '0+0': '1101',
                  '-0-': '1101',
                  '0+-': '1110',
                  '++0': '1111',
                  '00-': '1111'}

    i = 0
    while len(a) - 2 > i:
        index = a[i] + a[i + 1] + a[i + 2]

        res += table4b_3t[index]
        i += 3

    return res


# ====================================================================

f = open('1.rar', 'rb')
f2 = open('2.rar', 'wb')

b = f.read()
bits = code_bits(b)
memory = bits

print(bits, '\n', '\n')
print('****************************************Логическое кодирование 8b/10b****************************************')

bits = coding(bits)

print(bits, '\n')
print('****************************************Скремблер a[i]^b[i-3]^b[i-7]****************************************')

bits = scrambler(bits)

print(bits, '\n')
print('****************************************Физическое кодирование 4B/3T****************************************')

bits = code_4b_3t(bits)

print(bits, '\n', '\n')
print('****************************************Физическое декодирование 4B/3T****************************************')

bits = decoding_4b_3t(bits)

print(bits, '\n')
print('****************************************Дескремблер a[i]^a[i-3]^a[i-7]****************************************')

bits = descrambler(bits)

print(bits, '\n')
print('****************************************Логическое декодирование 8b/10b****************************************')
bits = decoding(bits)

print(bits, '\n')
print(bits == memory)

b = decode_bits(bits)
f2.write(b)

f.close()
f2.close()

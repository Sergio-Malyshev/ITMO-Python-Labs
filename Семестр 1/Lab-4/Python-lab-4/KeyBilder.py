import random


def buildkey():
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfavit = '01234567890123456789ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = str(random.randint(100, 1000))
    n1 = int(number[:-2])
    n2 = int(number[1::3])
    n3 = int(number[-1:])
    block1 = "".join(random.choice(chars) for i in range(5))
    g_key = block1 + '-'

    for i in range(4):
        block = block1[:-1 * i]
        g_key += block
        if len(block) > 2:
            g_key += '-'
    blocks = g_key.split("-")
    b2 = str(blocks[1])
    b3 = blocks[2]
    b4 = blocks[3]
    final_key = ''
    new_key = ''
    for i in b2:
        index = alfavit.find(i)
        new_index = index + n1
        if i in alfavit:
            new_key += alfavit[new_index]
        else:
            new_key += i
    final_key += new_key + '-'
    new_key = ''
    for i in b3:
        index = alfavit.find(i)
        new_index = index + n2
        if i in alfavit:
            new_key += alfavit[new_index]
        else:
            new_key += i
    final_key += new_key + '-'
    new_key = ''
    for i in b4:
        index = alfavit.find(i)
        new_index = index + n3
        if i in alfavit:
            new_key += alfavit[new_index]
        else:
            new_key += i
    final_key += new_key
    answer = block1 + '-' + final_key
    # print('сгенерированный ключ:', g_key)
    # print('число сдвига:', number)
    # print(answer)
    return answer

import random

specialchars = '@#$%^*()_-=+/?.,~[]{}|;:'
strippedchars = '!1liI0oO'


def stringGenerator(charOptions, strLength=20):
    chars = ''
    for opt in charOptions:
        if opt == 1:
            chars += 'abcdefhjkmnpqrstuvwxyz'
        if opt == 2:
            chars += 'ABCDEFHJKMNPQRSTUVWXYZ'
        if opt == 3:
            chars += '0123456789'
        if opt == 4:
            chars += specialchars
        if opt == 5:
            chars += strippedchars

    return ''.join(random.choice(chars) for x in range(strLength))

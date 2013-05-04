# Copyright (C) 2012-2013  Benjamin Althues
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

import random

specialchars = '@#$%^*()_-=+/?.,~[]{}|;:'
strippedchars = '!1liI0oO'

def stringGenerator(charOptions, strLength=20):
    chars = ''
    for opt in charOptions:
        if opt == '1':
            chars += 'abcdefhjkmnpqrstuvwxyz'
        if opt == '2':
            chars += 'ABCDEFHJKMNPQRSTUVWXYZ'
        if opt == '3':
            chars += '0123456789'
        if opt == '4':
            chars += specialchars
        if opt == '5':
            chars += strippedchars

    return ''.join(random.choice(chars) for x in range(strLength))


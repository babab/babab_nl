# Copyright (c) 2013  Benjamin Althues <benjamin@babab.nl>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

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

# Copyright (C) 2012 Benjamin Althues
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

class Skin(object):
    active_skin = None
    skindict = { 1: 'Default',
                 2: 'Dark',
                 3: 'Ugly' }

    def __init__(self, request):
        self.active_skin = 1

        if request.GET:
            request.session['skin'] = request.GET['skin']

        try:
            skin = int(request.session['skin'])
        except (KeyError, ValueError):
            skin = 1

        if skin in range(1, 4):
            self.active_skin = skin

    def getActiveSkinName(self):
        return self.skindict[self.active_skin].lower()

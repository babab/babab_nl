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

from django import forms
from django.forms.widgets import CheckboxSelectMultiple

charOptions = (('1', 'Range a-z'),
               ('2', 'Range A-Z'),
               ('3', 'Range 0-9'),
               ('4', 'Special chars'),
               ('5', 'Include !,1,l,i,I,0,o,O'))

class strgenForm(forms.Form):
    number_of_chars = forms.IntegerField(min_value=2,max_value=108, initial=50)
    type_of_chars = forms.MultipleChoiceField(choices=charOptions,
            widget=CheckboxSelectMultiple, initial=[1,2,3,4])

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

from django.db import models

class NewsItem(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    time = models.DateTimeField()
    tag = models.ManyToManyField('NewsTag')

    def __unicode__(self):
        return self.title

class NewsTag(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

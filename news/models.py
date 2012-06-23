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

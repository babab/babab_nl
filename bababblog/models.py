from django.db import models


class Base(models.Model):
    '''Abstract base class'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Tag(Base):
    '''Tags for blog articles'''


class Comment(Base):
    '''Comments for blog articles'''
    email = models.EmailField()
    body = models.TextField()
    html = models.TextField()


class Article(models.Model):
    '''Blog articles'''
    title = models.CharField(max_length=80)
    url = models.SlugField(max_length=80)
    tags = models.ManyToManyField(Tag)
    body = models.TextField()
    html = models.TextField()

    def __str__(self):
        return self.url

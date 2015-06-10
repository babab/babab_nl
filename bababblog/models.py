from django.db import models


class Base(models.Model):
    '''Abstract base class'''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NamedBase(Base):
    '''Abstract base class with a name field'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Tag(NamedBase):
    '''Tags for blog articles'''


class Comment(NamedBase):
    '''Comments for blog articles'''
    email = models.EmailField()
    html = models.TextField()


class Article(Base):
    '''Blog articles'''
    title = models.CharField(max_length=80)
    url = models.SlugField(max_length=80)
    tags = models.ManyToManyField(Tag)
    html = models.TextField()

    def __str__(self):
        return self.url

    class Meta:
        get_latest_by = 'updated_at'

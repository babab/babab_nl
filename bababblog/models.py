from django.db import models


class Base(models.Model):
    '''Abstract base class'''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = 'updated_at'


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
    tags = models.ManyToManyField(Tag, blank=True)
    html = models.TextField()

    def __str__(self):
        return self.url


class Project(NamedBase):
    '''Projects'''
    language = models.CharField(blank=True, max_length=50)
    homepage = models.URLField(blank=True, null=True)
    description = models.CharField(blank=True, max_length=2048)
    ordering = models.SmallIntegerField(default=32767)
    html = models.TextField()
    json = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.ordering, self.name)

    # def save(self, *args, **kwargs):
    #     self.languageHash = str2hex(self.language)
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ['ordering', 'updated_at']

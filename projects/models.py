from django.db import models

class Base(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

class Project(Base):
    description = models.TextField()
    tags = models.ManyToManyField('ProjectTag')
    homepage = models.BooleanField()

class ProjectRelease(Base):
    project = models.ForeignKey(Project)
    date = models.DateField()

class ProjectTag(Base):
    pass

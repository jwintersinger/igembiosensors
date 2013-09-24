from django.db import models
from taggit.managers import TaggableManager

class Team(models.Model):
  name = models.CharField(max_length=100, unique=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name

class SensorInput(models.Model):
  name = models.CharField(max_length=100, unique=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name

class SensorOutput(models.Model):
  name = models.CharField(max_length=100, unique=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name

class Track(models.Model):
  name = models.CharField(max_length=100, unique=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name

class Application(models.Model):
  name = models.CharField(max_length=100, unique=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name

class CompetitionResult(models.Model):
  result = models.CharField(max_length=100, unique=True)

  class Meta:
    ordering = ['result']

  def __str__(self):
    return self.result

class Award(models.Model):
  name = models.CharField(max_length=100, unique=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name

class Project(models.Model):
  team = models.ForeignKey(Team)
  year = models.IntegerField()
  title = models.CharField(max_length=100)
  is_biosensor = models.BooleanField(
    default = True,
    verbose_name = 'Is biosensor',
    help_text = 'Is a biosensor according to Calgary/Paris Betterncourt definition.',
  )
  wiki_url = models.URLField(verbose_name = 'Wiki URL')
  category = models.ForeignKey(Category)
  abstract = models.TextField()
  inputs = models.ManyToManyField(SensorInput)
  outputs = models.ManyToManyField(SensorOutput)
  application = models.ForeignKey(Application)
  track = models.ForeignKey(Track, blank=True, null=True)
  results = models.ManyToManyField(CompetitionResult, blank=True)
  awards = models.ManyToManyField(Award, blank=True)
  tags = TaggableManager(blank=True)

  class Meta:
    ordering = ['-year', 'team__name']

  def __str__(self):
    return '%s %s' % (self.team, self.year)

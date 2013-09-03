from django.db import models
from taggit.managers import TaggableManager

class Team(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name

class SensorInput(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name

class SensorOutput(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name

class Track(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name

class Application(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name

class CompetitionResult(models.Model):
  result = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.result

class Project(models.Model):
  team = models.ForeignKey(Team)
  year = models.IntegerField()
  title = models.CharField(max_length=100)
  category = models.ForeignKey(Category)
  abstract = models.TextField()
  track = models.ForeignKey(Track)
  inputs = models.ManyToManyField(SensorInput)
  outputs = models.ManyToManyField(SensorOutput)
  application = models.ForeignKey(Application)
  results = models.ManyToManyField(CompetitionResult, blank=True)
  tags = TaggableManager(blank=True)

  def __str__(self):
    return '%s %s' % (self.team, self.year)

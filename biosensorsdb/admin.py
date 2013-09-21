import biosensorsdb.models
from django.contrib import admin
from django.db import models
from django.forms import SelectMultiple

class ProjectAdmin(admin.ModelAdmin):
  search_fields = [
   'team__name',
   'year',
   'title',
   'is_biosensor',
   'category__name',
   'abstract',
   'track__name',
   'inputs__name',
   'outputs__name',
   'application__name',
   'results__result',
   'awards__name',
   'tags__name',
  ]
  formfield_overrides = {
    models.ManyToManyField: {
      # Increase number of rows shown.
      'widget': SelectMultiple(attrs={'size': '15'}),
    }
  }

admin.site.register(biosensorsdb.models.Team)
admin.site.register(biosensorsdb.models.Category)
admin.site.register(biosensorsdb.models.SensorInput)
admin.site.register(biosensorsdb.models.SensorOutput)
admin.site.register(biosensorsdb.models.Track)
admin.site.register(biosensorsdb.models.Application)
admin.site.register(biosensorsdb.models.CompetitionResult)
admin.site.register(biosensorsdb.models.Award)
admin.site.register(biosensorsdb.models.Project, ProjectAdmin)

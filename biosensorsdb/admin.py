import biosensorsdb.models
from django.contrib import admin

admin.site.register(biosensorsdb.models.Team)
admin.site.register(biosensorsdb.models.SensorInput)
admin.site.register(biosensorsdb.models.SensorOutput)
admin.site.register(biosensorsdb.models.Track)
admin.site.register(biosensorsdb.models.Application)
admin.site.register(biosensorsdb.models.CompetitionResult)
admin.site.register(biosensorsdb.models.Project)

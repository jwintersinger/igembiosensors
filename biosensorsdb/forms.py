from django.forms import ModelForm
from biosensorsdb.models import Project
from django.forms import TextInput

class ProjectForm(ModelForm):
  class Meta:
    model = Project
    fields = [
      'team',
      'year',
      'title',
      'abstract',
      'track',
      'inputs',
      'outputs',
      'application',
      'results',
      'tags'
    ]
    widgets = {
      'abstract': TextInput()
    }

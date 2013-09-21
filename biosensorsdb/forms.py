from django import forms
from biosensorsdb.models import Project

NO_BIOSENSOR_PREF = '1'

class IsBiosensorSelect(forms.NullBooleanSelect):
  # Modified from http://stackoverflow.com/q/17398484/1691611.
  '''
  Customized to change 'Unknown' text label.
  '''
  def __init__(self, attrs=None):
    choices = (
      (NO_BIOSENSOR_PREF, 9*'-'),
      ('2',               'Yes'),
      ('3',               'No'),
    )
    super(forms.NullBooleanSelect, self).__init__(attrs, choices)

class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = [
      'team',
      'year',
      'title',
      'is_biosensor',
      'category',
      'abstract',
      'track',
      'inputs',
      'outputs',
      'application',
      'results',
      'awards',
      'tags',
    ]
    widgets = {
      # Use select widget rather than checkbox to enable not specifying a
      # choice, and for visual consistency with rest of form.
      'is_biosensor': IsBiosensorSelect(),

      # Don't want full textarea in filter form.
      'abstract': forms.TextInput(),
    }

from django.shortcuts import render
from biosensorsdb.forms import ProjectForm, NO_BIOSENSOR_PREF
from biosensorsdb.models import Project
from django.db.models import Q
from taggit.models import Tag
from django.views.decorators.clickjacking import xframe_options_exempt
import operator

@xframe_options_exempt
def index(request):
  form = ProjectForm(request.GET, label_suffix='')
  # Force form.cleaned_data to be created.
  form.is_valid()
  form_data = form.cleaned_data

  # Non-required types will appear in form.cleaned_data even when no value is
  # specified for them in the associated form. We must remove these, as they
  # otherwise mean we will *only* receive results with an empty value for the
  # field, rather than *all* results (regardless of that field's value), as the
  # user intended.
  for filter_type in ('track', 'results', 'awards', 'tags'):
    if not form_data[filter_type]:
      del form_data[filter_type]

  # Remove any fields from filter data not specified in request. (This is
  # necssary for is_biosensor boolean field, as this field is False regardless
  # of whether the user explicitly unchecked the corresponding checkbox, or
  # simply didn't specify a value in his request (e.g., on inital load, when
  # page isn't customized via "Filter biosensors" form).
  for field_name in form_data.keys():
    if field_name not in form.data.keys():
      del form_data[field_name]

  # When user does not specifically include or exclude proper biosensors,
  # display both.
  if 'is_biosensor' in form.data.keys() and \
    form.data['is_biosensor'] == '1':
    del form_data['is_biosensor']

  filter_types = {
    'team': 'exact',
    'year': 'exact',
    'title': 'icontains',
    'is_biosensor': 'exact',
    'category': 'exact',
    'abstract': 'icontains',
    'track': 'exact',
    'inputs': 'in',
    'outputs': 'in',
    'application': 'exact',
    'awards': 'exact',
    'results': 'in'
  }

  projects = Project.objects.all().order_by('-year', 'team__name')

  # Filter on all fields except tags.
  for filter_name, filter_type in filter_types.items():
    if filter_name not in form_data:
      continue
    kwargs = {'%s__%s' % (filter_name, filter_type): form_data[filter_name]}
    projects = projects.filter(**kwargs)

  # Filter on tags.
  # If no tags exist in DB, skip this operation -- otherwise, reduce() will
  # throw exception because one will be reducing empty set.
  if 'tags' in form_data and Tag.objects.count() > 0:
    tag_filters = []
    for tag in form_data['tags']:
      tag_filters.append(Q(name__icontains=tag))
    matching_tags = Tag.objects.filter(reduce(operator.or_, tag_filters))
    projects = projects.filter(tags__in=matching_tags)

  # If project has multiple tags matching what user provided in 'tags' filter,
  # that project will appear multiple times in result set.
  projects = projects.distinct()

  context = {
    'form': form,
    'projects': projects
  }
  return render(request, 'biosensorsdb/index.html', context)

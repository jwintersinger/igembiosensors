from django.shortcuts import render
from biosensorsdb.forms import ProjectForm
from biosensorsdb.models import Project
from django.db.models import Q
from taggit.models import Tag
import operator

def index(request):
  form = ProjectForm(request.GET, label_suffix='')
  # Force form.cleaned_data to be created.
  form.is_valid()
  form_data = form.cleaned_data

  # Non-required types with multiple potential values will appear in
  # form.cleaned_data as empty lists. We must remove these, as they otherwise
  # mean we will always receive an empty result set (as no element can be
  # within the empty list).
  for filter_type in ('results', 'tags'):
    if not form_data[filter_type]:
      del form_data[filter_type]

  filter_types = {
    'team': 'exact',
    'year': 'exact',
    'title': 'icontains',
    'category': 'exact',
    'abstract': 'icontains',
    'track': 'exact',
    'inputs': 'in',
    'outputs': 'in',
    'application': 'exact',
    'results': 'in'
  }

  projects = Project.objects.all()

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

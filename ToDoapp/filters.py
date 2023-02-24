from django_filters import rest_framework as filters

from .models import TODO, Project


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Project
        fields = ["name", "id"]


class TODOFilter(filters.FilterSet):
    # min_date = filters.DateTimeFilter(field_name="create", lookup_expr='gte', input_formats=['%Y-%m-%dT%H:%M'])
    # max_date = filters.DateTimeFilter(field_name="create", lookup_expr='lte', input_formats=['%Y-%m-%dT%H:%M'])
    create = filters.DateFromToRangeFilter()

    class Meta:
        model = TODO
        fields = ["project", "id", "create"]

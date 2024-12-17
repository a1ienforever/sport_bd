import django_filters
from .models import Athlete, Competition, Team


class AthleteFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains', label="Имя")
    last_name = django_filters.CharFilter(lookup_expr='icontains', label="Фамилия")
    team__name = django_filters.CharFilter(lookup_expr='icontains', label="Команда")

    class Meta:
        model = Athlete
        fields = ['first_name', 'last_name', 'team__name']


class CompetitionFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label="Название")
    location = django_filters.CharFilter(lookup_expr='icontains', label="Место проведения")

    class Meta:
        model = Competition
        fields = ['name', 'location']


class TeamFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label="Название")
    coach__first_name = django_filters.CharFilter(lookup_expr='icontains', label="Тренер")

    class Meta:
        model = Team
        fields = ['name', 'coach__first_name']



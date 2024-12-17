from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from sport_event.models import *
# Register your models here.
admin.site.register(Competition)
admin.site.register(Team)
admin.site.register(Achievement)
admin.site.register(Coach)
admin.site.register(Result)

class AthleteResource(resources.ModelResource):
    first_name = resources.Field(attribute='first_name', column_name='Имя')
    last_name = resources.Field(attribute='last_name', column_name='Фамилия')
    date_of_birth = resources.Field(attribute='date_of_birth', column_name='Дата рождения')
    team_name = resources.Field(attribute='team__name', column_name='Команда')
    sport_name = resources.Field(attribute='sport__name', column_name='Вид спорта')

    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'team_name', 'sport_name')
        export_order = ('id', 'first_name', 'last_name', 'date_of_birth', 'team_name', 'sport_name')

@admin.register(Athlete)
class AthleteAdmin(ImportExportModelAdmin):
    resource_class = AthleteResource
    list_display = ('first_name', 'last_name', 'team', 'sport')

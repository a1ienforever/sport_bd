from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from sport_event.models import Athlete, Team


class AddTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['num', 'name', 'price', 'note', 'photo']


class AddAthleteForm(ModelForm):
    team = forms.ModelChoiceField(queryset=Team.objects.all(), label='Модель', empty_label='Модель не выбрана')

    class Meta:
        model = Athlete
        fields = ['first_name', 'last_name', 'date_of_birth', 'team']


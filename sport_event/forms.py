from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from sport_event.models import Athlete, Team, Competition


class AddTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'city']


class AddAthleteForm(ModelForm):
    team = forms.ModelChoiceField(queryset=Team.objects.all(), label='Команда', empty_label='Выберите команду')

    class Meta:
        model = Athlete
        fields = ['first_name', 'last_name', 'date_of_birth', 'team']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class AddCompetitionForm(ModelForm):

    class Meta:
        model = Competition
        fields = ['name', 'location', 'date', 'teams']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

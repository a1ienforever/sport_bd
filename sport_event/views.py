from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .forms import AddAthleteForm, AddCompetitionForm
from .models import *

name_th = ["Название соревнования", "Место проведения", "Дата проведения"]
NAME_TH_ATHLETE = ['ФИО', 'Дата рождения', 'Команда']
NAME_TH_TEAM = ['Название', 'Город', 'Дата основания', 'Тренер']



class CompetitionHome(ListView):
    model = Competition
    template_name = "inventory_system/index.html"
    context_object_name = "competitions"
    extra_context = {
        "title": "Главная страница",
        "name_th": name_th,
    }

class CompetitionCreateView(CreateView):
    model = Competition
    form_class = AddCompetitionForm
    template_name = 'inventory_system/add-compet.html'
    success_url = reverse_lazy('')


class CompetitionPage(DetailView):
    model = Competition
    template_name = "inventory_system/competition.html"
    slug_url_kwarg = "competition_slug"
    context_object_name = "competition"
    extra_context = {"title": "Информация о карточке"}


class CreateTeam(CreateView):
    model = Team
    fields = ["name", "city"]
    template_name = "inventory_system/addproduct.html"
    success_url = reverse_lazy("")
    extra_context = {"title": "Добавление команды"}


class Teams(ListView):
    model = Team
    context_object_name = "teams"
    template_name = "inventory_system/teams.html"
    extra_context = {"title": "Список карточек", "name_th": NAME_TH_TEAM}


class TeamPage(DetailView):
    model = Team
    template_name = "inventory_system/team.html"
    slug_url_kwarg = "team_slug"
    context_object_name = "team"
    extra_context = {"title": "Информация о карточке"}


class CreateAthlete(CreateView):
    model = Athlete
    form_class = AddAthleteForm
    template_name = "inventory_system/newcard.html"
    success_url = reverse_lazy("")
    extra_context = {
        "title": "Добавление нового спортсмена",
    }


class AthletePage(DetailView):
    model = Athlete
    template_name = "inventory_system/athlete.html"
    slug_url_kwarg = "athlete_slug"
    context_object_name = "athletes"
    extra_context = {"title": "Информация о карточке"}


class Athletes(ListView):
    model = Athlete
    context_object_name = "athletes"
    template_name = "inventory_system/athletes.html"
    extra_context = {"title": "Список карточек", 'name_th': NAME_TH_ATHLETE}


def shipment(request):
    return HttpResponse("Product Shipment")

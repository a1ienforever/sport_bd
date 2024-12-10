from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import *

name_th = ["Название соревнования", "Место проведения", "Дата проведения"]


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
    fields = "__all__"
    template_name = 'inventory_system/add-compet.html'
    success_url = reverse_lazy('')


def date_filter(request):
    return HttpResponse("Hello world!")


class CreateAthlete(CreateView):
    model = Athlete
    fields = ['first_name', 'last_name', 'date_of_birth', 'team']
    template_name = "inventory_system/newcard.html"
    success_url = reverse_lazy("")
    extra_context = {
        "title": "Добавление нового спортсмена",
    }


class CreateTeam(CreateView):
    model = Team
    fields = ["name", "city"]
    template_name = "inventory_system/addproduct.html"
    success_url = reverse_lazy("")
    extra_context = {"title": "Добавление команды"}


class Teams(ListView):
    model = Team
    context_object_name = "cards"
    template_name = "inventory_system/cards.html"
    extra_context = {"title": "Список карточек"}


class AthletePage(DetailView):
    model = Athlete
    template_name = "inventory_system/card.html"
    slug_url_kwarg = "athlete_slug"
    context_object_name = "athlete"
    extra_context = {"title": "Информация о карточке"}


def shipment(request):
    return HttpResponse("Product Shipment")

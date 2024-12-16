from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import AddAthleteForm, AddCompetitionForm
from .models import *

name_th = ["Название соревнования", "Место проведения", "Дата проведения"]
NAME_TH_ATHLETE = ['ФИО', 'Дата рождения', 'Команда']
NAME_TH_TEAM = ['Название', 'Город', 'Дата основания', 'Тренер']
NAME_TH_SPORT = ['Название', 'Описание']
NAME_TH_COACH = ['Имя', 'Фамилия', 'Команда']


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


class DeleteCompetition(DeleteView):
    model = Competition
    template_name = "inventory_system/confirm_delete.html"  # Шаблон подтверждения удаления
    success_url = reverse_lazy("")


class CreateTeam(CreateView):
    model = Team
    fields = ["name", "city", 'sport']
    template_name = "inventory_system/add-team.html"
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


class DeleteTeam(DeleteView):
    model = Team
    template_name = "inventory_system/confirm_delete.html"  # Шаблон подтверждения удаления
    success_url = reverse_lazy("teams")


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
    context_object_name = "athlete"
    extra_context = {"title": "Информация о карточке"}


class Athletes(ListView):
    model = Athlete
    context_object_name = "athletes"
    template_name = "inventory_system/athletes.html"
    extra_context = {"title": "Список карточек", 'name_th': NAME_TH_ATHLETE}


class UpdateAthlete(UpdateView):
    model = Athlete
    context_object_name = "athlete"
    template_name = "inventory_system/update-athletes.html"
    fields = '__all__'  # Specify the fields to be updated
    extra_context = {"title": "Обновление"}
    success_url = reverse_lazy('athletes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context


class DeleteAthlete(DeleteView):
    model = Athlete
    template_name = "inventory_system/confirm_delete.html"  # Шаблон подтверждения удаления
    success_url = reverse_lazy("athletes")


class CreateSport(CreateView):
    model = Sport
    fields = ["name", 'description']
    template_name = "inventory_system/newsport.html"
    success_url = reverse_lazy("sports")
    extra_context = {
        "title": "Добавление нового вида спорта",
    }


class SportPage(DetailView):
    model = Sport
    template_name = "inventory_system/sport.html"
    slug_url_kwarg = "sport_slug"
    context_object_name = "sport"
    extra_context = {"title": "Информация о виде спорта"}


class Sports(ListView):
    model = Sport
    context_object_name = "sports"
    template_name = "inventory_system/sports.html"
    extra_context = {"title": "Список карточек", 'name_th': NAME_TH_SPORT}


class DeleteSport(DeleteView):
    model = Sport
    template_name = "inventory_system/confirm_delete.html"  # Шаблон подтверждения удаления
    success_url = reverse_lazy("sports")


class UpdateSport(UpdateView):
    model = Sport
    context_object_name = "sport"
    template_name = "inventory_system/update-sport.html"
    fields = '__all__'  # Specify the fields to be updated
    extra_context = {"title": "Обновление"}
    success_url = reverse_lazy('sports')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context


class CoachListView(ListView):
    model = Coach
    template_name = 'inventory_system/coach_list.html'  # Шаблон для отображения списка
    context_object_name = 'coaches'
    extra_context = {'title': 'Список тренеров', 'name_th': NAME_TH_COACH}


class CoachDetailView(DetailView):
    model = Coach
    template_name = 'inventory_system/coach_detail.html'  # Шаблон для отображения деталей
    slug_url_kwarg = "coach_slug"
    context_object_name = "coach"
    extra_context = {"title": "Информация о тренере"}

class CoachCreateView(CreateView):
    model = Coach
    template_name = 'inventory_system/coach_form.html'    # Шаблон для формы создания
    fields = ['first_name', 'last_name', 'team', 'sport']  # Поля для формы
    success_url = reverse_lazy('coach_list')  # Перенаправление после успешного создания


class CoachUpdateView(UpdateView):
    model = Coach
    template_name = 'inventory_system/coach_form.html'    # Тот же шаблон, что и для создания
    fields = ['first_name', 'last_name', 'team', 'sport']  # Поля для формы
    success_url = reverse_lazy('coach_list')  # Перенаправление после успешного обновления


class CoachDeleteView(DeleteView):
    model = Coach
    template_name = 'inventory_system/coach_confirm_delete.html'  # Шаблон для подтверждения удаления
    success_url = reverse_lazy('coach_list')

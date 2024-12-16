from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import UpdateAthlete, Sports, DeleteSport, UpdateSport, CreateSport, SportPage, DeleteAthlete, \
    DeleteCompetition, DeleteTeam, CoachListView, CoachDetailView, CoachCreateView, CoachUpdateView, CoachDeleteView

urlpatterns = [
    path("", login_required(views.CompetitionHome.as_view()), name=""),
    path("competition/", login_required(views.CompetitionCreateView.as_view()), name="add-competition"),
    path("competition/<slug:competition_slug>/", login_required(views.CompetitionPage.as_view()), name="competition"),
    path('competition/delete/<int:pk>/', DeleteCompetition.as_view(), name='delete_competition'),

    path("teams/", login_required(views.Teams.as_view()), name="teams"),
    path("addteam/", login_required(views.CreateTeam.as_view()), name="addproduct"),
    path("team/<slug:team_slug>/", login_required(views.TeamPage.as_view()), name="team"),
    path('team/delete/<int:pk>/', DeleteTeam.as_view(), name='delete_team'),

    path("addathlete/", login_required(views.CreateAthlete.as_view()), name="newcard"),
    path("athletes/<slug:athlete_slug>/", login_required(views.AthletePage.as_view()), name="athlete"),
    path("athletes/", login_required(views.Athletes.as_view()), name="athletes"),
    path('athletes/update/<int:pk>/', UpdateAthlete.as_view(), name='update_athlete'),
    path('athletes/delete/<int:pk>/', DeleteAthlete.as_view(), name='delete_athlete'),

    path('sports/', Sports.as_view(), name='sports'),
    path('sports/delete/<int:pk>/', DeleteSport.as_view(), name='delete_sport'),
    path('sports/update/<int:pk>/', UpdateSport.as_view(), name='update_sport'),
    path('sports/new/', CreateSport.as_view(), name='create_sport'),
    path('sports/<slug:sport_slug>/', SportPage.as_view(), name='sport_page'),

    path('coach/', CoachListView.as_view(), name='coach_list'),
    path('coach/<int:pk>/', CoachDetailView.as_view(), name='coach_detail'),
    path('coach/create/', CoachCreateView.as_view(), name='coach_create'),
    path('coach/<int:pk>/update/', CoachUpdateView.as_view(), name='coach_update'),
    path('coach/<int:pk>/delete/', CoachDeleteView.as_view(), name='coach_delete'),

]

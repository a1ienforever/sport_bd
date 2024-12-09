from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path("", login_required(views.CompetitionHome.as_view()), name=""),
    path("newcard/", login_required(views.CreateAthlete.as_view()), name="newcard"),
    path("addproduct/", login_required(views.CreateTeam.as_view()), name="addproduct"),
    path("shipment/", login_required(views.shipment), name="shipment"),
    path("cards/", login_required(views.Teams.as_view()), name="cards"),
    path("filter/", login_required(views.date_filter), name="date"),
    path("card/<slug:card_slug>/", login_required(views.AthletePage.as_view()), name="card"),
]

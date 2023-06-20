from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register),
    path("user_creation/", views.user_creation),
path("achievement_upload/", views.achievement_upload),
path("portfolio_creation/", views.portfolio_creation),
path("profile/", views.profile),
path("quniob/", views.quniob),
]
from rest_framework import routers
from django.urls import path

from mind_palace_back.account import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view())
]


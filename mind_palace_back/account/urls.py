from rest_framework import routers
from django.urls import path

from mind_palace_back.account import views


router = routers.DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('signup', views.SignUpView.as_view()),
    *router.urls
]


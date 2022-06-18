from rest_framework import routers
from django.urls import path

from mind_palace.user import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('signup/', views.SignUpView.as_view()),
    *router.urls
]


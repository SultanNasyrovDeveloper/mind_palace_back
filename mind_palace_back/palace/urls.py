from django.urls import include, path
from rest_framework import routers

from mind_palace_back.palace import views


router = routers.DefaultRouter()
router.register('palaces', views.UserMindPalaceViewSet)

urlpatterns = [
    path('node', include('mind_palace_back.palace.node.urls'))
]

urlpatterns = urlpatterns + router.urls

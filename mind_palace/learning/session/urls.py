from rest_framework.routers import DefaultRouter
from mind_palace.learning.session import views

router = DefaultRouter()
router.register('', views.LearningSessionViewSet)


urlpatterns = router.urls
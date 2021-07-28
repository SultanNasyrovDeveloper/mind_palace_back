from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/application/', include('mind_palace_back.application.urls')),
    path('api/v1/account/', include('mind_palace_back.account.urls')),
    path('api/v1/palace/', include('mind_palace_back.palace.node.urls')),
    path('api/v1/palace/', include('mind_palace_back.palace.urls')),
    path('api/v1/learning/sessions/', include('mind_palace_back.learning.session.urls')),
    path('api/v1/learning/statistics/', include('mind_palace_back.learning.stats.urls')),
    path('api/v1/learning/', include('mind_palace_back.learning.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
import accounts.views
import Challenges.views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('', accounts.views.login),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('challenges/', include('Challenges.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

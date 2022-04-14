from django.contrib import admin
from django.urls import path, include
from . import views
import accounts.views
import Challenges.views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('', accounts.views.login),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('challenges/', include('Challenges.urls')),
]

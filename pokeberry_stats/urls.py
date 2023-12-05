from django.contrib import admin
from django.urls import path
from stats_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('allBerryStats/', views.all_berry_stats, name='all_berry_stats'),
    path('histogram/', views.histogram, name='histogram'),
]

from django.contrib import admin
from django.urls import path
from maps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.searchbar, name='show'),
    path('explore/', views.explore, name='explore'),
    path('rec/', views.rec, name='rec'),
    path('', views.home, name='Home'),
]

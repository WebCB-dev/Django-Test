from django.urls import path, include
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('home/', views.home, name="home" ),
    
]

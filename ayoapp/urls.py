from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('my_experience', views.myexperience, name="experiencepage"),
]
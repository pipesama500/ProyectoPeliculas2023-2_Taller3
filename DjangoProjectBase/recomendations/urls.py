from django.urls import path,include
from . import views
app_name = "recomendations_app"
urlpatterns = [
    path('', views.recomendations_function, name='recomendations_function'),
]
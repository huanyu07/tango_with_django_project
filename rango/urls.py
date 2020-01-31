from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('about/',view.about, name = 'about')
=======
>>>>>>> e39a0b30f8c9dc99257d291087cdce302a6fa2e0
]

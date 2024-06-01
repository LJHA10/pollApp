from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    # Ruta principal para home (localhost:8000/poll/)
    path('', views.home, name='home'),
    # Ruta para votar en una pregunta específica (localhost:8000/poll/1/vote)
    path('<int:q_id>/vote/', views.vote, name='vote'),
    # Ruta para ver el resultado de una pregunta específica (localhost:8000/poll/1/result)
    path('<int:q_id>/result/', views.result, name='result'),
]

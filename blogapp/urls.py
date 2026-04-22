from django.urls import path
from blogapp import views
app_name = 'blogapp'

urlpatterns = [
    
    path('', views.accueil_view, name='accueil'),  
    path('connexion/', views.connexion_view, name='connexion'), 
    path('inscription/', views.inscription_view, name='inscription'),
    path('deconnexion/', views.deconnexion_view, name='deconnexion'),
] 

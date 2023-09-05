from django.urls import path
import poesias.views as views

urlpatterns = [
    path('', views.home_view),
    path('sobre', views.sobre_view),
    path('user/<str:username>', views.user_view),
   
]
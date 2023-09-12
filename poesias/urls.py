from django.urls import path
import poesias.views as views
from projeto import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view),
    path('sobre', views.sobre_view),
    path('user/<str:username>', views.user_view),
    path('contato', views.contato_view),
    path('blog', views.blog_view),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
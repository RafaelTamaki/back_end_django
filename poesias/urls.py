from django.urls import path
import poesias.views as views
from projeto import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home_view),
    path('sobre', views.sobre_view),
    path('blog', views.blog_view),

    path('poema_detail', views.poema_detail),
    path('page_extends', views.page_extends),
    path('poema_list', views.poema_list),

   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
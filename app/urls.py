

from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.show, name='show'),
    path('about', views.about, name='about'),
    path('help', views.help, name='help')
]

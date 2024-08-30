"""
URL configuration for filmesdpt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cinema import views
from cinema.views import duna
from cinema.views import menino
from cinema.views import todos
from cinema.views import bob
from cinema.views import dias
from cinema.views import emcartaz
from cinema.views import godzila
from cinema.views import login2
from cinema.views import kong
from cinema.views import trailer
from cinema.views import sala

urlpatterns = [
    path('sala/',views.sala, name='sala'),
    path('trailer/',views.trailer, name='trailer'),
    path('kong/',views.kong, name='kong'),
    path('emcartaz/',views.emcartaz, name='emcartaz'),
    path('login2/',views.login2, name='login2'),
    path('godzila/',views.godzila, name='godzila'),
    path('dias/',views.dias, name='dias'),
    path('bob/',views.bob, name='bob'),
    path('todos/',views.todos, name='todos'),
    path('menino/',views.menino, name='menino'),
    path('duna/',views.duna, name='duna'),
    path('',views.login,name='login'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('admin/', admin.site.urls),
    path('cinema/', include("cinema.urls", namespace="cinema")),
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

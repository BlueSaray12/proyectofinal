from django.urls import path
from . import views as coreViews

urlpatterns = [

    path('', coreViews.home, name="home"),
    path('menu/', coreViews.menu, name="menu"),
]

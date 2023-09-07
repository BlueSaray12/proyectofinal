from django.urls import path
from about import views as aboutViews

urlpatterns = [

    path('', aboutViews.about, name="about"),

]
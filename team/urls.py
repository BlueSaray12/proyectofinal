from django.urls import path
from team import views as teamViews

urlpatterns = [

       path('', teamViews.team, name="team"),

]
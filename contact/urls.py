from django.urls import path
from . import views as coreViews

urlpatterns = [

    path('contact/', coreViews.contact, name="contact"),

]

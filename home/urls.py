from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Udit??"
admin.site.site_title = "7 Cloud Kitchen"
admin.site.index_title = "Welcome to 7 Cloud Kitchen"

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("checkout1", views.checkout1, name='chcekout1'),
    path("checkout2", views.checkout2, name='checkout2')

]
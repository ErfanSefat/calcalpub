from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signOut/', views.signOut, name='signOut'),
    path('success/', views.success, name='success'),
    path('addevent/', views.addevent, name='addevent'),
    path('addschedule/', views.addschedule, name='addschedule'),

]
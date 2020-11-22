from django.urls import path
from .views import *

app_name = 'dashboard'
urlpatterns = [
    path('', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('update_profile/',update_profile_view,name='update_profile'),
    path('aboutus/',aboutus,name='aboutus'),
]

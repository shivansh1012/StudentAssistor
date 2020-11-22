from django.urls import path,include

from .views import *
app_name='social'
urlpatterns=[
	path('',index,name="home"),
	path('upload/',show_file,name="upload"),
	path('upload/<int:pk>/',delete_book,name="delete_book"),

]
from django.urls import path,include

from . import views
app_name='fileuploadapp'
urlpatterns=[
	path('',views.index,name="home"),
	path('upload/',views.show_file,name="upload"),
	path('upload/<int:pk>/', views.delete_book,name="delete_book"),

]
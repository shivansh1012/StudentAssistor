from django.urls import path

from .views import *

app_name = 'calendarapp'
urlpatterns = [
    path('', CalendarView.as_view(), name='calendar'),
    path('event/new/', create_event, name='event_new'),
    path('event/edit/<int:pk>/', EventEdit.as_view(), name='event_edit'),
    path('event/<int:event_id>/details/', event_details, name='event-detail'),
    path('add_eventmember/<int:event_id>', add_eventmember, name='add_eventmember'),
    path('event/<int:pk>/remove', EventMemberDeleteView.as_view(), name="remove_event"),
]
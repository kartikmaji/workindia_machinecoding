from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('user', views.registration, name='signup'),
    path('user/auth', views.login, name='login'),
    path('sites/list/', views.list_notes, name='list_notes'),
    path('sites', views.new_note, name='new_note'),
]
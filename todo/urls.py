from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('todo/', views.todo, name='todo'),
    path('toggle/<int:pk>/', views.toggle_todo, name='toggle_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('toggle/<int:pk>/', views.toggle_complete, name='toggle_complete'),

]

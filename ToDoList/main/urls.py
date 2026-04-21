from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('set_task_color/<int:pk>/', views.set_task_color, name='set_task_color'),
]
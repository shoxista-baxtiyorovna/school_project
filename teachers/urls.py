from django.urls import path
from . import views


app_name = 'teachers'

urlpatterns = [
    path('list/', views.teacher_list, name='teacher_list'),
    path('create/', views.teacher_form, name='teacher_form'),
    path('detail/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('delete/<int:teacher_id>/', views.teacher_delete, name='teacher_delete'),
]
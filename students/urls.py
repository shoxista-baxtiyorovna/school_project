from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('list/', views.student_list, name='student_list'),
    path('create/', views.student_form, name='student_form'),
    path('detail/<int:student_id>/', views.student_detail, name='student_detail'),
]
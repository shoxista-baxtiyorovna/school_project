from django.urls import path
from . import views


app_name = 'groups'

urlpatterns = [
    path('list/', views.group_list, name='group_list'),
    path('create/', views.group_form, name='group_form'),
    path('detail/<int:group_id>/', views.group_detail, name='group_detail'),
    path('delete/<int:group_id>/', views.group_delete, name='group_delete'),
]
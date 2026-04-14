from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_complaint, name='submit_complaint'),
    path('list/', views.complaint_list, name='complaint_list'),
    path('detail/<int:pk>/', views.complaint_detail, name='complaint_detail'),
    path('delete/<int:pk>/', views.delete_complaint, name='delete_complaint'),
    path('success/', views.success, name='success'),
]
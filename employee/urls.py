from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('form/', views.Form.as_view(), name='form'),
    path('update/<str:pk>', views.empUpdate, name='update'),
    path('delete/<str:pk>/', views.empDelete, name='delete'),

    path('position-list/', views.positonList, name="position-list"),
    path('position-update/<str:pk>/', views.positionUpdate, name='position-update'),
    path('position-delete/<str:pk>/', views.positionDelete, name='position-delete')
]

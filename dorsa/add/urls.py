from django.urls import path
from . import views

app_name = 'add'
urlpatterns = [
    path('sum/', views.Add.as_view(), name='Add'),
    path('history/', views.History.as_view(), name='Add'),
    path('total/', views.TotalValues.as_view(), name='Add'),
]

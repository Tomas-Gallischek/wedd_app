from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),       
    path('zenich/', views.on_view, name='on'),    
    path('nevesta/', views.ona_view, name='ona'),
]
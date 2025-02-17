from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('analyze_layout_all/', views.analyze_layout_all, name='analyze_layout_all'),
    path('analyze-layout/', views.analyze_layout, name='analyze_layout'),
    path('send_message/', views.send_message, name='send_message'),
    path('inspect/<str:code>/', views.InspectItem.as_view(), name='inspect'),
]
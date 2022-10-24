from . import views
from django.urls import path

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('api/', views.GetLinkApi.as_view()),
    path('<str:user_link>/', views.main_page, name='main_page'),
]


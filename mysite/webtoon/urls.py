from django.urls import path

from . import views


urlpatterns = [
    path('', views.webtoon_list, name='list'),
    path('<int:pk>/', views.webtoon_detail, name='detail'),

]
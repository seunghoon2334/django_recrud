from django.urls import path, include
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'), #boards/
    path('new/', views.new, name='new'), #boards/new
    # path('create/', views.create, name='create'),
    path('<int:board_pk>/', views.detail, name='detail'),
    path('<int:board_pk>/edit/', views.edit, name='edit'),
    # path('<int:board_pk>/update/', views.update, name='update'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/comments/', views.comment_create, name='comment_create'),
]

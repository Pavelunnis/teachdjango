from django.urls import path, re_path
from .import views

urlpatterns = [
    re_path(r'^contact/', views.contact),
    re_path(r'^about', views.about),
    path('products/', views.products), #маршрут по умолчанию
    path('products/<int:productid>/', views.products),
    path('users/', views.users), #маршрут по умолчанию
    path('users/<int:id>/<str:name>/', views.users),
    path('details/', views.details),
    path('access/<int:age>', views.access),
    path('', views.index),
]
from django.contrib import admin
from django.urls import path, include
from .api_views import *

app_name = 'main_store'
urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/create/', ProductCreate.as_view()),
    path('products/<int:id>/', ProductRetrieveUpdateDestroy.as_view()),
    path('products/<int:id>/stats/', ProductStats.as_view()),
]

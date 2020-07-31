from django.urls import path
from .views import index, CategoryPage

app_name = 'videos'
urlpatterns = [
    path('', index, name="index"),
    path('<slug:slug>', CategoryPage.as_view(), name="property_detail"),
]
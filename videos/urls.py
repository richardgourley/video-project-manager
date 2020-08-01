from django.urls import path
from .views import index, CategoryPage, ProjectDetail

app_name = 'videos'
urlpatterns = [
    path('', index, name="index"),
    path('<slug:slug>', CategoryPage.as_view(), name="category_page"),
    path('video/<int:pk>', ProjectDetail.as_view(), name="project_detail"),
]
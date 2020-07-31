from django.shortcuts import render
from .models import Category

# Create your views here.
def index(request):
	categories = Category.objects.all()
	return render(request, 'videos/index.html', {'categories':categories})
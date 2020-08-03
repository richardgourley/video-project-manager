from .models import Category

def category_renderer(request):
	return{
	    'categories': Category.objects.all()
	}
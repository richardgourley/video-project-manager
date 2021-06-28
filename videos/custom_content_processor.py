from .models import Category

# Gets all category objects - available in homepage
def category_renderer(request):
	return{
	    'categories': Category.objects.all()
	}
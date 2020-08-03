from django.shortcuts import render
from .models import Category, Project, Testimonial
from django.views import generic

# Create your views here.
def index(request):
    testimonials = Testimonial.objects.all()[:5]
    return render(request, 'videos/index.html', {'testimonials':testimonials})

class CategoryPage(generic.DetailView):
    model = Category
    template_name = 'videos/category-page.html'

    def get_queryset(self):
        return Category.objects.all()

class ProjectDetail(generic.DetailView):
	model = Project
	template_name = 'videos/project-detail.html'

	def get_queryset(self):
		return Project.objects.all()


        
        


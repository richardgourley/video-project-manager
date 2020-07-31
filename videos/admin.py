from django.contrib import admin
from .models import Category, Project, Testimonial

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['name', 'display_order', 'placement', 'category']
	list_filter = ['category']

	def display_order(self, obj):
		return obj.order

	display_order.short_description = 'ORDER (Lowest number appears first on pages)'

class TestimonialAdmin(admin.ModelAdmin):
	list_display = ['client_name', 'category']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Testimonial, TestimonialAdmin)

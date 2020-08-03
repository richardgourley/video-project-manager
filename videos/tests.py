from django.test import TestCase, Client
from django.urls import reverse

from .models import Project, Category, Testimonial

# Create your tests here.
'''
FUNCTIONS THAT CREATE OBJECT INSTANCES FOR TESTING
'''
def create_project(name, project_image, video_code, order, category, placement):
    return Project.objects.create(
        name=name, 
        project_image = project_image,
        video_code = video_code,
        order = order,
        category = category,
        placement = placement
    )

def create_category(name, homepage_image, homepage_text, category_page_text, slug):
    return Category.objects.create(
        name = name,
        homepage_image = homepage_image,
        homepage_text = homepage_text,
        category_page_text = category_page_text,
        slug = slug
    )

def create_testimonial(client_name, comment, category):
    return Testimonial.objects.create(
        client_name = client_name,
        comment = comment,
        category = category
    )



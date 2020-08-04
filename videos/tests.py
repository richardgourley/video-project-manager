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

'''
VIEW TESTS
'''

class IndexTests(TestCase):
    def setup(self):
        self.client = Client

    def test_index_returns_200(self):
        response = self.client.get(reverse('videos:index'))
        self.assertEqual(response.status_code, 200)

    def test_categories_appear_in_navmenu(self):
        category1 = create_category("wedding", "image1.jpg", "home text", "category text", "wedding")
        project1 = create_project("Wedding1", "image2.jpg", 69789, 1, category1, "c")
        response = self.client.get(reverse('videos:index'))
        self.assertIn("<a class=\"dropdown-item\" href=\"/wedding\">wedding</a>", str(response.content))

class CategoryPageTests(TestCase):
    def setup(self):
        self.client = Client

    def test_category_page_returns_200(self):
        category1 = create_category("wedding", "image1.jpg", "home text", "category text", "wedding")
        project1 = create_project("Wedding1", "image2.jpg", 69789, 1, category1, "c")
        response = self.client.get(reverse('videos:category_page', args=(category1.slug,)))
        self.assertEqual(response.status_code, 200)

    def test_categories_appear_in_navmenu(self):
        category1 = create_category("wedding", "image1.jpg", "home text", "category text", "wedding")
        project1 = create_project("Wedding1", "image2.jpg", 69789, 1, category1, "c")
        response = self.client.get(reverse('videos:category_page', args=(category1.slug,)))
        self.assertIn("<a class=\"dropdown-item\" href=\"/wedding\">wedding</a>", str(response.content))

    def test_projects_appear_lowest_order_first(self):
        category1 = create_category("wedding", "image1.jpg", "home text", "category text", "wedding")
        project1 = create_project("Wedding1", "image2.jpg", 69789, 2, category1, "c")
        project2 = create_project("Wedding2", "image3.jpg", 78958, 1, category1, "c")
        response = self.client.get(reverse('videos:category_page', args=(category1.slug,)))
        projects = response.context['category'].get_projects_category_page()
        # We expect project2 to appear first in 'category.get_projects_category_page'
        self.assertEqual('Wedding2', projects[0].name)

class ProjectDetailTests(TestCase):
    def setup(self):
        self.client = Client

    def test_property_detail_returns_200(self):
        category1 = create_category("wedding", "image1.jpg", "home text", "category text", "wedding")
        project1 = create_project("Wedding1", "image2.jpg", 69789, 2, category1, "c")
        response = self.client.get(reverse("videos:project_detail", args=(project1.id,)))
        self.assertEqual(response.status_code, 200)

    def test_property_detail_returns_404_with_incorrect_id(self):
        response = self.client.get(reverse("videos:project_detail", args=("18",)))
        self.assertEqual(response.status_code, 404)



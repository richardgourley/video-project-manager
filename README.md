# Video Project Website Manager - Django
This is a management system for a video production company. 

The site admin can enter details for each category including an image, homepage text and text to appear on the individual category page.  The admin can then enter projects which have an image to appear in a grid on the home page and each individual category page.

The admin can choose which projects, the order of the projects and how many projects appear under each category on the homepage and each individual category page.

The site is setup so that when the admin creates a new category, the menu, homepage and category page are all created dynamically.  Testimonials can also be added to each category - 5 latest are displayed on homepage.

## MODELS AND FIELDS
- Category - name, homepage image, homepage text, category page text (can be more detailed than home page), slug (used in dynamic creation of urls)
- Project - name, image (used in grid display to click through to see each project), category (foreign field), placement ('h','c') (home/category page)
- Testimonial - client name, comment, category (foreign key)

## SITE ADMIN
- Category - can add image for the homepage, text for homepage (shorter), longer text for each category page.
- Project - name, image and category
          - admin can choose if each project appears on home page, category page or both.
          - admin can choose the order each video is to appear on homepage, category page or both.
- Testimonial - can add client names, comments and assign to a category

## SITE PAGES
- index - displays category info, an image and clickable grid of projects.
- category-page - template for displaying text and the selected and ordered projects for each category.
- project detail - simple template that displays the video via the embedded video code.
- header, footer, navbar - using custom content processors - all categories are available for navbar and footer menus.

## TESTING
- Tests categories appear in navbar menus correctly
- Tests projects are returned on correct page with model placemenent option
- Tests ordering of projects returns correct order on pages.
- Tests 200 for all pages
- Tests video_code appears for project detail page

## SKILLS REFERENCE
VIEWS
- Generic classes for views - ListView, DisplayView

MODELS
- Foreign keys
- FileField
- SlugField
- Class Meta - Verbose names
- Defining __str__ creating human readable names for admin.
- Help text on fields
- Bespoke functions used on Category

ADMIN
- list_display to configure display of items in list view of each object
- list filter - allows filtering of large numbers of objects
- short_description - adds more specific details

CUSTOM CONTENT PROCESSORS
- Used to make categories available in every template - for dynamic menus.
- python decouple used in hidden file for project information - see settings

# Video Project Website Manager - Django

## Intro
A website written in Django which allows a video production company to manage and showcase their work.

The site admin can create categories, video projects and testimonials and has full control over which projects appear where on the site.

## Features

- The admin can create video projects, each containing a video and a featured image.
- The admin can create categories for their videos.
- The admin can decide whether each video appears on the home page, the category page or both.
- The site is setup to create category pages and video pages automatically.
- Category pages dynamically appear in the website menu.
- For the home page, the admin can create an intro text and add an image for each category which is displayed on the home page with a view more link to explore more videos in each category.
- Testimonials - the site admin can create testimonials from customers and assign the testimonial to a project and category.

## TOOLS/ SKILLS REFERENCE
Written in pure Django.  For students of Django here are some of the tools/ skills covered in the project.

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

TESTING
- Tests categories appear in navbar menus correctly
- Tests projects are returned on correct page with model placemenent option
- Tests ordering of projects returns correct order on pages.
- Tests 200 http response for all pages.
- Tests video_code appears for project detail page


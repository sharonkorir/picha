from email.mime import image
from unicodedata import name
from django.test import TestCase
from .models import location, category, Image

# Create your tests here.

class ImageTestClass(TestCase):

    '''
    Test class that defines test cases for the image class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        # Creating a new category and saving it
        self.new_category = category(name = 'test category')
        self.new_category.save()

        # Creating a new location and saving it
        self.new_location = location(name = 'test location')
        self.new_location.save()

        self.new_image= Image(name = 'Test Image',description = 'This is a random test image', image = 'random.jpg')
        self.new_image.save()

        self.new_image.category.add(self.new_category)

        self.new_image.location.add(self.new_location)

    def tearDown(self):
        location.objects.all().delete()
        category.objects.all().delete()
        Image.objects.all().delete()
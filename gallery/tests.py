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

        # Creating a new image and saving it
        self.new_image= Image(name = 'Test Image',description = 'This is a random test image', image = 'random.jpg', category=self.new_category,location=self.new_location)
        self.new_image.save()

        

    def tearDown(self):
        location.objects.all().delete()
        category.objects.all().delete()
        Image.objects.all().delete()

    def test_get_all_images(self):
        all_images = Image.get_images()
        self.assertTrue(len(all_images)>0)

    def test_filter_by_location(self):
        test_location = 'test_location'
        image_by_location = Image.location_filter(test_location)
        self.assertTrue(len(image_by_location) > 0)

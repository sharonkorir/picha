from django.test import TestCase
from .models import Owner, location, category, Image

# Create your tests here.

class OwnerTestClass(TestCase):

    '''
    Test class that defines test cases for the owner class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Set up method
    def setUp(self):
        self.sharon= Owner(first_name = 'Sharon', last_name ='Korir')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sharon,Owner))
    
    # Testing Save Method
    def test_save_method(self):
        self.sharon.save_owner()
        owners = Owner.objects.all()
        self.assertTrue(len(owners) > 0)
from unicodedata import name
from django.db import models

# Create your models here.

class location(models.Model):
    '''
    location model acts as blueprint for all location instances
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class category(models.Model):
    '''
    category model acts as blueprint for all category instances
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    '''
    Image model acts as blueprint for all image instances
    '''
    name = models.CharField(max_length =60)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/',default='no image')
    #owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING, null=True)
    category = models.ForeignKey(category, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(location, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_image(self):
        self.save()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def location_filter(cls,location):
        location = Image.location
        images = cls.objects.filter(location = location)
        return images

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images

    

    
    

from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class location(models.Model):
    '''
    location model acts as blueprint for all location instances
    '''
    name = models.CharField(max_length =30)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name

    @classmethod
    def get_location_by_id(cls, id):
        location = cls.objects.filter(id = id)
        return location

    @classmethod
    def delete_location(cls, id):
        location = cls.get_location_by_id(id).delete()

    @classmethod
    def update_location(cls,id):
        location = cls.get_location_by_id(id).update()
        return location

class category(models.Model):
    '''
    category model acts as blueprint for all category instances
    '''
    name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.name

    @classmethod
    def get_category_by_id(cls, id):
        category = cls.objects.filter(id = id)
        return category

    @classmethod
    def delete_category(cls, id):
        category = cls.get_category_by_id(id).delete()

    @classmethod
    def update_category(cls,id):
        category = cls.get_category_by_id(id).update()
        return category

class Image(models.Model):
    '''
    Image model acts as blueprint for all image instances
    '''
    name = models.CharField(max_length =60)
    description = models.TextField()
    image = CloudinaryField('image')
    #image = models.ImageField(upload_to = 'images/',default='no image')
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
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id = id)
        return image

    @classmethod
    def delete_images(cls, id):
        image = cls.get_image_by_id(id).delete()

    @classmethod
    def update_image(cls,id):
        image = cls.get_image_by_id(id).update()
        return image

    @classmethod
    def location_filter(cls,location):
       
        images = cls.objects.filter(location__name__icontains=location)
        return images

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images

    

    
    
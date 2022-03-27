from django.db import models

# Create your models here.
class Owner(models.Model):
    '''
    Owner model to manage photos on admin dashboard
    '''
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    #email = models.EmailField()

    def __str__(self):
        return self.first_name

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
    #image = models.ImageField()
    editor = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(category, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(location, on_delete=models.DO_NOTHING)
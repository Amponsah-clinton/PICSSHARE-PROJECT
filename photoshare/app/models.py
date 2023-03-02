from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(null=False, blank=False)

    
    def __str__(self):
        return self.category.name
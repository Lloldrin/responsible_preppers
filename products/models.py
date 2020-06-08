from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=256)
    friendly_name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=256, null=True, blank=True)
    name = models.CharField(max_length=256)
    img_url = models.URLField(max_length=1024, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    img_url_2 = models.URLField(max_length=1024, null=True, blank=True)
    img_2 = models.ImageField(null=True, blank=True)
    img_url_3 = models.URLField(max_length=1024, null=True, blank=True)
    img_3 = models.ImageField(null=True, blank=True)
    img_url_4 = models.URLField(max_length=1024, null=True, blank=True)
    img_4 = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    key_point_1 = models.CharField(max_length=256, null=True, blank=True)
    key_point_2 = models.CharField(max_length=256, null=True, blank=True)
    key_point_3 = models.CharField(max_length=256, null=True, blank=True)
    key_point_4 = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
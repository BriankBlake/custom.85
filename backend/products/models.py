from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)

    class Meta:

        verbose_name_plural = 'categories'

    def __str__(self):

        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default='un-branded')

    desciption = models.TextField(blank=True)

    slug = models.SlugField(max_length=255)

    price = models.DecimalField(max_digits=8, decimal_places=4)

    image = models.ImageField(upload_to='images/')

    countInStock = models.IntegerField(null=True, blank=True, default=0)


    class Meta:

        verbose_name_plural = 'products'

    def __str__(self):

        return self.title

















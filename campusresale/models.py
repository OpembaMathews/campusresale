from django.db import models
from django.urls import reverse
# from django.core.urlresolvers import reverse
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length = 200, db_index = True )
    slug = models.SlugField (max_length = 200, db_index = True, unique = True )

    def __str__(self):
        return self.name

    # @models.permalink
    def get_absolute_url(self):
        return reverse ('campusresale: product_list_by_category', args = [self.slug] )

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'products', on_delete=models.CASCADE )
    name = models.CharField( max_length = 200, db_index = True )
    slug = models.SlugField (max_length = 200, db_index = True, unique = True )
    image = models.ImageField( upload_to = 'img/%Y/%m/%d/', blank = True )
    description = models.TextField( blank = True )
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField( default = True )
    created = models.DateTimeField( auto_now_add = True )
    updated = models.DateTimeField( auto_now_add = True )


    class Meta:
        ordering = ['name']
        index_together = (('id', 'slug'),)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse( 'shop:product_detail',
                        args=[self.id, self.slug] )

        

from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    


class tutors(models.Model):
    category = models.ForeignKey(Category, related_name='tutors', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    Tagline = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images=models.ImageField(upload_to="media")
  

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('onlinetutors:tutor_detail', args=[self.id, self.slug])
    


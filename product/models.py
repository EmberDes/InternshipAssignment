from django.db import models

# Create your models here.
class Product(models.Model):
    name  = models.CharField(max_length=80)
    code = models.IntegerField(max_length=30, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
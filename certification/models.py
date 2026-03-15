from django.db import models

# Create your models here.
class Certification(models.Model):
    name = models.CharField(max_length=80)
    code = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
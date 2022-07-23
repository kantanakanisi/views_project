from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    class Meta:
        db_table = 'items'

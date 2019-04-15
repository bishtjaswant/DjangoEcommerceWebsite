from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_decription = models.TextField(max_length=500)
    image = models.ImageField(upload_to="shop/images", default="")
    category =  models.CharField(max_length=50, default="")
    subcategory =  models.CharField(max_length=50, default="")
    price =  models.IntegerField(default=0)
    product_date = models.DateTimeField()


    def __str__(self):
        return self.product_name
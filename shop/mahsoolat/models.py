from django.db import models

# Create your models here.
class mahsoolat(models.Model):
    title =models.CharField(max_length=60)
    description =models.TextField()
    PRODUCT_TYPES = [
    ("phone", "گوشی"),
    ("tablet", "تبلت"),
    ("console", "کنسول"),
    ("laptop", "لپتاپ"),
    ("accessory", "لوازم جانبی"),
]

    product_type = models.CharField(max_length=20 , choices=PRODUCT_TYPES , default="phone")
    
    
    
    Reagen = models.CharField(max_length=10,default="usa")
    Rom = models.IntegerField(default="0")

    price=models.BigIntegerField(default=0)
    offer =models.IntegerField()
    hafezeh=models.CharField(max_length=7,default="0")
    image=models.ImageField(null=True,upload_to="products_img")
    video = models.FileField(null=True,upload_to="Media/videos")
    
    def __str__(self):
        return self.title
        
    
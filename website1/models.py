from django.db import models

# Create your models here.
class Records(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=10)
    last_name =models.CharField(max_length=10)
    email =models.CharField(max_length=254)
    phone =models.CharField(max_length=10)
    address =models.CharField(max_length=50)
    city =models.CharField(max_length=100)
    state=models.CharField(max_length=10)
    zipcode=models.CharField(max_length=10)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
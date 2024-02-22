from django.db import models




class  PRODUCT(models.Model):

    name=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    productid=models.CharField(max_length=200)
    

    




class CART(models.Model):
    user_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    productid=models.CharField(max_length=200)

    def __str__(self):
        return "usercart"
    # product=models.ManyToManyField(PRODUCT)
    




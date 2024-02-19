from django.db import models




class  PRODUCT(models.Model):

    name:models.CharField()
    image:models.CharField()
    price:models.CharField()
    id_:models.CharField()
    

    




class CART(models.Model):
    user_id:models.CharField()
    product:models.ManyToManyField(PRODUCT)
    




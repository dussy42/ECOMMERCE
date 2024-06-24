from django.db import models









class CHECKOUT(models.Model):
    app_label = 'checkout'
    user_id=models.CharField(max_length=200)
    # name=models.CharField(max_length=200)
    # image=models.CharField(max_length=200)
    # price=models.IntegerField(null)
    productId=models.IntegerField()
    quantity=models.IntegerField()

    def __str__(self):
        return "usercart"
    # product=models.ManyToManyField(PRODUCT)
    




from django.shortcuts import render ,redirect
from django.conf import settings
from .models import CHECKOUT
from .serialisers import cartser
from django.http import HttpResponse

 

def cart (req):
  item = []
  if(req.user.is_authenticated):
    v = CHECKOUT.objects.get(user_id = req.user.username)
    if(v):
      item_ = cartser(v,many=True)
      item = [{**_["product"] , **_} for _ in item_]
    # for val in item_:


    # data =  resser(res,many=True)
  
  return   render(req,"cart.html",{"item":item})
def addtocart (req):

  li = req.body
  for val in li:
    cart = CHECKOUT.objects.get(userId =req.user.username,productId=val.productId)
  
    if(cart):
      cart.quantity = val.quantity
      cart.save()
    else:
     cart = CHECKOUT.objects.create(userId =req.user.username,productId=val.productId)

    #  cart.product.add()
    #  cart.save()

  
  
  return   HttpResponse(200)


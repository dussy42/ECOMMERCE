import json
from django.shortcuts import render ,redirect
from django.conf import settings
from .models import CHECKOUT
from .serialisers import cartser
from django.http import HttpResponse, QueryDict
from django.conf import settings
from rest_framework.decorators import api_view

def findObj(id):
 print("ccc")
 c = [_  for _ in settings.JSONFOOD if _["id"] == f"{id}"]
 b = c[0]if len(c) >=1 else {}
 print(b,"ccc",id)
 return b

def cart (req):
  item = []
  if(req.user.is_authenticated):
    v = CHECKOUT.objects.filter(user_id = req.user.username)
    if(v):
      item_ = cartser(v,many=True)
      print(item_.data)
      item = [{**findObj(dict(_)["productId"]) , **_} for _ in item_.data]
    # for val in item_:


    # data =  resser(res,many=True)
  
  return   render(req,"cart.html",{"item":item})
# @api_view(["post"])
def addtocart (req):
  decoded_data = req.body.decode('utf-8')
  li = json.loads(decoded_data)
  

  print(li)
  for val in li:
    cart = CHECKOUT.objects.get_or_create(user_id =req.user.username,productId=val["id"],
                                          
                                          defaults={
                                            "quantity":val["quantity"]
                                          }
                                          )
  
   

    #  cart.product.add()
    #  cart.save()

  
  
  return   HttpResponse(200)


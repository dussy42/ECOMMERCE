from django.shortcuts import render ,redirect
from django.conf import settings
# from .models import CART ,PRODUCT

 

def index (req):
  if(req.user):
    print(req.user)
  return   render(req,"index.html")
def product (req,id):
  item_=None
  for index, item in enumerate(settings.JSONFOOD):
    if item["id"].strip() ==  id.strip():
         item_ = item
         break
  # JSONFOOD.fin
  print(id,item_)
  # return   render(req,"productlist.html",{"data":settings.JSONFOOD})
  return   render(req,"product.html",{"item":item_})
  # return   render(req,"product.html")
def cart (req):
  
  return   render(req,"cart.html")
# def addtocart (req):
#   product = PRODUCT.object.get(productid =req.body.id)
#   cart = CART.object.get(user_id =req.user.id)
#   if not cart:
#     cart = CART.object.create(user_id =req.user.id)
  
  
#   return   render(req,"cart.html")
def productlist (req):
  return   render(req,"productlist.html",{"data":settings.JSONFOOD})




from django.shortcuts import render ,redirect
from django.conf import settings


from django.http import HttpResponse

 


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
def productlist (req):
  return   render(req,"productlist.html",{"data":settings.JSONFOOD})




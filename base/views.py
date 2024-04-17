from django.shortcuts import render ,redirect
from django.conf import settings
from .models import CART ,PRODUCT
from .serialisers import cartser
from django.http import HttpResponse

 

def index (req):
  if(req.user):
    print(req.user)
  return   render(req,"index.html")



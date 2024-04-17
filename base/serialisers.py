from .models import CART
from rest_framework.serializers import  ModelSerializer
class cartser (ModelSerializer):
     class Meta:
        model = CART
        fields = '__all__'

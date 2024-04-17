from .models import CHECKOUT
from rest_framework.serializers import  ModelSerializer
class cartser (ModelSerializer):
     class Meta:
        model = CHECKOUT
        fields = '__all__'

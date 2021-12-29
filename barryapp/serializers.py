from django.db import models
from django.db.models import fields
from rest_framework import serializers
from barryapp.models import Beginnerpay

class BeginnerpaySerializers(serializers.ModelSerializer):
    class Meta:
        model=Beginnerpay
        fields=('name','email','phone','address','payment_id','paid')
        

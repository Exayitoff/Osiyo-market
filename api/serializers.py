from rest_framework import serializers
from home.models import *

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('name','slug')

class ElektronikaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Elektronika
    fields = ('name','price','image','about')


class SigaretSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sigaret
    fields = ('name','price','image','about')


class PishiriqlarSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sigaret
    fields = ('name','price','image','about')
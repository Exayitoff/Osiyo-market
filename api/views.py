from rest_framework.generics import ListAPIView
from home.models import *
from .serializers import *


class CategoryAPIView(ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class ElektronikaAPIView(ListAPIView):
  queryset = Elektronika.objects.all()
  serializer_class = ElektronikaSerializer

class ShirinlikAPIView(ListAPIView):
  queryset = Pishiriqlar.objects.all()
  serializer_class = PishiriqlarSerializer

class SigaraAPIView(ListAPIView):
  queryset = Sigaret.objects.all()
  serializer_class = SigaretSerializer
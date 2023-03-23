from django.urls import path
from .views import *

urlpatterns = [
    path('kategoriya/', CategoryAPIView.as_view()),
    path('elektronika/', ElektronikaAPIView.as_view()),
    path('sigaret/', SigaraAPIView.as_view()),
    path('shirinlik/', ShirinlikAPIView.as_view()),
]


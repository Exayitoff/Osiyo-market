from django.urls import path
from .views import (
                    home,
                    electronic,
                    sigaret,
                    pishiriq
                    ) 

urlpatterns = [
    path('', home , name='home' ),
    path('elektronika', electronic , name='elektronika' ),
    path('sigaret', sigaret , name='sigara' ),
    path('pecheniye', pishiriq , name='pechenye' ),
]

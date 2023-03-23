from django.shortcuts import render
from .models import *
def home(requests):
  ctg = Category.objects.all()
  pechi = Pishiriqlar.objects.all()
  elek = Elektronika.objects.all()
  sig = Sigaret.objects.all()
  slide = Slayder.objects.all()
  ctx = {
    'ctg': ctg,
    'pechi': pechi[len(pechi)-3:],
    'pechi2': pechi[len(pechi)-6:len(pechi)-3],
    'pechi3': pechi[len(pechi)-9:len(pechi)-6],
    'elektronika': elek[len(elek)-3:],
    'elektronika2': elek[len(elek)-6:len(elek)-3],
    'elektronika3': elek[len(elek)-9:len(elek)-6],
    'sig': sig[len(sig)-3:],
    'sig2': sig[len(sig)-6:len(sig)-3],
    'sig3': sig[len(sig)-9:len(sig)-6],
    'slider': slide,
  }
  return render(requests, 'blog/index.html', ctx)

def electronic(requests):
  ctx = {}
  return render(requests, 'blog/elec.html', ctx)
def sigaret(requests):
  ctx = {}
  return render(requests, 'blog/fashion.html', ctx)
def pishiriq(requests):
  ctx = {}
  return render(requests, 'blog/jewel.html', ctx)
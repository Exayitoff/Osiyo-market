from django.db import models
from django.utils.text import slugify

class Category(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField(unique=True, blank=True)
  class Meta:
    verbose_name_plural = 'Kategoriya'


  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super(Category, self).save(*args, **kwargs)
  def __str__(self) -> str:
    return self.name

class Elektronika(models.Model):
  name = models.CharField(max_length=255)
  price = models.PositiveIntegerField(verbose_name='Narxi')
  image = models.ImageField(upload_to='rasmlar/', verbose_name='Rasmi')
  about = models.TextField(verbose_name="Ma\'lumot")

  class Meta:
    verbose_name_plural = 'Elektronika'
  def __str__(self) -> str:
    return self.name


class Sigaret(models.Model):
  name = models.CharField(max_length=255)
  price = models.PositiveIntegerField(verbose_name='Narxi')
  image = models.ImageField(upload_to='rasmlar/', verbose_name='Rasmi')
  about = models.TextField(verbose_name="Ma\'lumot")

  class Meta:
    verbose_name_plural = 'Sigaret'
  def __str__(self) -> str:
    return self.name

class Pishiriqlar(models.Model):
  name = models.CharField(max_length=255)
  price = models.PositiveIntegerField()
  image = models.ImageField(upload_to='rasmlar/', verbose_name='Rasmi')
  about = models.TextField(verbose_name="Ma\'lumot")

  class Meta:
    verbose_name_plural = 'Pishiriqlar'
  def __str__(self) -> str:
    return self.name

class Slayder(models.Model):
  title = models.CharField(max_length=255, verbose_name="Slayder sarlavhasi")
  slug = models.SlugField(unique=True, blank=True)
  class Meta:
     verbose_name_plural = 'Slayder'
  def __str__(self) -> str:
    return self.title
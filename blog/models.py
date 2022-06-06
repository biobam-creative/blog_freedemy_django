from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateTimeField()
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    tags = TaggableManager()
    link = models.CharField(max_length=255, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)


class Opportunity(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateTimeField()
    closing_date = models.DateTimeField()
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Opportunity, self).save(*args, **kwargs)



# Create your models here.

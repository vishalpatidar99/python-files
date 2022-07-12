from locale import T_FMT, T_FMT_AMPM
from django.db import models
from datetime import date

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

class City(models.Model):
    name = models.CharField(max_length=35)

class Person(models.Model):
    hometown = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

class Book(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

class Topping(models.Model):
    name = models.CharField(max_length=25)

class Pizza(models.Model):
    name = models.CharField(max_length=25)
    toppings = models.ManyToManyField(Topping)
    vegetarian = models.BooleanField(null=True)

    def __str__(self):
        return "%s (%s)" % (self.name, ", ".join(topping.name for topping in self.toppings.all()),)

class Restaurant(models.Model):
    pizzas = models.ManyToManyField(Pizza, related_name='restaurants')
    best_pizza = models.ForeignKey(Pizza, related_name='championed_by', on_delete=models.CASCADE)


class Chapter(models.Model):
    title = models.CharField(max_length=35, unique=True)

class Book2(models.Model):
    title = models.CharField(max_length=256)
    chapters = models.ManyToManyField(Chapter)


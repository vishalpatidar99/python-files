from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <=self.pub_date <= now 

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Person(models.Model):
    SHIRT_SIZES =(
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=30)
    shirt_size=models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name

class Toppings(models.Model):
    name=models.CharField(max_length=25)

class Pizzas(models.Model):
    toppings=models.ManyToManyField(Toppings)

class Group(models.Model):
    name = models.CharField(max_length=120)
    members = models.ManyToManyField(Person, through="Membership", through_fields=('group', 'person'))
    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=60)
    def __str__(self):
        return self.person

class Students(models.Model):
    s_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class Coaching(models.Model):
    students = models.ManyToManyField(Students, blank=True)
    subject = models.CharField(max_length=25)

    def __str__(self):
        return self.subject

class Manufacture(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Cars(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    date_of_manufacturing = models.DateField()

    def __str__(self):
        return self.name

class Hospital_2(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Doctor_2(models.Model):
    hospital = models.ForeignKey(Hospital_2, on_delete=models.PROTECT)
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    specialist = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Patient_2(models.Model):
    hospital = models.ForeignKey(Hospital_2, on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor_2, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    disease = models.CharField(max_length=25)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name=="Yoko Ono's blog":
            return "Yoko shall never have her own blog!"
        else:
            super().save(*args, **kwargs)

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']

class Unmanaged(models.Model):

    class Meta:
        abstract = True
        managed = False

class Student(CommonInfo, Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta, Unmanaged.Meta):
        pass

class StudentNew(CommonInfo, Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta, Unmanaged.Meta):
        pass

class StudentNew1(CommonInfo,Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta, Unmanaged.Meta):
        pass

class CommonInfo2(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(null=True)
    class Meta:
        abstract = True
        ordering = ['name']

class Unmanaged(models.Model):
    class Meta:
        abstract = True
        managed = False

class Studentnew2(CommonInfo,Unmanaged):
    home_group = models.CharField(max_length=5, null=True)
    class Meta(CommonInfo2.Meta, Unmanaged.Meta):
        db_table = 'student_info2'

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False) 
    serves_pizza = models.BooleanField(default=False) 

class Person2(models.Model):
    first_name=models.CharField(max_length=35)
    last_name=models.CharField(max_length=35)

class MyPerson(Person2):
    class Meta:
        proxy = True
    def do_something(self):
        pass

class OrederedPerson(Person2):
    class Meta:
        ordering = ['last_name']
        proxy = True

class NewManager(models.Manager):
    pass

class MyPerson2(Person2):
    manager = NewManager()

    class Meta:
        proxy = True

class ExtraManager(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True

class MyPerson3(Person2, ExtraManager):
    class Meta:
        proxy = True

class Student2(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN,)

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}

class Student3(models.Model):
    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')
        GRADUATE = 'GR', _('Graduate')

    year_in_school = models.CharField(max_length=2, choices=YearInSchool.choices, default=YearInSchool.FRESHMAN,)

    def is_upperclass(self):
        return self.year_in_school in {self.YearInSchool.JUNIOR, self.YearInSchool.SENIOR,}

class MoonLandings(models.Model):
    class MoonLandings2(datetime.date, models.Choices):
        APOLLO_11 = 1969, 7, 20, 'Apollo 11 (Eagle)'
        APOLLO_12 = 1969, 11, 19, 'Apollo 12 (Intrepid)'
        APOLLO_14 = 1971, 2, 5, 'Apollo 14 (Antares)'
        APOLLO_15 = 1971, 7, 30, 'Apollo 15 (Falcon)'
        APOLLO_16 = 1972, 4, 21, 'Apollo 16 (Orion)'
        APOLLO_17 = 1972, 12, 11, 'Apollo 17 (Challenger)'

    date = models.DateField(choices=MoonLandings2.choices)

class Registration(models.Model):
    name = models.CharField(max_length=35, db_column='NAME', db_index=True, editable=False)
    email = models.EmailField(max_length=35, db_column='EMAIL', db_index=True, db_tablespace=True, help_text='abc@gmail.com', )
    address = models.CharField(max_length=25, verbose_name='Address_of_user', db_column='Address', null=True)

class Practice(models.Model):
    n = models.BigIntegerField()

class Car(models.Model):
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.RESTRICT)
    name = models.CharField(max_length=25)
    date_of_manufacturing = models.DateField()

class Manufacturer(models.Model):
    name = models.CharField(max_length=25)

class Artist(models.Model):
    name = models.CharField(max_length=25)

class Album(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)

class Song(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    Album = models.ForeignKey(Album,on_delete=models.RESTRICT)
    name = models.CharField(max_length=25)

class Filing3(models.Model):
    file = models.FileField(upload_to='media', blank=True)

class Practice2(models.Model):
    first_name = models.CharField(max_length=35, unique=True)
    last_name = models.CharField(max_length=35, unique=True)

    class Meta:
        permissions = [('can_deliver_pizzas', 'can diliver pizzas')]
        unique_together = ['first_name','last_name']

class Blog2(models.Model):
    name = models.CharField(max_length=35)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog2, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=datetime.date.today)
    author = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name

class Some(models.Model):
    name = models.CharField(max_length=35)
    age=models.IntegerField()

class Other(models.Model):
    name=models.CharField(max_length=35)
    age=models.IntegerField()

class EntryDetail(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    details = models.TextField()


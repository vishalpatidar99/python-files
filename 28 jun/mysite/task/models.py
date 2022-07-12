from django.db import models

# Create your models here.

class InterviewCandidate(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    age = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender_choices=[
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Others'),
    ]
    qualification_choices=[
        ('gd', 'Graduate'),
        ('p_gd', 'Post Graduate'),
    ]
    passing_year_choices = [
        (2018, "2018"),
        (2019, "2019"),
        (2020, "2020"),
        (2021, "2021"),
        (2022, "2022"),
    ]
    profile_choices = [
        ('python', 'Python Developer'),
        ('react', 'React Developer'),
        ('HR', 'Human Resource'),
        ('BDE', 'Business Development Executive'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    qualification = models.CharField(max_length=5, choices=qualification_choices)
    passing_year=models.IntegerField(choices=passing_year_choices)
    profile = models.CharField(max_length=6, choices=profile_choices, default='python')
    number_of_given_interview = models.IntegerField(default=1)
    time = models.DateTimeField()

    def __str__(self):  
        return self.name

class InterviewUpdate(models.Model):
    interview_candidate = models.ForeignKey(InterviewCandidate, on_delete=models.CASCADE)
    interviewer = models.CharField(max_length=50)
    status_choices=[
        ('yes', 'Selected'),
        ('no', 'Regected'),
    ]
    status = models.CharField(max_length=3, choices=status_choices)

    def __str__(self):
        return self.interview_candidate
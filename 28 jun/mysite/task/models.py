from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    phone1 = models.CharField(max_length=12)
    phone2 = models.CharField(max_length=12,null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    gender_choices=[
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Others'),
    ]
    job_url = [
        ('python', 'Python Developer'),
        ('react', 'React Developer'),
        ('HR', 'Human Resource'),
        ('BDE', 'Business Development Executive'),
    ]
    source_choices=[
        ('in', 'Linkedin'),
        ('indeed', 'Indeed'),
        ('apna', 'Apna'),
        ('naukri', 'Naukri'),
        ('ref', 'Reffrence'),
        ('social', 'Social Media'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    profile = models.CharField(max_length=6, choices=job_url, default='python')
    source = models.CharField(max_length=10, choices=source_choices)
    number_of_given_interview = models.IntegerField(default=1)

    def __str__(self):  
        return self.name

class InterviewUpdate(models.Model):
    interview_candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    interviewer = models.CharField(max_length=50)
    status_choices=[
        ('yes', 'Selected'),
        ('no', 'Regected'),
    ]
    status = models.CharField(max_length=3, choices=status_choices)

    def __str__(self):
        return self.interview_candidate

class Qualification(models.Model):
    graduate_degree=[
        ('bsc', 'B.Sc.'),
        ('Bcom', 'B.Com.'),
        ('BA', 'B.A.'),
        ('BE', 'B.E.'),
        ('Btech', 'B.Tech.'),
    ]
    graduation = models.CharField(max_length=5, choices=graduate_degree)

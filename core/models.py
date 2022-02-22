from pyexpat import model
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from turtle import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


Marital_CHOICES = (
    ('Single(অবিবাহিত)', 'Single(অবিবাহিত)'),
    ('Married(বিবাহিত)', 'Married(বিবাহিত)'),
    ('Divorced(তালাকপ্রাপ্ত)','Divorced(তালাকপ্রাপ্ত)'),
    ('Widowed(বিধবা)','Widowed(বিধবা)')
    
)

Status_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
    ('Waiting', 'Waiting'),
    ('Successfully Done', 'Successfully Done')

)


Education_CHOICES = (
    ('MASTERS', 'MASTERS'),
    ('BACHELOR', 'BACHELOR'),
    ('H.S.C', 'H.S.C'),
    ('S.S.C', 'S.S.C'),
    ('J.S.C', 'J.S.C'),
    ('P.S.C', 'P.S.C'),

)


class Course(models.Model):
    Title = models.CharField(max_length=50, verbose_name="শীরনাম")
    description = models.TextField(max_length=500, verbose_name= "বর্ণনা" )

    def __str__(self):
        return self.Title

class Session(models.Model):
    course = models.ForeignKey(Course , related_name='session', on_delete=models.CASCADE, verbose_name="কোর্স")
    session_year = models.CharField(max_length=50,  verbose_name="শীরনাম")

    def __str__(self):
        return self.session_year


class District(models.Model):
    name = models.CharField(max_length=30, verbose_name="নাম")

    def __str__(self):
        return self.name

class Sub_district(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name="জেলা")
    name = models.CharField(max_length=30, verbose_name="নাম")

    def __str__(self):
        return self.name

class Applicant(models.Model):
    course = models.ForeignKey(Course , on_delete=models.CASCADE, verbose_name="কোর্স")
    session = models.ForeignKey(Session, related_name='applicants', on_delete=models.CASCADE, verbose_name="সেশন")
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    roll_no = models.CharField(max_length=50, blank=True, null=True, verbose_name="ক্রমিক নং")
    
    name_ban = models.CharField(max_length=50, verbose_name="নাম (বাংলা)")
    name_eng = models.CharField(max_length=50, verbose_name="নাম (English)")
    fathers_name_bangla = models.CharField(max_length=50, verbose_name=" পিতার নাম (বাংলা)")
    fathers_name = models.CharField(max_length=50, verbose_name="পিতার নাম (English)")
    mothers_name_bangla = models.CharField(max_length=50, verbose_name="মাতার নাম (বাংলা)")
    mothers_name = models.CharField(max_length=50, verbose_name="মাতার নাম (English)")
    marital_status = models.CharField(choices = Marital_CHOICES,max_length=50, verbose_name="বৈবাহিক অবস্থা")
    present_address = models.CharField(max_length=100, verbose_name="বর্তমান ঠিকানা")
    village = models.CharField(max_length=50, verbose_name="গ্র্রাম")
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, verbose_name="জেলা")
    sub_district = models.ForeignKey(Sub_district, on_delete=models.SET_NULL, null=True, verbose_name="উপজেলা")
    ps = models.CharField(max_length=50, verbose_name="থানা")
    post_office = models.CharField(max_length=50, verbose_name="ডাকঘর")
    date_of_birth = models.DateField(verbose_name="জন্মতারিখ")
    religion = models.CharField(max_length=50, verbose_name="ধর্ম")
    
    nid_BC =  models.CharField(max_length=25, verbose_name="জন্মনিবন্ধন/জাতীয় পরিচয়পত্র নং")
    
    education =  models.CharField(choices = Education_CHOICES,max_length=50, verbose_name="শিক্ষাগত যোগ্যতা")
    phone = models.CharField(max_length=11, verbose_name="মোবাইল")
    picture =  models.ImageField(upload_to='uploads/', verbose_name="ছবি")
    status =  models.CharField(choices = Status_CHOICES,max_length=50, verbose_name="সিদ্ধান্ত")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_eng


class Resolution(models.Model):
    title = models.CharField(max_length=50, verbose_name="শীরনাম")
    short_description = models.TextField(max_length=500, verbose_name= "বর্ণনা" )
    detail = models.TextField(max_length=1000, verbose_name= "বিস্তারিত বর্ণনা" )
    file_1 = models.FileField()

    def __str__(self):
        return self.title


class Financial_aid(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    ammount = models.FloatField()
    Detail = models.TextField(max_length=400, verbose_name= "বিস্তারিত" )

    def __str__(self):
        return self.applicant

    
# all session


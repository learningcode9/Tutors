from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    


class tutors(models.Model):
    
    category = models.ForeignKey(Category, related_name='tutors', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    Tagline = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description_tutor = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images=models.ImageField(upload_to="media")
    qualification=models.TextField(null=True)
    related_subjects=models.CharField(max_length=250,null=True)
    education_1=models.CharField(max_length=100,null=True)
    education_2=models.CharField(max_length=100,null=True,blank=True)
    education_3=models.CharField(max_length=100,null=True,blank=True)
    education_4=models.CharField(max_length=100,null=True,blank=True)
    Home_school=models.CharField(max_length=100,null=True,blank=True)
    Language=models.CharField(max_length=100,null=True,blank=True)
    Most_popular=models.CharField(max_length=100,null=True,blank=True)
    Music=models.CharField(max_length=100,null=True,blank=True)
    summar=models.CharField(max_length=100,null=True,blank=True)
    # # enter_monday = models.CharField(null=True,blank=True,defalut="Monday" max_length=50)
    enter_mondaytimings= models.CharField(default="NotAvailable",max_length=50,editable=True)
    # # enter_tuesday = models.CharField(null=True,blank=True,default="Tuesday" max_length=50)
    enter_tuesdaytimings= models.CharField(default="NotAvailable",max_length=50,editable=True)
    # # enter_wednesday = models.CharField(null=True,blank=True,max_length=50)
    enter_wednesdaytimings= models.CharField(default="NotAvailable",max_length=50,editable=True)
    # # enter_thursday = models.CharField(null=True,blank=True,max_length=50)
    enter_thursdaytimings= models.CharField(default="NotAvailable",max_length=50,editable=True)
    # # enter_friday = models.CharField(null=True,blank=True,max_length=50)
    enter_fridaytimings= models.CharField(default="Not Available",max_length=50,editable=True)
    # # enter_saturday = models.CharField(null=True,blank=True,max_length=50)
    enter_saturdaytimings= models.CharField(default="Not Available",max_length=50,editable=True)
    # # enter_sunday = models.CharField(null=True,blank=True,max_length=50)
    enter_sundaytimings= models.CharField(default="Not Available",max_length=50,editable=True)
    
   
    
    class Meta:
       ordering = ('name', )
       index_together = (('id', 'slug'),) 
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('onlinetutors:tutor_detail', args=[self.id, self.slug])
  

   

   



  
# Create your views here. 
class Application(models.Model):
    STATE_CHOICES =( 
    ('', 'Choose...'),("1","Alabama"),("2","Alaska"),("3","Arizona"),("4","Arkansas"),("5","California"),("6","Colorado"),
    ("7","Connecticut"),("8","Delaware"),("9","Florida"),("10","Georgia"),("11","Hawaii"),("12","Idaho"),
    ("13","Illinois"),("14","Indiana"),("15","Iowa"),("16","Kansas"),("17","Kentucky"),("18","Louisiana"),
    ("19","Maine"),("20","Maryland"),("21","Massachusetts"),("22","Michigan"),("23","Minnesota"),("24","Mississippi"),
    ("25","Missouri"),("26","Montana"),("27","Nebraska"),("28","Nevada"),("29","New Hampshire"),("30","New Jersey"),
    ("31","New Mexico"),("32","New York"),("33","North Carolina"),("34","North Dakota"),("35","Ohio"),
    ("36","Oklahoma"),("37","Oregon"),("38","Pennsylvania"),("39","Rhode Island"),("40","South Carolina"),
    ("41","South Dakota"),("42","Tennessee"),("43","Texas"),("44","Utah"),("45","Vermont"),("46","Virginia"),
    ("47","Washington"),("48","West Virginia"),("49","Wisconsin"),("50","Wyoming"),
    ) 

    GENDER_CHOICES=(
     ('male','Male'),
     ('female','Female'),
     ('other','other'),
    )
    k=(
    ('yes','Yes'),
    ('no','No'),
    )
    degree=(
    ('yes','Yes'),
    ('no','No'),
    )
    classroom=(
    ('yes','Yes'),
    ('no','No'),
    )
    genres1=(
       ('classical','Classical'),
       ('rock','Rock'),
       ('musical Theater','Musical Theater'),
       ('country','country'),
       ('blues','Blues'),
       ('christian Contemporary','Christian Contemporary'),
       ('gospel','Gospel'),
       ('other','Other'),
    )

    languages1=(
        ('english','English'),
        ('spanish','Spanish'),
        ('german','German'),
        ('chinese','Chinese'),
        ('hindi','Hindi'),
        ('french','French'),
        ('russian','Russian'),
        ('turkish','Turkish'),
    )
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    Email=models.EmailField(null=False,blank=False,unique=True)
    phonenumber=models.CharField(max_length=13,null=False, blank=False, unique=True)
    password = models.CharField(max_length=32)
    confirm_password=models.CharField(max_length=32)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100,choices=STATE_CHOICES)
    city = models.CharField(max_length=100)
    zipcode=models.CharField(max_length=15)
    DOB=models.DateField()
    Gender=models.CharField(max_length=50,choices=GENDER_CHOICES)
    k12=models.CharField(max_length=50,choices=k)
    degree=models.CharField(max_length=50,choices=degree)
    classroom=models.CharField(max_length=50,choices=classroom)
    # qgenres=models.CharField(max_length=50, choices=genres1)
    # languages=models.CharField(max_length=50, choices=languages1)
    languages = MultiSelectField(choices=languages1,null=True,blank=True)
    genres = MultiSelectField(choices=genres1,null=True,blank=True)
    resume = models.FileField(upload_to='resume/',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.firstname

class Comment(models.Model):
    post=models.ForeignKey(tutors,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=32) 
    email=models.EmailField()  
    body=models.TextField() 
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True) 
    active=models.BooleanField(default=True) 
    class Meta:   
        ordering=('created',) 
    def __str__(self): 
        return 'Commented By {} on {}'.format(self.name,self.post) 


class ratings(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.FloatField()
    tutorname=models.ForeignKey(tutors,related_name='ratings',on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_created=True)
    updated=models.DateTimeField(auto_created=True)
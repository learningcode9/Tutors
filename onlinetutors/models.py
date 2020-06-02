from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField


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
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images=models.ImageField(upload_to="media")
  

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
    ("1","Alabama"),("2","Alaska"),("3","Arizona"),("4","Arkansas"),("5","California"),("6","Colorado"),
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
    phonenumber=models.CharField(max_length=15,null=False, blank=False, unique=True)
    password = models.CharField(max_length=32)
    confirm_password=models.CharField(max_length=32)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
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
    languages = MultiSelectField(choices=languages1,null=True)
    genres = MultiSelectField(choices=genres1,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.firstname



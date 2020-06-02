from django import forms
from django.forms import ModelForm
from .models import Application


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
    # genres1=(
    #    ('classical','Classical'),
    #    ('rock','Rock'),
    #    ('musical Theater','Musical Theater'),
    #    ('country','country'),
    #    ('blues','Blues'),
    #    ('christian Contemporary','Christian Contemporary'),
    #    ('gospel','Gospel'),
    #    ('other','Other'),
    # )

# languages1=(
#     ('english','English'),
#     ('spanish','Spanish'),
#     ('german','German'),
#     ('chinese','Chinese'),
#     ('hindi','Hindi'),
#     ('french','French'),
#     ('russian','Russian'),
#     ('turkish','Turkish'),
#   )
class application(ModelForm):
    
    DOB=forms.DateField(widget = forms.SelectDateWidget) 
    Gender= forms.CharField(label='Gender',widget=forms.RadioSelect(choices=GENDER_CHOICES))
    k12=forms.CharField(label="Have you taught in K-12 schools?",widget=forms.RadioSelect(choices=k))
    degree=forms.CharField(label="Do you have a 4 year degree?",widget=forms.RadioSelect(choices=degree))
    classroom=forms.CharField(label="Have you taught in a classroom setting?",widget=forms.RadioSelect(choices=classroom))
    # languages=forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=languages1)
    # genres=forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=genres1)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
    class Meta:
        model=Application
        fields= '__all__'
        


     

   
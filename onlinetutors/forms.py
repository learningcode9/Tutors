from django import forms
from django.forms import ModelForm
from .models import Application
# from django.contrib.auth.password_validation import validate_password
from django.core import validators
from .validators import validate_password_uppercase,validate_password_length,validate_password_digit
from usps import USPSApi, Address
import requests

YEARS= [x for x in range(1971,2002)]
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
    error_css_class = 'error'
    
    DOB= forms.DateField(label="Date Of Birth",required=True,widget=forms.TextInput({ "placeholder": "YYYY-MM-DAY"}))
    Gender= forms.CharField(label='Gender',widget=forms.RadioSelect(choices=GENDER_CHOICES))
    k12=forms.CharField(label="Have you taught in K-12 schools?",widget=forms.RadioSelect(choices=k),required=True)
    degree=forms.CharField(label="Do you have a 4 year degree?",widget=forms.RadioSelect(choices=degree),required=True)
    classroom=forms.CharField(label="Have you taught in a classroom setting?",widget=forms.RadioSelect(choices=classroom),required=True)
    # languages=forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=languages1)
    # genres=forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=genres1)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput,validators=[validate_password_digit,validate_password_length,validate_password_uppercase])
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    address=forms.CharField(max_length=100)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)
    
    class Meta:
        model=Application
        fields= '__all__'
        

    def clean(self):
      total_cleaned_data=super().clean()
      bot_handler_value=total_cleaned_data['bot_handler']
      if len(bot_handler_value)>0:
        raise forms.ValidationError("Request from bot cann't be submitted")
      firstname=total_cleaned_data['firstname']
      if len(firstname)<2:
        raise forms.ValidationError('Plz enter valid firstname')
      lastname=total_cleaned_data['lastname']
      if len(lastname)<2:
        raise forms.ValidationError('Plz enter valid lastname')
     
      confirm_password=total_cleaned_data['confirm_password']
      password=total_cleaned_data['password']
      if password != confirm_password:
          raise forms.ValidationError('Both passwords should be same')
      phonenumber=total_cleaned_data['phonenumber']
      if len(phonenumber)<10:
        raise forms.ValidationError("please enter a valid phone number")
      if not phonenumber.isdigit(): 
        raise forms.ValidationError("please enter digits only")
      # if not int(phonenumber):
      #         raise ValueError("please enter a valid phone number")
      # address=total_cleaned_data["address"]
      # usps = USPSApi('107TUTOR8093', test=True)
      # validation = usps.validate_address(address)
      # print(validation.result)



       
        


     

   
from django import forms
from django.forms import ModelForm,DateInput
from onlinetutors.models import Application,tutors,Comment 
# from django.contrib.auth.password_validation import validate_password
from django.core import validators
from .validators import validate_password_uppercase,validate_password_length,validate_password_digit
import requests
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import re


class signupForm(forms.Form):
    firstname=forms.CharField(max_length=25,required=True,validators = [validators.MinLengthValidator(3)])
    lastname=forms.CharField(max_length=25,required=True,validators = [validators.MinLengthValidator(3)])
    username=forms.CharField(max_length=15,required=True,validators = [validators.MinLengthValidator(3)])
    email=forms.EmailField(required=True)
    password = forms.CharField(required=True,max_length=32, widget=forms.PasswordInput,validators=[validate_password_uppercase,validate_password_length,validate_password_digit])
    confirm_password = forms.CharField(required=True,max_length=32, widget=forms.PasswordInput)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput,validators=[])

    def clean(self):
      # total_cleaned_data=super().clean()
      # bot_handler_value=total_cleaned_data['bot_handler']
      # if len(bot_handler_value)>0:
      #   raise forms.ValidationError("Request from bot cann't be submitted")
      # password=total_cleaned_data['password']
      # if  len(password)<4:
      #   raise forms.ValidationError("Password is too short")
      # return password
      # if not re.search(r"[\d]+", password):
      #   raise forms.ValidationError("The password must contain at least one digit")
      # return password
      # if not re.search(r"[A-Z]+", password):
      #   raise forms.ValidationError("The password must contain at least one uppercase character")
      # return password
      # confirm_password=total_cleaned_data['confirm_password']
      # if password != confirm_password:
      #   raise forms.ValidationError("Both passwords should match")
      # return password
      password = self.cleaned_data.get('password')
      confirm_password = self.cleaned_data.get('confirm_password')
      if password != confirm_password:
          raise forms.ValidationError('Password Must Match')
      return super().clean()
      
      
        
        

    
   
class loginForm(forms.Form):
    username=forms.CharField(max_length=15)
    password=forms.CharField(max_length=15,widget=forms.PasswordInput(render_value=False))

# class resetPassword(forms.Form):
# class PasswordResetForm(forms.Form):
#     email=forms.EmailField()
    
# class PasswordResetForm(forms.Form):
#     # username=forms.CharField(max_length=15)
#     password = forms.CharField(required=True,max_length=32, widget=forms.PasswordInput,validators=[validate_password_uppercase,validate_password_length,validate_password_digit])
#     confirm_password = forms.CharField(required=True,max_length=32, widget=forms.PasswordInput)
#     def clean(self):
#       password = self.cleaned_data.get('password')
#       confirm_password = self.cleaned_data.get('confirm_password')
#       if password != confirm_password:
#           raise forms.ValidationError('Password Must Match')
#       return super().clean()

    


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
 
class application(ModelForm):
    error_css_class = 'error'
    
    DOB= forms.DateField(label="Date Of Birth",required=True,widget=forms.TextInput({ "placeholder": "YYYY-MM-DAY"}))
    Gender= forms.CharField(label='Gender',widget=forms.RadioSelect(choices=GENDER_CHOICES))
    k12=forms.CharField(label="Have you taught in K-12 schools?",widget=forms.RadioSelect(choices=k),required=True)
    degree=forms.CharField(label="Do you have a 4 year degree?",widget=forms.RadioSelect(choices=degree),required=True)
    classroom=forms.CharField(label="Have you taught in a classroom setting?",widget=forms.RadioSelect(choices=classroom),required=True)
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
    




        


     

   
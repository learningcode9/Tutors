from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from account.forms import application,signupForm,loginForm
from onlinetutors.models import Application
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from account.token_generator import account_activation_token
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q
from django.contrib import messages
from django.contrib.auth import authenticate 
import requests
# from requests_oauthlib import OAuth1
import json
# from requests.auth import HTTPBasicAuth
# from account import address_verification

# Create your views here.

def registration(request):
    
    if request.method == 'POST':
        form=application(request.POST,request.FILES)
        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            Email=form.cleaned_data['Email']
            phonenumber=form.cleaned_data['phonenumber']
            password = form.cleaned_data['password']
            confirm_password=form.cleaned_data['confirm_password']
            address = form.cleaned_data['address']
            state = form.cleaned_data['state']
            city =form.cleaned_data['city']
            zipcode=form.cleaned_data['zipcode']
            DOB=form.cleaned_data['DOB']
            Gender=form.cleaned_data['Gender']
            k12=form.cleaned_data['k12']
            degree=form.cleaned_data['degree']
            classroom=form.cleaned_data['classroom']
            genres=form.cleaned_data['genres']
            languages=form.cleaned_data['languages']
            resume=form.cleaned_data['resume']
            
      
            form=Application(firstname=firstname,lastname=lastname,Email= Email,phonenumber=phonenumber,
            password=password,address=address,state= state,city=city,zipcode=zipcode,
            DOB=DOB,Gender=Gender,k12=k12,degree=degree,classroom=classroom,languages=languages,genres=genres,resume=resume)
            # fullname=firstname+ ' ' +lastname
            # address_check=address_verification.run(addressee=fullname,street=address,city=city,state=state,zipcode=zipcode)
            # check=address_verification.run(firstname,address,city,state,zipcode)
            payload = {'addressee': firstname, 'street': address, 'city' : city, 'state' : state ,'zipcode' : zipcode}
            url = "https://us-street.api.smartystreets.com/street-address?&auth-id=9a7b8041-9ac4-7e15-75b0-780771fc3d92&auth-token=xMvDBs26P88X0Esk8q5D"
            headers={"Accept":"application/json"}
            
           
            response=requests.get(url,headers=headers, params=payload)
            # print(response.status_code)
            # # res_text=response.text.encode('utf8')
            # # print(json.loads(r.text))
            # print(response,type(response))
            # print(response.text,type(response.text))
            
            if response.text=="[]" :
                return HttpResponse("<h2>address is invalid ,please try again<h2>")
            else:

                send_mail(
                    "Thanks",
                    "Thanks for your registration,We will get back to you after reviewing your resume",
                    settings.EMAIL_HOST_USER,
                    [Email],
                    fail_silently=False,
                )
           
                form.save()
                return redirect("/thankyou/")
            
                
        else:
            print(form.errors)
    else:
        form=application()
    return render(request,"registration.html",{"form":form})



def signUp(request):

   
    if request.method == 'POST':
       
        form=signupForm(request.POST)#with the form data creating an object,when ever form submits then only this if part works.
        if  form.is_valid():#if form values are valid ,means without any errors
            
            abc=form.cleaned_data['firstname'] #capturing the data from the form fields
            last_name=form.cleaned_data['lastname']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            confirm_password=form.cleaned_data['confirm_password']
            user=User.objects.create_user(username=username,first_name=abc,last_name=last_name,email=email,password=password)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                
                'token': account_activation_token.make_token(user),
                 
            })
    
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
            # return redirect('../login')

            
    else:
        form=signupForm()
    return render(request,"signup.html",{"form":form})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('/account/login')
        
    else:
        return HttpResponse('Activation link is invalid!')

def login(request):
    if request.method=='POST':
        form=loginForm(request.POST)
       
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request,user)
                #messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else: 
                messages.error(request, "Invalid username or password.")
                return redirect('/account/login')
        
    else:
        form = loginForm()
        return render(request,"login.html",{"form":form})

def Logout(request):
    auth.logout(request)
    return redirect("/")






        
   
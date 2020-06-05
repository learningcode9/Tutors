from django.shortcuts import render,redirect, get_object_or_404
from onlinetutors.models import Category,tutors
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 
from .forms import application
from .models import Application
from django.core.mail import send_mail
from django.conf import settings


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


def thankyou(request):
    return render(request,'thankyou.html')
def home(request):
    return render(request,'home.html')

def arts(request):
    categories = Category.objects.filter(name='Arts')
    tutor = tutors.objects.filter(category_id=1)
    paginator=Paginator(categories,1)
    page_number=request.GET.get('page')   
    try:          
        categories=paginator.page(page_number)   
    except PageNotAnInteger:         
        categories=paginator.page(1)   
    except EmptyPage:           
        categories=paginator.page(paginator.num_pages) 
    context = {
        
        'categories': categories,
        'tutor': tutor
    }
  
    return render(request,'Arts.html',context)
# def music(request):
#     categories = Category.objects.filter(name='Music')
#     tutor = tutors.objects.filter(category_id=2)
#     context = {
        
#         'categories': categories,
#         'tutor': tutor
#     }
  
#     return render(request,'Music.html',context)
# def arts(request):
#     categories = Category.objects.filter(name='Theatre')
#     tutor = tutors.objects.filter(category_id=3)
#     context = {
        
#         'categories': categories,
#         'tutor': tutor
#     }
  
#     return render(request,'Theatre.html',context)
# def arts(request):
#     categories = Category.objects.filter(name='Dance')
#     tutor = tutors.objects.filter(category_id=4)
#     context = {
        
#         'categories': categories,
#         'tutor': tutor
#     }
  
#     return render(request,'Dance.html',context)
def tutor_detail(request, id, slug):
    tutor = get_object_or_404(tutors, id=id, slug=slug)
    
    context = {
        'tutor': tutor,
        
    }
    return render(request, 'detail.html', context)

def profile(request):
    return render(request,'tutorprofile.html')

# def application(request):
#     return render(request,'application.html')

def checkout(request):
    return render(request,'checkout.html')


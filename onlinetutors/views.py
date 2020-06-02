from django.shortcuts import render,redirect, get_object_or_404
from onlinetutors.models import Category,tutors
from .forms import application
from .models import Application


def registration(request):
    if request.method == 'POST':
        form=application(request.POST)
        if form.is_valid():
           
           
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            Email=form.cleaned_data['Email']
            phonenumber=form.cleaned_data['phonenumber']
            password = form.cleaned_data['password']
            confirm_password=form.cleaned_data['confirm_password']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
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
            
            form=Application(firstname=firstname,lastname=lastname,Email= Email,phonenumber=phonenumber,
            password=password,address1=address1,address2=address2, state= state,city=city,zipcode=zipcode,
            DOB=DOB,Gender=Gender,k12=k12,degree=degree,classroom=classroom,languages=languages,genres=genres)
           
            form.save()
            return redirect("/thankyou/")
    else:
        form=application()
    return render(request,"registration.html",{"form":form})


# def registration(request):
#     if request.method == 'POST':
#         form=application(request.POST)
#         if form.is_valid():
#             form.save()
#             firstname=form.cleaned_data['firstname']
#             lastname=form.cleaned_data['lastname']
#             country=form.cleaned_data['country']
#             form= djangoForm(firstname=firstname,lastname=lastname,country=country)
#             form.save()
#             return redirect("/thankyou/")
#     else:
#         form=application()
    # return render(request,"registration.html",{"form":form})









def thankyou(request):
    return render(request,'thankyou.html')
def home(request):
    return render(request,'home.html')

def arts(request):
    categories = Category.objects.filter(name='Arts')
    tutor = tutors.objects.filter(category_id=1)
    context = {
        
        'categories': categories,
        'tutor': tutor
    }
  
    return render(request,'Arts.html',context)
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


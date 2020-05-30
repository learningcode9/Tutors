from django.shortcuts import render,redirect, get_object_or_404
from onlinetutors.models import Category,tutors

# Create your views here.

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

def application(request):
    return render(request,'application.html')

def checkout(request):
    return render(request,'checkout.html')


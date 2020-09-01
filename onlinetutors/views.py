from django.shortcuts import render,redirect, get_object_or_404
from onlinetutors.models import Category,tutors
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 
# from . forms import application,CommentForm
from . forms import CommentForm
from .models import tutors,Comment,ratings
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Avg




def thankyou(request):
    return render(request,'thankyou.html')
def home(request):
    return render(request,'home.html')

def arts(request):
    categories = Category.objects.filter(name='Arts')
    tutor = tutors.objects.filter(category_id=1)
    paginator=Paginator(categories,2)
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

def tutor_detail(request, id, slug):
    tutor = get_object_or_404(tutors, id=id, slug=slug)
    
    context = {
        'tutor': tutor,
        
    }
    return render(request, 'detail.html', context)

def profile(request):
    return render(request,'tutorprofile.html')


def checkout(request):
    return render(request,'checkout.html')



        
def AddCommentView(request, pk):
    
    post = get_object_or_404(tutors, pk=pk)
    comments = post.comments.filter(active=True)
 
    # Comment posted
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            return redirect('/')
            
    else:
        form = CommentForm()

    return render(request,'add_comments.html', {'form': form})

def ratings(request,pk):
    
    rating_tutor=get_object_or_404(tutors,pk=pk)
    userratings=rating_tutor.ratings.all().aggregate(Avg('rating'))
 
    return render(request, 'detail.html')



def datePicker(request):
    return render(request,'data_picker.html')
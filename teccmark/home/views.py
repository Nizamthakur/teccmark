from django.shortcuts import render
from .models import BlogPost,Portfolio



def homePage(request):
    return render(request, 'index.html')

def blog(request):
    posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'blog.html', {'posts': posts})

def feature(request):
    portfolio_items = Portfolio.objects.all()
    return render(request, 'feature.html', {'portfolio_items': portfolio_items})

def about_us(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'service.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def contact(request):
    return render(request, 'contact.html')
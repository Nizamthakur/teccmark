from django.shortcuts import render

def homePage(request):
    return render(request, 'index.html')
def about_us(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def feature(request):
    return render(request, 'feature.html')
def services(request):
    return render(request, 'service.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')
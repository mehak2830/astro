from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def astrologer(request):
    return render(request,'astrologer.html')

def blog_detail(request):
    return render(request,'blog_detail.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def privacy_policy(request):
    return render(request,'privacy_policy.html')

def service_detail(request):
    return render(request,'service_detail.html')

def service(request):
    return render(request,'service.html')

def zodiac_single(request):
    return render(request,'zodiac_single.html')

def about(request):
    return render(request,'about.html')

def blog_left_detail(request):
    return render(request,'blog_left_detail.html')

def appointment(request):
    return render(request,'appointment.html')
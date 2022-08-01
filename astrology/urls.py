from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('astrologer',views.astrologer,name='astrologer'),
    path('blog_detail',views.blog_detail,name='blog_detail'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('privacy_policy',views.privacy_policy,name='privacy_policy'),
    path('service_detail',views.service_detail,name='service_detail'),
    path('service',views.service,name='service'),
    path('zodiac',views.zodiac_single,name='zodiac_single'),
    path('about',views.about,name='about'),
    path('blog_left_detail',views.blog_left_detail,name='blog_left_detail'),
    path('appointment',views.appointment,name='appointment'),
]
from typing import final
from studioproject.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
from datetime import datetime
from razorpay.resources import card, order
from barryapp.models import Contact
from barryapp.models import Index
from barryapp.models import Blog
from barryapp.models import Header
from barryapp.models import Blog2
from barryapp.models import Blog3
from barryapp.models import Text1
from barryapp.models import Text2
from barryapp.models import Pics
from barryapp.models import Photos
from barryapp.models import Photos2
from barryapp.models import Photos3
from barryapp.models import Photos4
from barryapp.models import Photos5
from barryapp.models import Photos6
from barryapp.models import Photos7
from barryapp.models import Text3
from barryapp.models import Text4
from barryapp.models import Images2
from barryapp.models import Images3
from barryapp.models import Images4
from barryapp.models import Slide1
from barryapp.models import Applynow
from barryapp.models import Slide3
from barryapp.models import Contactus
from barryapp.models import Beginner
from barryapp.models import Standard
from barryapp.models import Professional
from barryapp.models import Textbooknow
from django.contrib import messages 
#from django.contrib import shatterd

# Create your views here.
import razorpay
def index(request):
    index = Index.objects.all()
    blog = Blog.objects.all()
    header = Header.objects.all() 
    blog2 = Blog2.objects.all() 
    blog3 = Blog3.objects.all() 
    text1 = Text1.objects.all() 
    text2 = Text2.objects.all() 
    pics = Pics.objects.all()
    photos = Photos.objects.all()
    photos2 = Photos2.objects.all()
    photos3 = Photos3.objects.all()
    photos4 = Photos4.objects.all()
    photos5 = Photos5.objects.all()
    photos6 = Photos6.objects.all()
    photos7 = Photos7.objects.all()
    text3 = Text3.objects.all()
    text4 = Text4.objects.all()
    images2 = Images2.objects.all()
    images3 = Images3.objects.all()
    images4 = Images4.objects.all()
    slide1 = Slide1.objects.all()
    #slide2 = Slide2.objects.all()
    slide3 = Slide3.objects.all()    
    
    context = {
    'index':index, 
    'blog': blog, 
    'header': header, 
    'blog2': blog2, 'blog3': blog3, 
    'text1': text1, 'text2': text2, 
    'pics':pics, 'photos': photos, 
    'text3': text3, 
    'images2': images2, 'images3':images3, 'images4':images4, 
    'slide1': slide1, 'slide3': slide3, 
    'photos2': photos2, 'photos3': photos3, 'photos4':photos4, 'photos5':photos5, 'photos6': photos6, 'photos7': photos7, 
    'text4': text4,    
    }
    
    return render(
        request, "index.html",
         context
    ) 
    
    
def booknow(request):
    beginner = Beginner.objects.all()
    standard = Standard.objects.all()
    professional = Professional.objects.all()
    textbooknow = Textbooknow.objects.all()
    context ={
        'beginner': beginner,
        'standard': standard,
        'professional': professional,
        'textbooknow': textbooknow
    }
    return render(request, 'booknow.html', context)

def musicalbum(request):
    return render(request, 'musicalbum.html')


def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")

 
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')          
        contact=Contact(name=name, email= email, phone=phone, desc=desc, date=datetime.today())
        contact.save()   
        messages.success(request,'youre message has been sent')       
    return render(request, 'contact.html',)


def success(request):
    if request.method == "POST":
        a = request.POST
        print(a)
    return render(request,'success.html')

    
# adding Payment gateway

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def payment(request):
    order_amount = int(7999*100 )
    order_currency= "INR"
    payment_order = client.order.create(dict(amount=order_amount,currency=order_currency, payment_capture=1))
    payment_order_id = payment_order['id'] 
    context = { 
            'amount': 7999, 'api_key': RAZORPAY_API_KEY, 'order_id': payment_order_id
    }
    return render(request,'payment.html', context)   


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def standard(request):
    order_amount = int(9999*100 )
    order_currency= "INR"
    payment_order = client.order.create(dict(amount=order_amount,currency=order_currency, payment_capture=1))
    payment_order_id = payment_order['id'] 
    context = { 
            'amount': 9999, 'api_key': RAZORPAY_API_KEY, 'order_id': payment_order_id
    }
    return render(request,'standard.html', context)


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def professional(request):
    order_amount = int(19999*100 )
    order_currency= "INR"
    payment_order = client.order.create(dict(amount=order_amount,currency=order_currency, payment_capture=1))
    payment_order_id = payment_order['id'] 
    context = { 
            'amount': 19999, 'api_key': RAZORPAY_API_KEY, 'order_id': payment_order_id
    }
    return render(request,'professional.html', context)

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def advance(request):
    order_amount = int(14999*100 )
    order_currency= "INR"
    payment_order = client.order.create(dict(amount=order_amount,currency=order_currency, payment_capture=1))
    payment_order_id = payment_order['id'] 
    context = { 
            'amount': 14999, 'api_key': RAZORPAY_API_KEY, 'order_id': payment_order_id
    }
    return render(request,'advance.html', context)

def paytm(request):    
    return render(request,'paytm.html')

def applynow(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        portfoliolink = request.POST.get('portfoliolink')
        experience = request.POST.get('experience')
        images = request.POST.get('images')         
        applynow=Applynow(name=name, email= email, phone=phone, age=age, portfoliolink=portfoliolink, experience=experience, 
        images=images, date=datetime.today())
        applynow.save()   
        messages.success(request,'youre message has been sent')           
        
    return render(request, 'applynow.html')

 
    


        

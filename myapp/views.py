from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request=request,template_name='index.html')

def blog_details(request):
    return render(request=request,template_name='blog-details.html')


def blog(request):
    return render(request=request,template_name='blog.html')

def checkout(request):
    return render(request=request,template_name='checkout.html')


def contact(request):
    if request.method=="POST":
        user_name=request.POST.get("user_name")
        user_email=request.POST.get("user_email")

        send_mail(
    subject="Hello, user",
    message="Welcome!",
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=[user_email],
    fail_silently=False,
)

        return render(request, "contact.html",{"message": "Email sent sucessfully"})
    return render(request=request,template_name='contact.html')

def main(request):
    return render(request=request,template_name='main.html')


def product_details(request):
    return render(request=request,template_name='product-details.html')


def shop_cart(request):
    return render(request=request,template_name='shop-cart.html')

def shop(request):
    context=Shop.objects.all
    return render(request=request,template_name='shop.html',context={'context':context})


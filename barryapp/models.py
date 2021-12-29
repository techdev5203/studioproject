from datetime import timezone
from django.contrib import admin
from django.db import  models
from django.contrib.auth.models import User
from razorpay.resources.customer import Customer



# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name  


class Index(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name 


class Blog(models.Model):
    name = models.CharField(max_length=2000, null=True)
    Description = models.CharField(max_length=2000, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Blog2(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.TextField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name

class Blog3(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.TextField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=2000, null=True, blank=True)
    def __str__(self):
        return self.name

class Header(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.TextField(max_length=100, blank=True, default='0.0')
    tag = models.TextField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=2000, blank=True, default='0.0')
    def __unicode__(self):
        return self.name
        
    def __str__(self):
        return str(self.name)


class Text1(models.Model):
    name = models.CharField(max_length=200, null=True)
  
    def __str__(self):
        return self.name

class Text2(models.Model):
    name = models.CharField(max_length=200, null=True)   
    def __str__(self):
        return self.name

class Pics(models.Model):
    images = models.ImageField(upload_to='images')    
    def __str__(self):
        return str(self.images)
        
class Photos(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.TextField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class Text3(models.Model):
    name = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name

class Images2(models.Model):
    images = models.ImageField(upload_to='images')    
    def __str__(self):
        return str(self.images)

class Images3(models.Model):
    images = models.ImageField(upload_to='images')    
    def __str__(self):
        return str(self.images)

class Images4(models.Model):
    images = models.ImageField(upload_to='images')    
    def __str__(self):
        return str(self.images)

class Slide1(models.Model):
    name = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=2000, null=True)
    images = models.ImageField(upload_to='images')
    tag = models.TextField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.name

#class Slide2(models.Model):
 #   name = models.CharField(max_length=200, null=True)
  #  desc = models.CharField(max_length=2000, null=True)
   # images = models.ImageField(upload_to='images')
    #tag = models.TextField(max_length=50, blank=True, default='')

    #def __str__(self):
        #return self.name>

class Slide3(models.Model):
    name = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=2000, null=True)
    images = models.ImageField(upload_to='images')
    tag = models.TextField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.name

class Photos2(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.TextField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class Photos3(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.TextField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class Photos4(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.TextField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name


class Photos5(models.Model):
    images = models.ImageField(upload_to='images')    
    def __str__(self):
        return str(self.images)

class Photos6(models.Model):
    images = models.ImageField(upload_to='images')    
    def __str__(self):
        return str(self.images)

class Photos7(models.Model):
    images = models.ImageField(upload_to='images')    
    def __str__(self):
        return str(self.images)

class Text4(models.Model):
    name = models.CharField(max_length=200, null=True)
   
    def __str__(self):
        return self.name

class Contactus(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    address  = models.TextField(max_length=200, null=False)
    
    def __str__(self):
        return "{} {}".format(self.name)


class Beginner(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Standard(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Professional(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Advance(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    def __str__(self):
        return self.name

class Textbooknow(models.Model):
    title = models.CharField(max_length=2000)
    desc = models.CharField(max_length=2000)
    email = models.EmailField()

    def __str__(self):
        return self.title

class Applynow(models.Model):
    name = models.CharField(max_length=100, null= True)
    email = models.CharField(max_length=100, null= True)
    phone = models.CharField(max_length=12, null= True)
    age = models.TextField( null= True)
    portfoliolink = models.CharField(max_length=122, null= True)
    experience =  models.TextField( null= True)
    images = models.ImageField( null= True)  
    date = models.DateField()
    
    def __str__(self): 
        return str(self.name)  

 

   
   
     


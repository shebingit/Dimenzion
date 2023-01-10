from distutils.command.upload import upload
from email.policy import default
from turtle import position
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Admin_register(models.Model):
    reg_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200,default="")
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50) 
    
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    
    
class categories(models.Model):
    
    category_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE, null=True,default='')
    modelname = models.CharField(max_length=200,default='')
    description = models.CharField(max_length=255,default='')
    gib = models.FileField( upload_to="images/",null=True,blank=True,default='')
    price = models.FloatField(default='')
    types = models.CharField(max_length=255,default='')
    format = models.CharField(max_length=255,default='')
    modeltype = models.CharField(max_length=255,default='')
    image = models.ImageField(null=True, blank=True,default='')

class Register_freelance(models.Model):
    #profileinfo
    full_name=models.CharField(max_length=255,default='')
    country=models.CharField(max_length=255,default='')
    mobile=models.CharField(max_length=255,default='')
    email=models.CharField(max_length=255,default='')
    profile_pic=models.FileField(upload_to="profile/",null=True,blank=True,default='')
    Address=models.CharField(max_length=255,default='')
    #portfio
    position2=models.CharField(max_length=255,default='')
    work_1=models.FileField( upload_to="images/",null=True,blank=True,default='')
    work_2=models.FileField( upload_to="images/",null=True,blank=True,default='')
    work_3=models.FileField( upload_to="images/",null=True,blank=True,default='')
  
    #Expirence
    Total_exp=models.CharField(max_length=255,default='')
    company=models.CharField(max_length=255,default='')
    position=models.CharField(max_length=255,default='')
    Rate=models.CharField(max_length=255,default='')
    Resume=models.FileField( upload_to="images/",null=True,blank=True,default='')
   
    #education
    
    college=models.CharField(max_length=255,default='')
    special=models.CharField(max_length=255,default='')
    qualification=models.CharField(max_length=255,default='')
    #skills
    proffecional_title=models.CharField(max_length=255,default='')
    service=models.CharField(max_length=255,default='')
    skills=models.CharField(max_length=255,default='')
    over_view=models.CharField(max_length=255,default='')
    username=models.CharField(max_length=255,default='')
    password=models.CharField(max_length=255,default='')
    #work
    rating=models.IntegerField(default=1)
    ranking=models.IntegerField(default=0)
    w_status=models.CharField(max_length=10,default='0')


class cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    User=models.ForeignKey(User,on_delete=models.CASCADE)    
    



class designation(models.Model):
    designations= models.CharField(max_length=100)

    def __str__(self): 
        return self.designations

class Service_form(models.Model):
    req_date=models.DateField(auto_now_add=True,null=True,blank=True)
    user_name=models.CharField(max_length=100,default='')
    categori=models.CharField(max_length=100,default='')
    product=models.IntegerField(default='0')
    service_freelancer=models.CharField(max_length=100,default='')
    phone_number=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    Address=models.CharField(max_length=100,default='')
    description=models.TextField(default='')
    status=models.CharField(max_length=100,default='')
    file=models.FileField(upload_to="image",null=True,default='null')



    #shebin shaji

class Freelancerworks(models.Model):
    fr_user=models.CharField(max_length=100,default='')
    fr_categori=models.CharField(max_length=100,default='')
    fr_product=models.IntegerField(default='0')
    frelancer=models.ForeignKey(Register_freelance,on_delete=models.CASCADE,default='')
    fr_desecr=models.TextField(default='')
    fr_service_id=models.IntegerField(default='0')
    start_date=models.DateField(auto_now_add=True,null=True,blank=True)
    end_date=models.DateField(auto_now_add=False,null=True,blank=True)
    submitte_date=models.DateField(auto_now_add=False,null=True,blank=True)
    fr_file=models.FileField( upload_to="images/",null=True,blank=True,default='')
    fr_status= models.CharField(max_length=40)

class Messagebox(models.Model):
    name=models.CharField(max_length=100,default='')
    email=models.EmailField()
    phno=models.CharField(max_length=100,default='')
    company_name=models.CharField(max_length=100,default='')
    messag=models.TextField()
    mg_date=models.DateField(auto_now_add=True,null=True,blank=True)
    files=models.FileField(upload_to="files")
    




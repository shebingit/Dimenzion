from multiprocessing import context
from unicodedata import category
from winreg import REG_QWORD
from django.shortcuts import render,redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
import os
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Min,Max


import datetime
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.

def home(request):
    new=Product.objects.filter(category=2)
    special=Product.objects.filter(category=1)
    feature=Product.objects.filter(id=2)
    new=Product.objects.all().order_by('-id')[:3]
    special=Product.objects.all().order_by('id')[:3]
    feature=Product.objects.all().order_by('id')[3:6]
    count_a=Product.objects.filter(category_id=1).count()
    count_b=Product.objects.filter(category_id=4).count()
    count_c=Product.objects.filter(category_id=5).count()
    count_d=Product.objects.filter(category_id=6).count()
    count_e=Product.objects.filter(category_id=7).count()
    count_f=Product.objects.filter(category_id=8).count()
    persons=Register_freelance.objects.filter(ranking=1)
    return render(request, 'new_index.html',{'new':new,'fea':feature,'sp':special,'new':new,
        'sp':special,'fea':feature,'count_b':count_b,'count_c':count_c,'count_d':count_d,'count_e':count_e,
        'count_f':count_f,'count_a':count_a,'persons':persons})

def about(request):
    return render(request, 'new_about.html')

def about_two(request):
    return render(request, 'new_about_two.html')

def checkout(request):
    return render(request, 'new_checkout.html')

def contact(request):
    return render(request, 'new_contact.html')

def contact_two(request):
    return render(request, 'new_contact_two.html')

def model(request):
    if 'USID' in request.session:
        all=Product.objects.filter(category_id=1)
        three=Product.objects.filter(format='.3dx')
        count_a=Product.objects.filter(category_id=1).count()
        count_b=Product.objects.filter(category_id=4).count()
        count_c=Product.objects.filter(category_id=5).count()
        count_d=Product.objects.filter(category_id=6).count()
        count_e=Product.objects.filter(category_id=7).count()
        count_f=Product.objects.filter(category_id=8).count()
        return render(request, 'new_models.html',{'all':all,'three':three,'count_b':count_b,'count_c':count_c,'count_d':count_d,'count_e':count_e,'count_f':count_f,'count_a':count_a})
    else:
        all=Product.objects.filter(category_id=1)
        three=Product.objects.filter(format='.3dx')
        count_a=Product.objects.filter(category_id=1).count()
        count_b=Product.objects.filter(category_id=4).count()
        count_c=Product.objects.filter(category_id=5).count()
        count_d=Product.objects.filter(category_id=6).count()
        count_e=Product.objects.filter(category_id=7).count()
        count_f=Product.objects.filter(category_id=8).count()
        return render(request, 'category_models.html',{'all':all,'three':three,'count_b':count_b,'count_c':count_c,'count_d':count_d,'count_e':count_e,'count_f':count_f,'count_a':count_a})

def photoshop(request):
    if 'USID' in request.session:
        categ=categories.objects.get(id=4)
        all=Product.objects.filter(category_id=4,product_status=1)
        price_low=Product.objects.filter(category_id=4,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=4,product_status=1).order_by('-price')
        return render(request,'category_photoshop.html',{'all':all,'three':price_low,'high_to':price_high,'categ':categ})
    else:
        categ=categories.objects.get(id=4)
        all=Product.objects.filter(category_id=4,product_status=1)
        price_low=Product.objects.filter(category_id=4,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=4,product_status=1).order_by('-price')
        return render(request,'photoshop_without_user.html',{'all':all,'three':price_low,'high_to':price_high,'categ':categ})

def ui_design(request):
    if 'USID' in request.session:
        categ=categories.objects.get(id=5)
        all=Product.objects.filter(category_id=5,product_status=1)
        price_low=Product.objects.filter(category_id=5,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=5,product_status=1).order_by('-price')
        return render(request,'category_uidesign.html',{'all':all,'three':price_low,'high_to':price_high,'categ':categ})
    else:
        categ=categories.objects.get(id=5)
        all=Product.objects.filter(category_id=5,product_status=1)
        price_low=Product.objects.filter(category_id=5,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=5,product_status=1).order_by('-price')
        return render(request,'ui_design_without_user.html',{'all':all,'three':price_low,'high_to':price_high,'categ':categ})
        

def house_plans(request):
    if 'USID' in request.session:
        categ=categories.objects.get(id=6)
        all=Product.objects.filter(category_id=6,product_status=1)
        price_low=Product.objects.filter(category_id=6,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=6,product_status=1).order_by('-price')
        return render(request,'category_houseplans.html',{'all':all,'three':price_low,'high_to':price_high,'categ':categ})
    else:
        categ=categories.objects.get(id=6)
        all=Product.objects.filter(category_id=6,product_status=1)
        price_low=Product.objects.filter(category_id=6,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=6,product_status=1).order_by('-price')
        return render(request,'houseplan_without_user.html',{'all':all,'three':price_low,'high_to':price_high,'categ':categ})
        

def logo_creation(request):
    if 'USID' in request.session:
        categ=categories.objects.get(id=7)
        all=Product.objects.filter(category_id=7,product_status=1)
        price_low=Product.objects.filter(category_id=7,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=7,product_status=1).order_by('-price')
        return render(request,'category_logo.html',{'all':all,'three':price_low,'high_to':price_high,'categ':categ})
    else:
        categ=categories.objects.get(id=7)
        all=Product.objects.filter(category_id=7,product_status=1)
        price_low=Product.objects.filter(category_id=7,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=7,product_status=1).order_by('-price')
        return render(request,'logo_without_user.html',{'all':all,'three':price_low,'high_to':price_high,'categ':categ})

def drawings(request):
    if 'USID' in request.session:
        categ=categories.objects.get(id=8)
        all=Product.objects.filter(category_id=8,product_status=1)
        price_low=Product.objects.filter(category_id=8,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=8,product_status=1).order_by('-price')
        return render(request,'category_drawings.html',{'all':all,'three':price_low,'high_to':price_high,'categ':categ})
    else:
        categ=categories.objects.get(id=8)
        all=Product.objects.filter(category_id=8,product_status=1)
        price_low=Product.objects.filter(category_id=8,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=8,product_status=1).order_by('-price')
        return render(request,'drawing_without_user.html',{'all':all,'three':price_low,'high_to':price_high,'categ':categ})



def model_two(request):
    all=Product.objects.all()
    three=Product.objects.filter(format='.3dx')
    return render(request, 'new_models_2.html',{'all':all,})

#.............price low to high .............

def price_low(request):
    if 'USID' in request.session:
        categ=categories.objects.get(id=1)
        default=Product.objects.filter(category_id=1,product_status=1)
        price_low=Product.objects.filter(category_id=1,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=1,product_status=1).order_by('-price')
        return render(request,'cat_price_low.html',{'three':price_low,'normal':default,'high':price_high,'categ':categ})
    else:
        default=Product.objects.filter(category_id=1,product_status=1)
        categ=categories.objects.get(id=1)
        price_low=Product.objects.filter(category_id=1,product_status=1).order_by('price')
        price_high=Product.objects.filter(category_id=1,product_status=1).order_by('-price')
        return render(request,'3dmodel_without_user.html',{'three':price_low,'normal':default,'high':price_high,'categ':categ})


def price_high(request):
    price_high=Product.objects.filter(category_id=1).order_by('-price')
    return render(request,'cat_price_high.html',{'three':price_high})
    

#.................category...3dx...................

def three(request):
    three=Product.objects.filter(format='.3dx',category_id=1)
    return render(request, 'cat_three_models.html',{'three':three})

#.................fbx..........................
def fbx(request):
    fbx=Product.objects.filter(format='.fbx',category_id=1)
    return render(request, 'cat_three_models.html',{'three':fbx})

#....................obj......................
def obj(request):
    obj=Product.objects.filter(format='.obj',category_id=1)
    return render(request, 'cat_obj_models.html',{'three':obj})


def product(request):
    return render(request, 'new_product.html')

def profile(request,pk):
    person=Register_freelance.objects.get(id=pk)
    return render(request, 'new_profile.html',{'p':person})

def freelancer(request):
    person=Register_freelance.objects.all()
    return render(request, 'new_freelancer.html',{'person':person})

def admin_log(request):
    return render(request, 'admin_log.html')


def freereg(request):
    cate=categories.objects.all()
    if request.method == 'POST':

        fullname=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['phone_number']
        profilepic=request.FILES['profile_picture']
        # addres=request.POST['address']
        # country=request.POST['country']
        username=request.POST['user_name']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

    
        if User.objects.filter(username=username):
            messages.info(request,'username already exists')
           
            return redirect('freereg')
        elif Register_freelance.objects.filter(username=username):
            messages.info(request,'username already exists') 
           
            return redirect('freereg')
        
        elif (password==cpassword):

            education=request.POST['quali']
            profi=request.POST['desi']
            total_exp=request.POST['Expirence']
            Resume=request.FILES['resume']
            overview=request.POST['overview']
            result=Register_freelance(full_name=fullname,
                                    email=email,
                                    mobile=mobile,
                                    profile_pic=profilepic,
                                    username=username,
                                    password=password,Resume=Resume,Total_exp=total_exp,
                                    over_view=overview,qualification=education,proffecional_title=profi)
            result.save()

            msg_reg="Registraion  successfull"
            return render(request,'free_lance_reg_second_form.html',{'msg_reg':msg_reg,'result':result,'cate':cate})
        else:
            messages.info(request,'Password Does not match') 
            return redirect('freereg')
        
    return render(request,'free_lance_reg.html',{'cate':cate})



def freelances_details_save(request):
    cate=categories.objects.all()
    if request.method == 'POST':
      
        pr_id = request.POST['perid']
    
        result=Register_freelance.objects.get(id=pr_id)
    

        service=request.POST['service']
        previous_work_1=request.FILES.get('first_work')
    
        previous_work_2=request.FILES.get('second_work')
        #previous_work_3=request.FILES.get('previous_work_3')

        result_other=FreelancerService(free_id=result,
                                work_2=previous_work_2,
                                work_1=previous_work_1,
                                service=service)
        result_other.save()
        msg_ser="Service Added."
        return render(request,'free_lance_reg_second_form.html',{'cate':cate,'result':result,'msg_ser':msg_ser})  
    else:
        return render(request,'free_lance_reg_second_form.html',{'cate':cate,'result':result})                         



def cartitem(request,pk):
    if 'USID' in request.session:
       k=request.session['USID']  
       prod=Product(id=pk)
       user1=User(id=k)
       std=cart(product=prod,
           User=user1,)
       std.save()
       return redirect('viewcart')
    return render('user_logout')

def delete_cart(requets,pk):
    std=cart.objects.get(id=pk)
    std.delete()
    return redirect('viewcart')

def viewcart(request):
    if 'USID' in request.session:
       pk=request.session['USID']  
       ca=cart.objects.filter(User=pk)
       co=cart.objects.filter(User=pk).count()
       total=0
       for p in ca:
         total+=int(p.product.price)
       return render(request,'cart.html',{'ca':ca,'total':total,'co':co})
    return redirect('user_logout')   

def view_items(request,pk):
    if 'USID' in request.session:
        k=request.session['USID']
        std=Product.objects.get(id=pk)
        new=Product.objects.filter(category=2)
        categ=categories.objects.get(category_name=std.category)
        if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']
            address=request.POST['address']
            phone=request.POST['phone']
            description=request.POST['desc']
            files=request.FILES.get('example_file')
            status='0'
            product=std
           
            service_freelancer='null'
            sfm=Service_form(user_name=name,
                            email=email,
                            Address=address,
                            phone_number=phone,
                            description=description,
                            status=status,
                            product=product.id,
                            file=files,
                            categori=product.category.category_name,
                            service_freelancer=service_freelancer,
                            )
            sfm.save()
            # messages.info(request,'Request sent succesfully')
            msg="Your Request Is Successful"
            return render(request,'view_item_2.html',{'std':std,'new':new,'msg':msg,'categ':categ})
        return render(request,'view_item_2.html',{'std':std,'new':new,'categ':categ})
    
    else:
        std=Product.objects.get(id=pk)
        new=Product.objects.filter(category=2)
        categ=categories.objects.get(category_name=std.category)
        if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']
            address=request.POST['address']
            phone=request.POST['phone']
            description=request.POST['desc']
            files=request.FILES.get('extra')
            status='0'
            product=std

            service_freelancer='null'
            sfm=Service_form(user_name=name,
                            email=email,
                            Address=address,
                            phone_number=phone,
                            description=description,
                            status=status,
                            file=files,
                            product=product.id,
                            categori=product.category.category_name,
                            service_freelancer=service_freelancer,
                            )
            sfm.save()
            # messages.info(request,'Request sent succesfully')
            msg="Your Request Is Successful"
            return render(request,'view_item_without_user.html',{'std':std,'new':new,'msg':msg,'categ':categ})
        return render(request,'view_item_without_user.html',{'std':std,'new':new,'categ':categ})


def Request_form(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        description=request.POST['description']
        categ=request.POST['cate']
        examp_file=request.FILES.get('example')
        status='0'
        std=Service_form(user_name=name,
                               email=email,
                               Address=address,
                               phone_number=phone,
                               description=description,
                               categori=categ,
                               status=status,
                               file=examp_file)
        std.save()
        if 'USID' in request.session:
            messages.success(request,'Success')
            return redirect('userhome')
        else:
            messages.success(request,'Success')
            return redirect('home')

        

def view_items_two(request,pk):
    if 'USID' in request.session:
        std=Product.objects.get(id=pk)
        new=Product.objects.filter(category=2)
        return render(request,'view_item.html',{'std':std,'new':new})
    else:
        std=Product.objects.get(id=pk)
        new=Product.objects.filter(category=2)
        return render(request,'view_item_2_without.html',{'std':std,'new':new})
        
  
    

def registration(request):
    it = categories.objects.all()
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                
                messages.info(request, 'username already exists')
                return redirect('registration')
            
            elif Register_freelance.objects.filter(username=username):
                messages.info(request, 'username already exists')
                return redirect('registration')
                
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                user.save()
                msg = "Registration Successfull"
                # messages.info(request, 'Registration successfully completed')
                return render(request,'registration.html',{'msg':msg})
        else:
            messages.info(request, 'password not matching')
            return redirect('registration')
   
    return render(request, 'registration.html',{'it':it})




def check_username(request):
    
        # Get the username from the request
        username = request.GET.get('username')

        # Check if the username exists in the database
        if User.objects.filter(username=username).exists() or Register_freelance.objects.filter(username=username):
            # If the username exists, return a JSON response indicating that it exists
            return JsonResponse({'exists': True})
        else:
            # If the username does not exist, return a JSON response indicating that it does not exist
            return JsonResponse({'exists': False})

def check_useremail(request):
    
        # Get the username from the request
        useremail = request.GET.get('useremail')

        # Check if the username exists in the database
        if User.objects.filter(email=useremail).exists() or Register_freelance.objects.filter(email=useremail):
            # If the username exists, return a JSON response indicating that it exists
            return JsonResponse({'exists': True})
        else:
            # If the username does not exist, return a JSON response indicating that it does not exist
            return JsonResponse({'exists': False})
        
        
#..................login..................................

def admin_login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # request.session["uid"] = user.id
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                request.session['admid']=user.id
                return redirect('admin_dashboard')
            else:
                request.session['USID']=user.id
                return redirect('userhome')      
        if Register_freelance.objects.filter(username=username,password=password):
            free=Register_freelance.objects.get(username=username,password=password) 
            request.session['F.id']=free.id
            return redirect('freelancer_home')
                        
        else:
           
            messages.info(request,'Invalid username or password.Try again!')
            return redirect('admin_log')
        messages.info(request, 'Invalid username or password')
   
    return redirect('admin_log')


def freelancer_home(request):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
        fr_ongoing=Freelancerworks.objects.filter(fr_status='2',frelancer_id=std).count
        fr_complete=Freelancerworks.objects.filter(fr_status='1',frelancer_id=std).count
        frwork=Freelancerworks.objects.filter(frelancer=free,fr_status='2')
        frworks=Freelancerworks.objects.filter(Q(fr_status='3') | Q(fr_status='1'),frelancer=free)
        return render(request,'freelance_home.html',{'p':free,'fr_ongoing':fr_ongoing,'fr_complete':fr_complete,'frwork':frwork,'frworks':frworks})
    return redirect('user_logout')


def freelancer_profile(request):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
        r=free.rating
        serv=FreelancerService.objects.filter(free_id=free)
        return render(request,'freelancer_profile.html',{'free':free,'serv':serv,'r':range(r)})
    return redirect('user_logout')

def free_edit_save(request,pk):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
        if request.method == 'POST':

            free.full_name=request.POST['name']
            free.email=request.POST['email']
            free.mobile=request.POST['phone_number']
            free.Address=request.POST['addre']
            free.qualification=request.POST['quali']
            free.proffecional_title=request.POST['profi']
            free.country=request.POST['country']
            free.over_view=request.POST['overview']
            
            if request.FILES.get('profile_picture'):
                free.profile_pic=request.FILES.get('profile_picture')
            else:
                free.profile_pic=  free.profile_pic
            
            free.save()
            return redirect('freelancer_profile')
        else:
            return redirect('freelancer_profile')
    return redirect('user_logout')

def free_service_delete(request,pk):
    serv=FreelancerService.objects.get(id=pk)
    serv.delete()
    return redirect('freelancer_profile')


def freelancer_password(request):
    if 'F.id' in request.session:
        std=request.session['F.id']
        fr=Register_freelance.objects.get(id=std)
        return render(request,'freelancer_password.html',{'fr':fr})
    return redirect('user_logout')


def free_password_change(request,pk):
    if request.method == 'POST':
        user=Register_freelance.objects.get(id=pk)
        user.username=request.POST['fr_user']
        user.password=request.POST['admin_newpsw']
        user.save()
        messages.info(request,'Old Password Changed To New')
        return redirect('freelancer_password')
    else:
        return redirect('freelancer_password')


def userhome(request):
    if 'USID' in request.session: 
       new=Product.objects.all().order_by('-id')[:3]
       special=Product.objects.all().order_by('id')[:3]
       feature=Product.objects.all().order_by('id')[3:6]
       count_a=Product.objects.filter(category_id=1).count()
       count_b=Product.objects.filter(category_id=4).count()
       count_c=Product.objects.filter(category_id=5).count()
       count_d=Product.objects.filter(category_id=6).count()
       count_e=Product.objects.filter(category_id=7).count()
       count_f=Product.objects.filter(category_id=8).count()
       persons=Register_freelance.objects.filter(ranking=1)
       return render(request, 'new_index2.html',{'new':new,'sp':special,'fea':feature,'count_b':count_b,'count_c':count_c,
           'count_d':count_d,'count_e':count_e,'count_f':count_f,'count_a':count_a,'persons':persons})
    return redirect('user_logout')


def admin_dashboard(request):
    if request.session.has_key('admid'):
        abc= request.session['admid']
        adm=User.objects.filter(id=abc)
        users = User.objects.all().count()
        models = Product.objects.all().count()


        # Notification Count
        req_date = Service_form.objects.filter(status='0',req_date=datetime.date.today()).count()
        msg_date = Messagebox.objects.filter(mg_date=datetime.date.today()).count()
        req_date_data=Service_form.objects.filter(status='0',req_date=datetime.date.today())
        msg_date_data= Messagebox.objects.filter(mg_date=datetime.date.today())
      


        req1 = Service_form.objects.filter(status='0').count()
        req2 = Service_form.objects.filter(Q(status='3') | Q(status='4')  | Q(status='5') ).count()
        req3 = Freelancerworks.objects.filter(fr_status='1').count()
        messg=Messagebox.objects.all().order_by('-id')
        return render(request, 'admin_dashboard.html',{'adm': adm, 'users': users, 'models': models,
            'messg':messg,'req':req1,'req2':req2,'req3':req3,'req_date':req_date,'msg_date':msg_date,
            'req_date_data':req_date_data,'msg_date_data':msg_date_data})
    
    return redirect('user_logout')


def admin_profile(request):
    abc= request.session['admid']
    adm=User.objects.filter(id=abc)
    adm1=User.objects.get(id=abc)
     # Notification Count
    req_date = Service_form.objects.filter(status='0',req_date=datetime.date.today()).count()
    msg_date = Messagebox.objects.filter(mg_date=datetime.date.today()).count()
    req_date_data=Service_form.objects.filter(status='0',req_date=datetime.date.today())
    msg_date_data= Messagebox.objects.filter(mg_date=datetime.date.today())
      
    return render(request, 'admin_profile.html',{'adm': adm,'req_date':req_date,'msg_date':msg_date,
            'req_date_data':req_date_data,'msg_date_data':msg_date_data,'adm1':adm1})

def admin_password_change(request,pk):
    if request.method == 'POST':
        psw=request.POST['admin_newpsw']
        user=User.objects.get(id=pk)
        user.set_password(psw)
        user.save()
        messages.info(request,'Old Password Changed To New')
        return redirect('admin_profile')
    else:
        return redirect('admin_profile')



def messge_remove(request,pk):
    messg=Messagebox.objects.filter(id=pk)
    messg.delete()
    return redirect('admin_dashboard')


def models_show(request):
    abc= request.session['admid']
    adm=User.objects.filter(id=abc)
    all=Product.objects.all()

    # Notification Count
    req_date = Service_form.objects.filter(status='0',req_date=datetime.date.today()).count()
    msg_date = Messagebox.objects.filter(mg_date=datetime.date.today()).count()
    req_date_data=Service_form.objects.filter(status='0',req_date=datetime.date.today())
    msg_date_data= Messagebox.objects.filter(mg_date=datetime.date.today())
      
    return render(request, 'models.html',{'adm': adm,'all':all,'req_date':req_date,'msg_date':msg_date,
            'req_date_data':req_date_data,'msg_date_data':msg_date_data})


def admin_log(request):
    it = categories.objects.all()
    request.session.flush()
    return render(request, 'admin_log.html',{'it':it})

# def admin_dashboard(request):
#     if 'admid' in request.session:
#         if request.session.has_key('admid'):
#             admid = request.session['admid']
#         else:
#             return redirect('/')
#         adm = Admin_register.objects.filter(reg_id=admid)
#         users = Admin_register.objects.all().count()
#         models = Product.objects.all().count()
#         return render(request, 'admin_dashboard.html', {'adm': adm, 'users': users, 'models': models,})
#     else:
#         return redirect('/')

def user_logout(request):
    request.session.flush()
    return redirect('admin_log')


def buyNow(request, id):
    model = Product.objects.get(id=id)
    it = categories.objects.all()
    SAdm_id = request.session['SAdm_id']
    member = User.objects.get(id=SAdm_id)
    return render(request, 'buynow.html', {'model': model,'it':it, 'member': member,})

def buyNownotloged(request, id):
    model = Product.objects.get(id=id)
    it = categories.objects.all()

    return render(request, 'buynownotloged.html', {'model': model,'it':it,})

def saveform(request):
    if request.method=='POST':
        
        nm=request.POST['name']
        mb=request.POST['mobile']
        el=request.POST['email']
        cg=request.POST['catg']
        im=request.POST['itm']
        pc=request.POST['price']
        mg=request.POST['message']
        
        std=oders(
            name=nm,
            mobile=mb,
            email=el,
            catag=cg,
            item=im,
            price=pc,
            mesg=mg,

                    )
        std.save()
        print("hii")
        return render(request,'submited.html') 


def orderlist(request):
    obj=oders.objects.all()
    context={'msg':obj}
    return render(request,'orderlist.html',context) 

def new_page(request, id):
    
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        member = User.objects.get(id=SAdm_id)
        products = Product.objects.all()
        it = categories.objects.all()
        data = cartData(request)
        cartItems = data['cartItems']
        man1 = Product.objects.filter(category_id=id)
        man = categories.objects.filter(cat_id=id)
        sub = SubCategory.objects.all()
        # return render(request, 'new_page.html', {'it':it,'products':products,'cartItems':cartItems,'man': man, 'man1': man1})
        return render(request, 'new_page.html', {'sub':sub,'it':it,'products':products,'cartItems':cartItems,'man': man, 'man1': man1,'member':member})
    # else:
    #         return redirect('/')



def new_page2(request, id):
    # member = User.objects.get(id=SAdm_id)
    products = Product.objects.all()
    it = categories.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    man1 = Product.objects.filter(category_id=id)
    man = categories.objects.filter(cat_id=id)
    sub = SubCategory.objects.all()
        # return render(request, 'new_page.html', {'it':it,'products':products,'cartItems':cartItems,'man': man, 'man1': man1})
    return render(request, 'new_page2.html', {'sub':sub,'it':it,'products':products,'cartItems':cartItems,'man': man, 'man1': man1})

def sub(request, id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    member = User.objects.get(id=SAdm_id)
    products = Product.objects.all()
    it = categories.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    man1 = Product.objects.filter(subcategory_id=id)
    man = categories.objects.filter(cat_id=id)
    subcate = SubCategory.objects.filter(id=id)
    sub1 = SubCategory.objects.all()
    return render(request, 'sub.html', {'subcate':subcate,'it':it,'data':data,'cartItems':cartItems,'member':member,'products':products,'sub':sub1,'man': man, 'man1': man1})


def Signup_emailval(request):
    email = request.GET.get('email', None)
 
    data = {
        'is_taken': Admin_register.objects.filter(email=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Email already exists.'
    return JsonResponse(data)

def registration(request):
    it = categories.objects.all()
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                return redirect('admin_log')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                user.save()
                msg_success = "Registration Successfull"
                messages.info(request, 'Registration successfully completed')
                return render(request,'registration.html',{'msg_success':msg_success})
        else:
            messages.info(request, 'password not matching')
            return redirect('registration')
   
    return render(request, 'registration.html',{'it':it})






def admin_logout(request):
    if 'admid' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def admin_settings(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        return render(request, 'admin_settings.html', {'adm': adm})
    else:
        return redirect('/')

def admin_edit_profile(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        if request.method == 'POST':
            abb = Admin_register.objects.get(reg_id=admid)
            abb.fullname = request.POST['fullname']
            abb.email = request.POST['email']
            abb.username = request.POST['username']
            abb.save()
            return redirect("admin_settings")
        return render(request, 'admin_edit_profile.html', {'adm': adm})
    else:
        return redirect('/')

def admin_edit_picture(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        if request.method == 'POST':
            abb = Admin_register.objects.get(reg_id=admid)
            abb.photo = request.FILES['img']
            abb.save()
            return redirect("admin_settings")
        return render(request, 'admin_edit_picture.html', {'adm': adm})
    else:
        return redirect('/')

def admin_edit_password(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        if request.method == 'POST':
            ac = Admin_register.objects.get(reg_id=admid)
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    ac.password = request.POST.get('confirmPassword')
                    ac.save()
                    msg_success = "Password changed successfully"
                    return render(request, 'admin_settings.html', {'msg_success': msg_success})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
        return render(request, 'admin_edit_password.html', {'adm': adm})
    else:
        return redirect('/')



def show_category(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        caty = categories.objects.all()
        return render(request, 'categories.html', {'caty': caty,'adm':adm})
    else:
        return redirect('/')

def Sub_categories(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        cate = categories.objects.all()
        subcate = SubCategory.objects.all()
        return render(request, 'Sub_categories.html', {'subcate':subcate,'caty': cate,'adm':adm})
    else:
        return redirect('/')

def add_category(request):
    try:

        if request.method == 'POST':
            category_name = request.POST['category_name']
            category_logo = request.FILES['category_logo']
            # sub_category1 = request.POST['sub_category1']
            # strippeddata1 = sub_category1.replace(" ", "")
            # sub_category2 = request.POST['sub_category2']
            # strippeddata2 = sub_category2.replace(" ", "")
            # sub_category3 = request.POST['sub_category3']
            # strippeddata3 = sub_category3.replace(" ", "")
            # sub_category4 = request.POST['sub_category4']
            # strippeddata4 = sub_category4.replace(" ", "")
            # sub_category5 = request.POST['sub_category5']
            # strippeddata5 = sub_category5.replace(" ", "")
            cat = categories(category_name=category_name, category_logo=category_logo)
            # cat = categories(category_name=category_name, category_logo=category_logo, sub_category1=strippeddata1,
            #                  sub_category2=strippeddata2, sub_category3=strippeddata3, sub_category4=strippeddata4, sub_category5=strippeddata5)
            cat.save()

            return redirect('category')
        else:
            return redirect('categories')
    except:
        return redirect('categories')

def add_subcategory(request):
        if request.method == 'POST':
            abc = SubCategory()
            abc.category_id  = request.POST['category']
            abc.subcategory = request.POST['subcategory']
            abc.save()
            msg_success = "Added successfull"
            return render(request, 'Sub_categories.html', {'msg_success': msg_success})
        return render(request, 'Sub_categories.html',) 
            

def cat_delete(request, cat_id):

    emp = categories.objects.get(cat_id=cat_id)
    emp.delete()
    return redirect('category')

def subcat_delete(request, id):
    
    emp = SubCategory.objects.get(id=id)
    emp.delete()
    return redirect('Sub_categories')


def admin_models(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        return render(request, 'admin_models.html',{'adm':adm})
    else:
        return redirect('/')


def addmodel(request):
    abc= request.session["admid"]
    adm=User.objects.filter(id= abc)
    var = categories.objects.all()

    # Notification Count
    req_date = Service_form.objects.filter(status='0',req_date=datetime.date.today()).count()
    msg_date = Messagebox.objects.filter(mg_date=datetime.date.today()).count()
    req_date_data=Service_form.objects.filter(status='0',req_date=datetime.date.today())
    msg_date_data= Messagebox.objects.filter(mg_date=datetime.date.today())

    return render(request, "addmodel.html", {'var': var,'adm':adm,'req_date':req_date,
        'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})


def createmodel(request):
    if request.method == 'POST':

        modelname = request.POST['modelname']
        description = request.POST['description']
        gib = request.FILES['gib']
        price = request.POST['price']
        types = request.POST['types']
        format = request.POST['format']
        modeltype = request.POST['modeltype']
        category = request.POST['category']
        rating = request.POST['rate']
        # fbx = request.FILES['fbx']

        item = Product(modelname=modelname, description=description, gib=gib, price=price, 
            types=types, format=format, modeltype=modeltype, category_id=category,rating=rating,product_status=1)
        item.save()
        return redirect('addmodel')
    else:
        return redirect('createmodel')

def edit_model(request,pk):
    abc= request.session["admid"]
    adm=User.objects.filter(id= abc)
    var = categories.objects.all()
    item = Product.objects.get(id=pk)

    # Notification Count
    req_date = Service_form.objects.filter(status='0',req_date=datetime.date.today()).count()
    msg_date = Messagebox.objects.filter(mg_date=datetime.date.today()).count()
    req_date_data=Service_form.objects.filter(status='0',req_date=datetime.date.today())
    msg_date_data= Messagebox.objects.filter(mg_date=datetime.date.today())

    return render(request, "edit_model.html", {'var': var,'adm':adm,'item':item,
'req_date':req_date,'msg_date':msg_date,
            'req_date_data':req_date_data,'msg_date_data':msg_date_data})



def approve_model(request,pk):
    item = Product.objects.get(id=pk)
    item.product_status=1
    item.save()
    return redirect('models_show')
   


def edit_save_model(request,pk):
    if request.method == 'POST':
        item= Product.objects.get(id=pk)
        item.modelname = request.POST['modelname']
        item.description = request.POST['description']

        img = request.FILES.get('gib')
        if img:
           item.gib=img
        else:
              item.gib= item.gib
        item.price = request.POST['price']
        item.types = request.POST['types']
        item.format = request.POST['format']
        item.modeltype = request.POST['modeltype']
        item.rating = request.POST['edit_rate']
        cate=categories.objects.get(category_name= request.POST['category'])
        item.category_id =cate
        item.save()
        return redirect('models_show')


def admin_payment_history(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        return render(request, 'admin_payment_history.html',{'adm':adm})
    else:
        return redirect('/')


def payment_table(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        var = payment.objects.all()
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            var = payment.objects.filter(date__range=[fromdate, todate])
        return render(request, 'payment_table.html', {'var': var,'adm':adm})
    else:
        return redirect('/')


def registeredusers(request):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    # Notification Count
    req_date = Service_form.objects.filter(status='0',req_date=datetime.date.today()).count()
    msg_date = Messagebox.objects.filter(mg_date=datetime.date.today()).count()
    req_date_data=Service_form.objects.filter(status='0',req_date=datetime.date.today())
    msg_date_data= Messagebox.objects.filter(mg_date=datetime.date.today())
    use = User.objects.filter(is_superuser=0)
    return render(request, 'registeredusers.html', {'use': use,'adm':adm,'req_date':req_date,
        'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})
    


def delete(request, reg_id):
    admid = request.session['admid']
    use = Admin_register.objects.get(reg_id=reg_id)
    use.delete()
    return redirect('registeredusers')


def adminedit(request, id):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        item = Product.objects.filter(id=id)
        viva = categories.objects.all()
        return render(request, "adminedit.html", {'item': item, 'viva': viva})
    else:
        return redirect('/')

def admin_editmodel(request, id):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        item = Product.objects.filter(id=id)
        viva = categories.objects.all()
        return render(request, "admin_editmodel.html", {'item': item, 'viva': viva})
    else:
        return redirect('/')


def admin_current_models(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        category = categories.objects.all()
        item = Product.objects.all()
        return render(request, 'admin_current_models.html', {'category': category, 'item': item,'adm':adm})
    else:
        return redirect('/')


def model_delete(request, id):
    abc = Product.objects.get(id=id)
    abc.delete()
    return redirect('admin_current_models')


def modeledit(request, id):
    if request.session['admid'] == "":
        return redirect('logout')
    else:
        if request.method == "POST":
            item = Product.objects.get(id=id)
            item.modelname = request.POST.get('modelname', item.modelname)
            item.description = request.POST.get('description', item.description)
            item.gib = request.FILES.get('gib', item.gib)
            item.price = request.POST.get('price', item.price)
            item.types = request.POST.get('types', item.types)
            item.format = request.POST.get('format', item.format)
            item.modeltype = request.POST.get('modeltype', item.modeltype)
            item.category_id = request.POST.get('category_name', item.category_id)
            item.fbx = request.FILES.get('fbx', item.fbx)

            item.save()
            return redirect('admin_current_models')






# def login(request):
#     if request.method == 'POST':
#         username  = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username,password=password)
#         if user is not None:
#             request.session['SAdm_id'] = user.id
#             return redirect('store')
        

        # elif Admin_register.objects.filter(username=request.POST['username'], password=request.POST['password'], designation="user").exists():
        #     member = Admin_register.objects.get(
        #         username=request.POST['username'], password=request.POST['password'])
        #     request.session['userid'] = member.reg_id
        #     return redirect('userhome')

#         else:
#             return redirect('login')
#     else:
#          return render(request,'login.html')

# def logout(request):
#     if 'user' in request.session:
#         request.session.flush()
#         return redirect('/')
#     else:
#         return redirect('/')

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)


def cart_item(request):
    # if 'SAdm_id' in request.session:
    #     if request.session.has_key('SAdm_id'):
    #         SAdm_id = request.session['SAdm_id']
    #     else:
    #         return redirect('/')
    #     it = categories.objects.all()
    #     member = User.objects.get(id=SAdm_id)
    #     data = cartData(request)
    #     print(data['cartItems'])
    #     cartItems = data['cartItems']
    #     order = data['order']
    #     items = data['items']

    #     context = {'items':items, 'order':order, 'cartItems':cartItems,'member':member,'it':it,}
    return render(request, 'cart.html')

def checkout(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		member = User.objects.get(id=SAdm_id)
		data = cartData(request)
		it = categories.objects.all()
		cartItems = data['cartItems']
		order = data['order']
		items = data['items']

		context = {'items':items, 'order':order, 'cartItems':cartItems,'member':member,'it':it}
		return render(request, 'checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
    print("name")
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)

def newcart(request):
    return render(request,'newcart.html')

def request(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        
        member = User.objects.get(id=SAdm_id)
        it = categories.objects.all()
        return render(request, 'request.html',{'it': it, 'member': member})
    

def request_not_logedin(request):
    it = categories.objects.all()
    return render(request,'nologrequest.html',{'it':it})

def reqlist(request):
    re=Request.objects.all()
 
    return render(request,'requestli.html',{'re':re})


def savereq(request):
    if request.method=='POST':
        n=request.POST.get('name')
        nu=request.POST.get('number')
        em=request.POST.get('email')
        at=request.POST.get('about')
        images=request.FILES.get('image')
        req=Request(name=n, mobile=nu, email=em, about=at, image=images)
        req.save()
        return redirect('home')

def deletereq(request,id):
    re=Request.objects.get(id=id)
    re.delete()
    return redirect('reqlist')




def freelancers(request):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    person=FreelancerService.objects.all()
    # Notification Count
    req_date = Service_form.objects.filter(status='0',req_date=datetime.date.today()).count()
    msg_date = Messagebox.objects.filter(mg_date=datetime.date.today()).count()
    req_date_data=Service_form.objects.filter(status='0',req_date=datetime.date.today())
    msg_date_data= Messagebox.objects.filter(mg_date=datetime.date.today())

    return render(request, 'freelancers.html', {'person': person,'adm':adm,'req_date':req_date,
        'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})


def freelancer_page(request,freel_id):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    person=Register_freelance.objects.get(id=freel_id)
    r= int(person.rating)
    fr_ongoing=Freelancerworks.objects.filter(fr_status='2',frelancer_id=freel_id).count
    fr_complete=Freelancerworks.objects.filter(fr_status='1',frelancer_id=freel_id).count
    fr=Freelancerworks.objects.filter(frelancer_id=freel_id)
    return render(request, 'freelancer.html', {'person': person,'adm':adm,'r':range(r),'fr_ongoing':fr_ongoing,'fr_complete':fr_complete,'fr':fr})


def rating(request,freel_rt):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    person=Register_freelance.objects.get(id=freel_rt)
    if request.method=='POST':
        person.rating=request.POST['rt']
        person.save()  
    return redirect('freelancers')

#Requested works loading

def requested_work(request):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    s=Service_form.objects.all().order_by('-id')
    serv=Freelancerworks.objects.all()
    r=Register_freelance.objects.all()

    # Notification Count
    req_date = Service_form.objects.filter(status='0',req_date=datetime.date.today()).count()
    msg_date = Messagebox.objects.filter(mg_date=datetime.date.today()).count()
    req_date_data=Service_form.objects.filter(status='0',req_date=datetime.date.today())
    msg_date_data= Messagebox.objects.filter(mg_date=datetime.date.today())

    return render(request, 'requested_work.html', {'adm':adm,'r':r,'s':s,'serv':serv,
        'req_date':req_date,'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})

def request_reject(request,pk):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    s=Service_form.objects.get(id=pk)
    s.delete()

    return redirect('requested_work')


def ongoing_work(request):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    s=Service_form.objects.all().order_by('-id')

    # Notification Count
    req_date = Service_form.objects.filter(status='0',req_date=datetime.date.today()).count()
    msg_date = Messagebox.objects.filter(mg_date=datetime.date.today()).count()
    req_date_data=Service_form.objects.filter(status='0',req_date=datetime.date.today())
    msg_date_data= Messagebox.objects.filter(mg_date=datetime.date.today())
    fr=Freelancerworks.objects.all()
    return render(request, 'ongoing_work.html', {'adm':adm,'s':s,'req_date':req_date,'msg_date':msg_date,
        'req_date_data':req_date_data,'msg_date_data':msg_date_data,'fr':fr})



def Change_status_form(request,pk):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    s=Service_form.objects.get(id=pk)
    return render(request, 'work_status_change.html', {'adm':adm,'s':s})

def Change_status_save(request,pk):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    if request.method=='POST':
        n=request.POST['ser_des']
        nu=request.POST['ser_date']
        images=request.FILES.get('ser_file')
        s=Service_form.objects.get(id=pk)
        serv=Freelancerworks.objects.get(fr_service_id=s.id)
        fr=Register_freelance.objects.get(id=serv.frelancer.id)
        fr.w_status=1
        fr.save()
        serv.fr_status=6
        serv.fr_desecr=n
        serv.end_date=nu
        serv.save()
        if images:
            s.file=images
        else:
            s.file=s.file
        s.status=5
        s.save()
        return redirect('ongoing_work')
    

def complete_job(request,pk):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
  
    s=Service_form.objects.get(id=pk)
    fr_work=Freelancerworks.objects.get(fr_service_id=s.id)
    fr=Register_freelance.objects.get(id=fr_work.frelancer.id)
    s.status=1
    s.save()
    fr_work.fr_status=1
    fr_work.save()
    frwrk=Freelancerworks.objects.filter(Q(fr_status='2') | Q(fr_status='3')| Q(fr_status='5'),frelancer=fr)
    if frwrk:
        fr.w_status='1'
        fr.save()
    else:
        fr.w_status='0'
        fr.save()
   
    return redirect('ongoing_work')


def completed_work(request):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    fr=Freelancerworks.objects.filter(fr_status='1')

    # Notification Count
    req_date = Service_form.objects.filter(status='0',req_date=datetime.date.today()).count()
    msg_date = Messagebox.objects.filter(mg_date=datetime.date.today()).count()
    req_date_data=Service_form.objects.filter(status='0',req_date=datetime.date.today())
    msg_date_data= Messagebox.objects.filter(mg_date=datetime.date.today())

    return render(request, 'completed_work.html', {'adm':adm,'fr':fr,'req_date':req_date,
        'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})

#Freelancer Allocate

def freelancer_allocate(request):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    
    if request.method == 'POST':
        sr=Service_form.objects.get(id=int(request.POST['u-id']))
        work=Freelancerworks()
        work.fr_categori=sr.categori
        work.fr_user=sr.user_name
        work.fr_product=sr.product
        work.fr_service_id=sr.id
        work.frelancer=Register_freelance.objects.get(id=int(request.POST['frid']))
        work.end_date=request.POST['fr-date']
        work.fr_desecr =request.POST['admin_dese']
        work.fr_status=2
        work.save()
        msg='Successfuly Allocated'
        
        sr.status=2
        sr.save()
        fr_st=Register_freelance.objects.get(id=int(request.POST['frid']))
        fr_st.w_status=1
        fr_st.save()
        s=Service_form.objects.all()
        return redirect('requested_work')


#freelancer Work Section page

def freelancer_work(request):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
        #frwork=Freelancerworks.objects.filter(frelancer=free,fr_status='2').order_by('-id')
        frworks=Freelancerworks.objects.filter(Q(fr_status='3') | Q(fr_status='6') ,frelancer=free).order_by('-id')
        return render(request, 'freelancer_works.html', {'free':free,'frworks':frworks})
    
def freelancer_completed_work(request):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
      
        frworks=Freelancerworks.objects.filter(fr_status='1',frelancer=free).order_by('-id')
        return render(request, 'freelancer_comleted_works.html', {'free':free,'frworks':frworks})
    
def freelancer_product(request):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
        prodt=Product.objects.filter(fr_id=std)
        var = categories.objects.all()
        return render(request, 'freelancer_products.html', {'free':free,'prodt':prodt,'var':var})


def freelancer_product_remove(request,pk):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
        prodt=Product.objects.get(id=pk)
        prodt.delete()
        prodt=Product.objects.filter(fr_id=std)
        var = categories.objects.all()
        return render(request, 'freelancer_products.html', {'free':free,'prodt':prodt,'var':var})
    

def Freelancer_product_add(request):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
        if request.method == 'POST':

            modelname = request.POST['frmodelname']
            description = request.POST['frdescription']
            gib = request.FILES['frgib']
            price = request.POST['frprice']
            types = request.POST['frtypes']
            format = request.POST['frformat']
            modeltype = request.POST['frmodeltype']
            category = request.POST['frcategory']
          
            # fbx = request.FILES['fbx']

            item = Product(modelname=modelname, description=description, gib=gib, price=price, 
                types=types, format=format, modeltype=modeltype, category_id=category,rating=0,fr_id=std)
            item.save()
        prodt=Product.objects.filter(fr_id=std)
        var = categories.objects.all()
        return render(request, 'freelancer_products.html', {'free':free,'prodt':prodt,'var':var})

    
def freelancer_work_accept(request,fr_wstatus):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
        frwork=Freelancerworks.objects.get(id=fr_wstatus)
        frwork.fr_status='3'
        frwork.save()
        msg='Successfuly Accepted the work.'
        serv=Service_form.objects.get(id=frwork.fr_service_id)
        serv.status='3'
        serv.save()
        frwork=Freelancerworks.objects.filter(frelancer=free,fr_status='2')
        frworks=Freelancerworks.objects.filter(Q(fr_status='3') | Q(fr_status='1'),frelancer=free)
        return render(request, 'freelance_home.html', {'free':free,'frworks':frworks,'msg':msg,'frwork':frwork,})
    
def freelancer_work_reject(request,fr_wrejejct):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
        free.w_status='0'
        free.save()
        frwork=Freelancerworks.objects.get(id=fr_wrejejct)
        frwork.fr_status='4'
        frwork.save()
        rej='Successfuly Rejected the work.'
        serv=Service_form.objects.get(id=frwork.fr_service_id)
        serv.status='0'
        serv.save()
        frwork=Freelancerworks.objects.filter(frelancer=free,fr_status='2')
        frworks=Freelancerworks.objects.filter(Q(fr_status='3') | Q(fr_status='1'),frelancer=free)
        return render(request, 'freelance_home.html', {'free':free,'frworks':frworks,'rej':rej,'frwork':frwork})

def freelancer_workfile_submit(request,fr_workfile):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
        if  request.method == 'POST':
            files= request.FILES.get('work_file')
            frwork=Freelancerworks.objects.get(id=fr_workfile)
            frwork.fr_status='5'
            frwork.fr_file =files
            frwork.submitte_date=datetime.date.today()
            frwork.save()
            file_msg='Successfuly Uploaded the work File.'
            serv=Service_form.objects.get(id=frwork.fr_service_id)
            serv.status='4'
            serv.save()
            
            frwrk=Freelancerworks.objects.filter(Q(fr_status='2') | Q(fr_status='3')| Q(fr_status='5'),frelancer=free)
            if frwrk:
                free.w_status='1'
                free.save()
            else:
                free.w_status='0'
                free.save()
            frworks=Freelancerworks.objects.filter(fr_status='3',frelancer=free).order_by('-id')
            return render(request, 'freelancer_works.html', {'free':free,'frworks':frworks,'file_msg':file_msg})
        

def rework_details(request,pk):
    if 'F.id' in request.session:
        std=request.session['F.id']
        free=Register_freelance.objects.get(id=std)
        frworks=Freelancerworks.objects.get(id=pk)
        s=Service_form.objects.all()
        p=Product.objects.all()
        return render(request, 'rework_details.html', {'free':free,'frworks':frworks,'s':s,'p':p})



# user uploaded design file view

def uploaded_design_view(request,pk):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    s=Service_form.objects.get(id=pk)
    p=Product.objects.all()
    c=FreelancerService.objects.filter(service=s.categori).values_list('free_id', flat=True)
    r=Register_freelance.objects.filter(w_status='0',id__in=c)
    fr=Freelancerworks.objects.all()
    return render(request, 'user_design_file.html', {'adm':adm,'s':s,'p':p,'r':r,'fr':fr})


def products(request):
    all=Product.objects.filter(category_id=6)
    return render(request, 'footer.html',{'all':all})


def send_message(request):
    if request.method =='POST':
        send_msg=Messagebox()
        send_msg.name= request.POST['name']
        send_msg.email= request.POST['email']
        send_msg.phno= request.POST['phone']
        send_msg.company_name= ''
        send_msg.messag= request.POST['message']
        send_msg.files= request.FILES.get('file-img')
        send_msg.save()
        messages.info(request,'Thank you for your Time, We will catch you soon..')
        if 'USID' in request.session:
            return redirect('contact_two')  
        else: 
         return redirect('contact')   
    
    else:
        if 'USID' in request.session:
            return redirect('contact_two')  
        else: 
            return redirect('contact')   
        
    
def add_toplist(request,pk):
    person=Register_freelance.objects.get(id=pk)
    person.ranking=1
    person.save()
    return redirect('freelancer_page',pk)


def remove_toplist(request,pk):
    person=Register_freelance.objects.get(id=pk)
    person.ranking=0
    person.save()
    return redirect('freelancer_page',pk)


def sortby_freelances(request,pk):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    req_date = Service_form.objects.filter(status='0',req_date=datetime.date.today()).count()
    msg_date = Messagebox.objects.filter(mg_date=datetime.date.today()).count()
    req_date_data=Service_form.objects.filter(status='0',req_date=datetime.date.today())
    msg_date_data= Messagebox.objects.filter(mg_date=datetime.date.today())

    if pk==1:
    
        person=FreelancerService.objects.filter(service='UI DESIGN')
        return render(request, 'freelancers.html', {'person': person,'adm':adm,'req_date':req_date,
        'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})
    
    elif pk==2:

        person=FreelancerService.objects.filter(service='PHOTOSHOP')
        return render(request, 'freelancers.html', {'person': person,'adm':adm,'req_date':req_date,
        'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})
    
    elif pk==3:
        person=FreelancerService.objects.filter(service='HOUSE PLANS')
        return render(request, 'freelancers.html', {'person': person,'adm':adm,'req_date':req_date,
        'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})
    
    elif pk==4:
       
        person=FreelancerService.objects.filter(service='LOGO CREATION')
        return render(request, 'freelancers.html', {'person': person,'adm':adm,'req_date':req_date,
        'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})
    
    elif pk==5:
       
        person=FreelancerService.objects.filter(service='DRAWINGS')
        return render(request, 'freelancers.html', {'person': person,'adm':adm,'req_date':req_date,
        'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})
    
    elif pk==6:
       
        person=FreelancerService.objects.filter(service='3D')
        return render(request, 'freelancers.html', {'person': person,'adm':adm,'req_date':req_date,
        'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})
    
    elif pk==7:
        
        person=FreelancerService.objects.filter(service='OTHER')
        return render(request, 'freelancers.html', {'person': person,'adm':adm,'req_date':req_date,
        'msg_date':msg_date,'req_date_data':req_date_data,'msg_date_data':msg_date_data})
    
def sortby_catagery(request,pk):

    if pk==1:
        cate=categories.objects.get(category_name='UI DESIGN')
        all=Product.objects.filter(category=cate)
        return render(request,'model_list.html',{'all':all})
    elif pk==2:
        cate=categories.objects.get(category_name='PHOTOSHOP')
        all=Product.objects.filter(category=cate)
       
        return render(request,'model_list.html',{'all':all})
    elif pk==3:
        cate=categories.objects.get(category_name='HOUSE PLANS')
        all=Product.objects.filter(category=cate)
    
        return render(request,'model_list.html',{'all':all})
    elif pk==4:
        cate=categories.objects.get(category_name='LOGO CREATION')
        all=Product.objects.filter(category=cate)
      
        return render(request,'model_list.html',{'all':all})
    elif pk==5:
        cate=categories.objects.get(category_name='DRAWINGS')
        all=Product.objects.filter(category=cate)
       
        return render(request,'model_list.html',{'all':all})
    elif pk==6:
        cate=categories.objects.get(category_name='3D')
        all=Product.objects.filter(category=cate)
       
        return render(request,'model_list.html',{'all':all})
    
def remove_model(request,pk):
    abc= request.session['admid']
    adm=User.objects.filter(id=abc)
    pro=Product.objects.get(id=pk)
    pro.delete()
    return redirect('models_show')

    
  
def freelances_details(request):
  
    serfr=FreelancerService.objects.get(id=request.GET.get('persid'))
    per=Register_freelance.objects.get(id=serfr.free_id.id)
    r= int(per.rating)
    fr_ongoing=Freelancerworks.objects.filter(fr_status='2',frelancer=per.id).count
    fr_complete=Freelancerworks.objects.filter(fr_status='1',frelancer=per.id).count
    fr_servi=FreelancerService.objects.all()
    return render(request,'freelancers_details.html',{'per':per,'r':range(r),'fr_ongoing':fr_ongoing,'fr_complete':fr_complete,'fr_servi':fr_servi})


def freelancer_delete(request,pk):
    fr=Register_freelance.objects.get(id=pk)
    if fr.w_status==0:
        fr.delete()
    else:
        messages.error(request,'Freelancer {} is already assigned a work'.format(fr.full_name))
    return redirect('freelancers')


def freelances_job_details(request):
    detail_id = request.GET.get('persid')
    job=Freelancerworks.objects.get(id=detail_id)
    serv=Service_form.objects.all()
    return render(request,'freelanser_job_details.html',{'job':job,'serv':serv})


def user_delete(request,pk):
    user=User.objects.get(id=pk)
    user.delete()
    return redirect('registeredusers')



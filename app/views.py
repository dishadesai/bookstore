from django.shortcuts import render,HttpResponseRedirect,redirect,reverse
from .models import *
from random import randint
# Create your views here.
def Indexpage(request):
    return render(request,"app/index.html")

def Afterlogincust(request):
    return render(request,"app/index-5.html")

def Afterloginsup(request):
    return render(request,"app/suplier/index.html")   

def LoginRegisterPage(request):
    return render (request,"app/login-register.html")

def RegCustomer(request):
    if request.POST['role']=="Customer":
        role=request.POST['role']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        psw=request.POST['psw']
        cpsw=request.POST['cpsw']

        user=User.objects.filter(Email=email)
        if user:
            message="User Already Exists"
            return render(request,"app/login-register.html",{'msg':message})
        else:
            if psw==cpsw:
                otp=randint(100000,999999)
                newuser=User.objects.create(Email=email,Role=role,Password=psw,OTP=otp)
                newcustomer=Customer.objects.create(user_id=newuser,Firstname=fname,Lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
            else:
                message="Password and Confirm Password Doesnot Match"
                return render(request,"app/login-register.html",{'msg':message})

    elif request.POST['role']=="Suplier":
        role=request.POST['role']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        psw=request.POST['psw']
        cpsw=request.POST['cpsw']

        user=User.objects.filter(Email=email)
        if user:
            message="User Already Exists"
            return render(request,"app/login-register.html",{'msg':message})
        else:
            if psw==cpsw:
                otp=randint(100000,999999)
                newuser=User.objects.create(Email=email,Role=role,Password=psw,OTP=otp)
                newsuplier=Suplier.objects.create(user_id=newuser,Firstname=fname,Lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
            else:
                message="Password and Confirm Password Doesnot Match"
                return render(request,"app/login-register.html",{'msg':message})


def OTPverify(request):
    otp= int(request.POST['otp'])
    email=request.POST['email']
    user=User.objects.get(Email=email)
    
    if user.OTP == otp :
        message="OTP verified Successfully"
        return render(request,"app/login-register.html",{'msg':message})
        
    

    else:
        message="OTP verification Unsuccessful"
        return render(request,"app/otpverify.html",{'msg':message})


def LoginUser(request):
    if request.POST['role'] == "Customer":
        email=request.POST['email']
        password=request.POST['psw']

        user=User.objects.get(Email=email)

        if user:
            if user.Password==password:
                cust=Customer.objects.get(user_id=user)
                request.session['Firstname']=cust.Firstname
                request.session['Lastname']=cust.Lastname
                request.session['id']=user.id
                request.session['Role']=user.Role
                request.session['email']=user.Email
                request.session['password']= user.Password
                return redirect('afterlogincust')
            else:
                message="Password is incorrect"
                return render(request,"app/login-register.html",{'msg':message})
    elif request.POST['role'] == "Suplier":
        email=request.POST['email']
        password=request.POST['psw']

        user=User.objects.get(Email=email)
        if user:
            if user.Password==password:
                sup=Suplier.objects.get(user_id=user)
                request.session['Firstname']=sup.Firstname
                request.session['Lastname']=sup.Lastname
                request.session['id']=user.id
                request.session['Role']=user.Role
                request.session['email']=user.Email
                request.session['password']= user.Password
                return redirect('afterloginsup')
            else:
                message="Password is incorrect"
                return render(request,"app/login-register.html",{'msg':message})

def Profilecust(request,pk):
    print("UESER ID--------------------->",pk)
    if 'email' in request.session and 'password' in request.session :
        udata=User.objects.get(id=pk) 
        if udata.Role=='Customer':
            cust=Customer.objects.get(user_id=udata)
            return render (request,"app/profile.html",{'key1':cust})
    else :
        return  redirect ('loginregisterpage')
    
def ProfieUpdateCust(request,pk):
     if 'email' in request.session and 'password' in request.session :
        udata=User.objects.get(id=pk) 
        if udata.Role=='Customer':
            cust=Customer.objects.get(user_id=udata)
            cust.Firstname= request.POST['fname']
            cust.Lastname= request.POST['lname']
            cust.City= request.POST['city']
            cust.State= request.POST['state']
            cust.Address= request.POST['address']
            cust.DOB= request.POST['dob']
            cust.Gender= request.POST['gender']
            cust.profile_pic=request.FILES['profilepic']
            cust.save()
            url=f"/profilecust/{pk}"
            return redirect(url)

def Profilesup(request,pk):
    
    if 'email' in request.session and 'password' in request.session :
        udata=User.objects.get(id=pk) 
        if udata.Role=='Suplier':
            sup=Suplier.objects.get(user_id=udata)
            return render (request,"app/suplier/profile.html",{'key1':sup})
    else :
        return  redirect ('loginregisterpage')


def ProfieUpdateSup(request,pk):
     if 'email' in request.session and 'password' in request.session :
        udata=User.objects.get(id=pk) 
        if udata.Role=='Suplier':
            sup=Suplier.objects.get(user_id=udata)
            sup.Firstname= request.POST['fname']
            sup.Lastname= request.POST['lname']
            sup.City= request.POST['city']
            sup.State= request.POST['state']
            sup.Address= request.POST['address']
            sup.DOB= request.POST['dob']
            sup.Gender= request.POST['gender']
            sup.Shopname=request.POST['shopname']
            sup.GST_no=request.POST['gst_no']
            sup.save()
            url=f"/profilesup/{pk}"
            return redirect(url)


def Catergoryindex(request):
    all_data=Catergory.objects.all()
    sub_data=SubCategory.objects.all()
    return render(request,"app/suplier/categories.html",{'key1':all_data ,'key2':sub_data})


def CategoryShow(request):
    all_data=Catergory.objects.all()
    sub_data=SubCategory.objects.all()
    return render (request,"app/suplier/product.html",{'key1':all_data ,'key2':sub_data})


def editpage(request,pk):
    edata=Catergory.objects.get(pk=pk)
    return render(request,"app/suplier/categories.html",{'key3':edata})


def DeleteData(request,pk):
    cdata=Catergory.objects.get(pk=pk)
    cdata.delete()
    return HttpResponseRedirect(reverse('categoryindex'))

def Product(request):
    all_data=Catergory.objects.all()
    sub_data=SubCategory.objects.all().filter()
    return render (request,"app/suplier/product.html",{'key1':all_data ,'key2':sub_data})


def SuplierLogout(request):
    if 'email' in request.session and 'password' in request.session:
        del request.session['email']
        del request.session['password']
        return redirect('loginregisterpage')
    else:
        return redirect('loginregisterpage')

def CustomerLogout(request):
    if 'email' in request.session and 'password' in request.session:
        del request.session['email']
        del request.session['password']
        return redirect('loginregisterpage')
    else:
        return redirect('loginregisterpage')

def AddProductView(request,pk):

    if 'email' in request.session and 'password' in request.session:
        udata=User.objects.get(id=pk)
        if udata.Role=="Suplier":
            sup_id=Suplier.objects.get(user_id=udata)
            ct_id = request.POST['cat_name']
            cid = Catergory.objects.get(id=ct_id)
            st_id =request.POST['subcat'] 
            sid =SubCategory.objects.get(id=st_id)
            Bname = request.POST['bname']
            Bprice = request.POST['bprice']
            Bdescription = request.POST['bdescription']
            stock = request.POST['stock']
            Bimg = request.FILES['bimg']
        
            newproduct =AddProduct.objects.create(sup_id=sup_id,cat_id=cid,subcat_id=sid,Bname=Bname,Bprice=Bprice,Bdescription=Bdescription,stock=stock,Bimg=Bimg)
            newproduct.save()
            return render(request,"app/suplier/index.html")

def ShowProduct(request):
    all_pro = AddProduct.objects.all()
    return render(request,"app/shop-grid.html",{'key5':all_pro})

def ProductDetail(request,pk):
    prodata = AddProduct.objects.get(pk=pk)
    allpro = AddProduct.objects.all()
    return render(request,"app/product-details.html",{'key6':prodata,'key7':allpro})



        
        

def AddCart(request,pk):
    if 'email' in request.session and 'password' in request.session:
        
        uid = request.session['id']
        master = User.objects.get(id=uid)
        proid=AddProduct.objects.get(id=pk)
        cust = Customer.objects.get(user_id=master)
        
        if master.Role=="Customer":
            price = int(request.POST['Bprice'])
            qty = int(request.POST['qty'])
            Total = price * qty
            newpro = AddToCart.objects.create(cus_id=cust,addpro_id=proid,QTY=qty,Total=Total)
            newpro.save()
            key8 = AddToCart.objects.all().filter(cus_id=cust)
            Sub_total=0
            for t in key8:
                Sub_total += t.Total
            return render(request,'app/cart.html',{'key8': key8 ,'QTY':qty,'Total':Total,'Subtotal':Sub_total})


def Cartview(request):
    key8=AddToCart.objects.all()
    pro=AddProduct.objects.all()
    return render(request,'app/cart.html',{'key8':key8,'key9': pro})




def CartDelete(request,pk):
    cart=AddToCart.objects.get(pk=pk)
    cart.delete()
    return HttpResponseRedirect(reverse('cartview'))
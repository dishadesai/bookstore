from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.
class User(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    OTP=models.IntegerField()
    Role=models.CharField(max_length=50)
    is_created=models.DateTimeField(auto_now_add=True)
    is_updated=models.DateTimeField(auto_now_add=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

class Customer(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Contact=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    DOB=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to="img/")

class Suplier(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Contact=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    DOB=models.CharField(max_length=50)
    Shopname=models.CharField(max_length=50)
    GST_no=models.IntegerField(default=123)
    
    
class Delivery(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Contact=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    DOB=models.CharField(max_length=50)
    Experience=models.CharField(max_length=50)
    Qualfication=models.CharField(max_length=50)


class Catergory(models.Model):
    
    cat_name=models.CharField(max_length=50)
    

    def __str__(self) :
        return self.cat_name

    
    

class SubCategory(models.Model):
    cat_id=models.ForeignKey(Catergory,on_delete=models.CASCADE)
    Type=models.CharField(max_length=50)
    
    is_created=models.DateTimeField(auto_now_add=True)
    is_updated=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.Type

class AddProduct(models.Model):
    sup_id=models.ForeignKey(Suplier,on_delete=models.CASCADE,default="")
    cat_id=models.ForeignKey(Catergory,on_delete=models.CASCADE)
    subcat_id=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    Bname=models.CharField(max_length=50)
    Bprice=models.CharField(max_length=50)
    Bdescription=models.CharField(max_length=500)
    stock=models.CharField(max_length=50,default="available")
    Bimg=models.ImageField(upload_to="img/")
    is_created=models.DateTimeField(auto_now_add=True)
    is_updated=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.Bname


class AddToCart(models.Model):
    cus_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    addpro_id=models.ForeignKey(AddProduct,on_delete=models.CASCADE)
    QTY=models.IntegerField(default=0)
    Total=models.IntegerField(default=0)
    Subtotal=models.IntegerField(default=0)
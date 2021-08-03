from app.models import Catergory
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.Indexpage,name="index"),
    path("loginregisterpage/",views.LoginRegisterPage,name="loginregisterpage"),
    path("regcustomer/",views.RegCustomer,name='register'),
    path("otpverify/",views.OTPverify,name='otpverify'),
    path("logincust/",views.LoginUser,name='logincust'),
    path("afterlogincust/",views.Afterlogincust,name="afterlogincust"),
    path("profilecust/<int:pk>",views.Profilecust,name='profilecust'),
    path("profileupdatecust/<int:pk>",views.ProfieUpdateCust,name='profileupdatecust'),
    path("loginsup/",views.Afterloginsup,name='afterloginsup'),
    path("profilesup/<int:pk>",views.Profilesup,name='profilesup'),
    path("profileupdatesup/<int:pk>",views.ProfieUpdateSup,name='profileupdatesup'),
    path("categoryindex/",views.Catergoryindex,name='categoryindex'),
    path("editpage/<int:pk>",views.editpage,name='editpage'),
    path("delete/<int:pk>",views.DeleteData,name='delete'),
    path("product/",views.Product,name='product'),
    path("suplierlogout/",views.SuplierLogout,name="suplierlogout"),
    path("cutomerlogout/",views.CustomerLogout,name="customerlogout"),
    path("addproduct/<int:pk>",views.AddProductView,name='addproduct'),
    path("showproduct/",views.ShowProduct,name='showproduct'),
    path("productdetail/<int:pk>",views.ProductDetail,name='productdetail'),
    path("addcart/<int:pk>",views.AddCart,name='addcart'),
    path("cartview/",views.Cartview,name='cartview'),
    path("cartdelete/<int:pk>",views.CartDelete,name='cartdelete'),
    
    
    
]

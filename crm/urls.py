from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'crm'
urlpatterns = [
 path('', views.home, name='home'),
 path('home', views.home, name='home'),
 path('shop', views.shop, name='shop'),
 path('cart', views.cart, name='cart'),
 path('pricing', views.pricing, name='pricing'),
 path('signin', views.signin, name='signin'),
path('signup', views.signup, name='signup'),
]


from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('shop', views.product_list, name='product_list'),
    path('pricefilter/', views.product_filter, name='product_filter'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]

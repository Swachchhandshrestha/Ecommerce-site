from django.urls import path
from .views import(
    HomeView,
    register,
    remove_from_cart,
    add_to_cart,
    OrderSummery,
    remove_single_item,
    ItemDetailView,
    checkout,
    ProductView



)

app_name= 'Shopin'

urlpatterns =[
    path('',HomeView.as_view(),name ='home'),
    path('signup/', register , name ='signup'),
    path('product/<slug>', ItemDetailView.as_view() , name ='product'),
    path('mobile/', ProductView.as_view() , name ='mobile'),
    path('remove-single-item/<slug>',remove_single_item,name='remove-single-item'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('orders/',OrderSummery.as_view(), name='orders'),
    path('checkout/',checkout,name='checkout')


]
from django.urls import path,re_path
from . import views
from ecommerce import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('store', views.store, name ="store"),
    path('fake_store', views.fake_store, name ="fake_store"),

    path('cart/', views.cart, name = "cart"),
    path('fake_cart/', views.fake_cart, name = "fake_cart"),

    path('checkout/',views.checkout, name= "checkout"),
    path('fake_checkout/',views.fake_checkout, name= "fake_checkout"),


    path('search',views.search_list, name= "search"),
    path('fake_search',views.fake_search_list, name= "fake_search"),
    
    re_path(r'update_item/', views.updateItem, name = "update_item"),
]
urlpatterns += staticfiles_urlpatterns()
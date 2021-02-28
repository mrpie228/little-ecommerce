from django.urls import path,re_path
from . import views
from ecommerce import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.store, name ="store"),


    re_path(r'^cart/$', views.cart, name = "cart"),
    path('fake_cart/', views.fake_cart, name = "fake_cart"),

    re_path(r'^checkout/$',views.checkout, name= "checkout"),


    re_path(r'^search/$',views.search_list, name= "search"),

    
    re_path(r'update_item/', views.updateItem, name = "update_item"),
]
urlpatterns += staticfiles_urlpatterns()
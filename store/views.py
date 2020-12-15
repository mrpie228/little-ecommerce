from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import simplejson as json
from django.views.generic.list import ListView
# Create your views here.
def store(request):
    products= Product.objects.all()
    context={'products':products}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated :
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context={'items':items,'order':order}
    return render(request, 'store/cart.html', context)


def fake_cart(request):
    if request.user.is_authenticated :
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context={'items':items,'order':order}
    return render(request, 'store/fake_cart.html', context)


def checkout(request):
    if request.user.is_authenticated :
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context={'items':items,'order':order}

    return render(request, 'store/checkout.html', context)



def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer= request.user.customer
    product= Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product= product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()
    
    return JsonResponse(data, safe=False)


#class Search(ListView):
 #   paginate_by=3
  #  def get_queryset(self):
   #     search_products = Product.objects.filter(name=self.request.GET.get("q"))
    #    return search_products
#
 #   def get_context_data(self, *args, **kwargs):
  #      context = super().get_context_data(*args, **kwargs)
   #     context["q"] = self.request.GET.get("q")
    #    return context

def search_list(request):
    search_query = request.GET.get('search','')
    if search_query:
        search_products = Product.objects.filter(name__icontains=search_query)
    else :
        search_products= Product.objects.all()

    context = {'search_query': search_query, 'search_products': search_products}
    return render(request, 'store/search.html', context)

def fake_search_list(request):
    search_query = request.GET.get('search','')
    if search_query:
        search_products = Product.objects.filter(name__icontains=search_query)
    else :
        search_products= Product.objects.all()

    context = {'search_query': search_query, 'search_products': search_products}
    return render(request, 'store/fake_search.html', context)
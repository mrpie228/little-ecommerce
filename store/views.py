from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import simplejson as json
from django.views.generic.list import ListView
from .utils import cookieCart, cartData, guestOrder



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
        try:
            cart= json.loads(request.COOKIES['cart'])
        except:
            cart={}

        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems= order['get_cart_items']
        for i in cart:
            cartItems+=cart[i]['quantity']
            product= Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            order['get_cart_total']+=total
            order['get_cart_items']+=cart[i]['quantity']

            item={
                'product':{
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "image":product.image,
                    },
                'quantity':cart[i]['quantity'],
                'get_total':total,
                }
            items.append(item)

    context={'items':items,'order':order}
    return render(request, 'store/cart.html', context)


def fake_cart(request):
    if request.user.is_authenticated :
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else:
        try:
            cart= json.loads(request.COOKIES['cart'])
        except:
            cart={}

        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems= order['get_cart_items']
        for i in cart:
            cartItems+=cart[i]['quantity']
            product= Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            order['get_cart_total']+=total
            order['get_cart_items']+=cart[i]['quantity']

            item={
                'product':{
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "image":product.image,
                    },
                'quantity':cart[i]['quantity'],
                'get_total':total,
                }
            items.append(item)

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

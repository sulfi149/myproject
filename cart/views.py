from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product,Variations
from .models import Cart,CartItem
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def _Cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):

    product = Product.objects.get(id=product_id)
    product_variation = []
    if request.method == 'POST':
        print(request.POST)
        for item in request.POST:
            key = item
            value = request.POST[key]
            
            try:      
                variation = Variations.objects.get(product_name=product,variation_category__iexact=key,variation_val__iexact=value)
                print(variation)        
                product_variation.append(variation)
            except:
                pass
                     
            
    try:
        cart  = Cart.objects.get(cart_id = _Cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _Cart_id(request)
        )
    cart.save()
    # group the cart item for that we need to check whether the cart item is exist or not 

    is_cart_item_exists = CartItem.objects.filter(product=product,cart=cart).exists()

    if is_cart_item_exists:
        cart_item = CartItem.objects.filter(product=product,cart=cart)
        # existing variation and product variation aswell itemid
        ex_var_list = []
        id = []
        for item in cart_item:
            existing_variation = item.variations.all()
            ex_var_list.append(list(existing_variation)) 
            id.append(item.id)
        print(ex_var_list)
        if product_variation in ex_var_list:
            # increase the cart item quantity
            indx = ex_var_list.index(product_variation)
            item_id = id[indx]
            item = CartItem.objects.get(product=product,id=item_id)
            item.quantity += 1
            item.save()
        else:
            # create a new cart item
            item= CartItem.objects.create(product=product,quantity=1,cart=cart)
            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(*product_variation)
            item.save()   
    
    else: 
        cart_item = CartItem.objects.create(
            product  = product,
            quantity = 1,
            cart = cart,
        )
        if len(product_variation) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)
        cart_item.save()

    return redirect('cart')




def remove_cart(request,product_id,cart_item_id):

    cart = Cart.objects.get(cart_id=_Cart_id(request))
    product = get_object_or_404(Product,id = product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart,id=cart_item_id)
    try:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass        
    return redirect('cart')        
def remove_cart_item(request,product_id,cart_item_id):
    cart = Cart.objects.get(cart_id=_Cart_id(request))
    product = get_object_or_404(Product,id = product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart,id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

    
def cart(request,Total=0,quantity=0,cart_items=0):
    tax = 0 
    grand_total=0
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user,is_active=True)
        else:
            cart = Cart.objects.get(cart_id = _Cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart,is_active=True)

        for cart_item in cart_items:
            Total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (3*Total) /100
        grand_total = Total + tax   
    except ObjectDoesNotExist:

    
        pass
    
    context = {
        'Total': Total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'      : tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html',context)

@login_required(login_url="login")
def checkout(request,Total=0,quantity=0,cart_items=0):
    tax = 0 
    grand_total=0
    try:
        cart = Cart.objects.get(cart_id = _Cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)

        for cart_item in cart_items:
            
            Total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (3*Total) /100
        grand_total = Total + tax   
    except ObjectDoesNotExist:

    
        pass
    
    context = {
        'Total': Total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'      : tax,
        'grand_total': grand_total,
    }

    return render(request,'store/checkout.html',context)
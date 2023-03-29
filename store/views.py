from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import category

from cart.views import _Cart_id
from cart.models import CartItem

from django.http import HttpResponse

from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
def home_view(request):
    products = Product.objects.all().filter(is_available=True)
    

    context = {
        'products' : products,
    }
    
    return render(request, "store/index.html", context)

def store(request,category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(category,slug=category_slug)
        products = Product.objects.filter(category = categories , is_available=True)
        paginator = Paginator(products,1)
        page = request.GET.get('page')
        paged_product  = paginator.get_page(page) 
        product_count=products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products,4)
        page = request.GET.get('page')
        paged_product  = paginator.get_page(page) 
        product_count=products.count()
      

    context = {
        'products' : paged_product,
        'product_count': product_count

        

     }
    
    return render(request,'store/store.html',context)
def product_detaile(request,category_slug,product_slug):
    try:
        single_product= Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart =CartItem.objects.filter(cart__cart_id=_Cart_id(request),product=single_product).exists()
    except Exception as e: 
        raise e   


    context = {
        'single_product' : single_product,
        'in_cart':in_cart
    }     
    return render(request,'store/product_detaile.html',context)
def search(request):
    return render(HttpResponse('search'))
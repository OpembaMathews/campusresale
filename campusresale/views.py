from django.shortcuts import render,get_object_or_404
from .models import Category, Product

# Create your views here
def index(request):
    return render (request , 'campusresale/index.html')
def about(request):
    # pass
    return render (request , 'campusresale/about.html')

def services(request):
    # pass
    return render (request , 'campusresale/services.html')

def login(request):
    # pass
    return render (request , 'campusresale/login.html')

def product_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter( available = True )
    if category_slug:
        category = get_object_or_404( Category, slug = category_slug )
        products = products.filter(category = category )

    return render (request, 'campusresale/product_list.html',{'category': category,
                            'products': products, 'categories': categories})


def product_detail(request, id, slug ):
    product = get_object_or_404( Product, id=id,
                                slug=slug, available = True )
    cart_product_form = CartAddProductForm()

    return render (request , 'campusresale/product_detail.html', {'product': product,
     'cart_product_form': cart_product_form})

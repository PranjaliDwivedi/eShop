from django.shortcuts import render
from django.views import View
from .forms import RegistrationForms
from django.contrib import messages
from django.contrib.auth.models import User
from .models import(
    Customer,
    Product,
    Cart,
    OrderPlaced,
)



class ProductView(View):
    def get(self, request):
        camera = Product.objects.filter(category='C')
        men = Product.objects.filter(category='M')
        women = Product.objects.filter(category='W')
        sunglasses = Product.objects.filter(category='S')
        shoes = Product.objects.filter(category='Sh')
        context = {
            'camera': camera,
            'shoes': shoes,
            'sunglasses': sunglasses,
            'men':men,
            'women':women,
        }

        return render(request, 'index.html', context)
    
class ProductDetails(View):
    def get(self, request, id):
        product = Product.objects.get(pk=id)
        return render(request, 'productDetails.html', {'product': product})
    
def shoes(request, data=None):
    if data == None:
        products = Product.objects.filter(category='Sh').filter(brand = 'Campus')
    elif data =='Nike':
        products = Product.objects.filter(category='Sh').filter(brand = 'Nike')


    elif data == 'below':
        products = Product.objects.filter(category='Sh').filter(discounted_price__lt = 50)

    elif data == 'above':
        products = Product.objects.filter(category='Sh').filter(discounted_price__gt = 49)

    return render(request, 'shoes.html', {'products': products})


def search(request):
    q = request.GET.get('query')
    data = Product.objects.filter(product_name__icontains = q)
    return render(request, 'search.html', {'data' :data, 'q': q})


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForms()
        return render(request, 'registration.html', {'form': form})


    def post(self, request):
        form = RegistrationForms(request.POST)
        if form.is_valid():
            messages.success(request, 'congratulation! Registered Successfully')
            form.save()
        return render(request, 'registration.html', {'form': form})
    
def profile(request):
    return render(request, 'profile.html')
    
def addToCart(request):
    user = request.user
    product_id = request.GET.get('pro_id')
    product = Product.objects.get(pk = product_id)
    print(request.user)

    for user in User.objects.all():
        Customer.objects.get_or_create(user=user)
    Customer = Customer.objects.get(user=user)
    Cart(user=Customer, product=product).save()
    return render(request, 'carts.html')


def carts(request):
    user = request.user
    customer = Customer.objects.get(user = user)
    cart = Cart.objects.filter(user= customer)

    total_price = 0
    for i in cart:
        total_price = i.product.discounted_price * i.quantity

    return render(request, 'carts.html', {'carts': cart, 'total':total_price})

def buynow(request):
    return render(request, 'buynow.html')

def registration(request):
    return render(request, 'registration.html')

def home(request):
    return render(request, 'index.html')

def men(request,data):
    men = Product.objects.filter(category = 'M')
    return render(request, 'men.html',{"men": men})

def women(request,data):
    women = Product.objects.filter(category = 'W')
    return render(request, 'women.html',{"women": women})

def shoes(request,data):
    shoes = Product.objects.filter(category = "Sh")
    return render(request, 'shoes.html',{"shoes": shoes})

def sunglasses(request,data):
    sunglasses = Product.objects.filter(category = 'S')
    return render(request, 'sunglasse.html',{"sunglasse": sunglasses})

def contact(request):
    return render(request, 'contact.html')

def products(request):
    return render(request, 'products.html')

def details(request):
    return render(request, 'details.html')

def buynow(request):
    return render(request, 'buynow.html')

def checkout(request):
    return render(request, 'checkout.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def change(request):
    return render(request, 'change.html')
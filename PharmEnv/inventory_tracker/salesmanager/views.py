from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
#here we include models so that views can use them
from .models import Product, Sale
#same for filters
from .filters import Product_filter
# Create your views here.
#including our model forms created in the forms file
from .forms import AddForm, SaleForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    products = Product.objects.all().order_by('-id')
    product_filters = Product_filter(request.GET, queryset = products)
    products = product_filters.qs
    return render(request, 'products/index.html', {'products' : products, 'product_filters' : product_filters})

@login_required
def home(request):
    return render(request, 'products/aboutdr.wuhayu.html')
#create a view for product_detail

@login_required
def product_details(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'products/product_detail.html',{'product': product})

@login_required
def issue_item(request, pk):
    issued_item = Product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)
    
    #checks if the required input is as its supposed to be
    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale = sales_form.save(commit = False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            #to keep track of the remaining stock after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()
            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)
            messages.success(request, 'Iten issued successfully.')
            return redirect('receipt') 
    return render(request, 'products/issue_item.html', {'sales_form':sales_form})


#this handles receipts issueing
@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request, 'products/receipt.html', {'sales': sales})
    

@login_required
def add_to_stock(request, pk):
    issued_item = Product.objects.get(id = pk)
    form = AddForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()

            #To add to the remaining stock quantity is reducing
            print(added_quantity)
            print (issued_item.total_quantity)
            messages.success(request, 'Successfully added to stock.')
            return redirect('index')

    return render (request, 'products/add_to_stock.html', {'form': form})
@login_required
def all_sales(request):
    sales = Sale.objects.all()
    total = sum([items.amount_recieved for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change

    return render(request, 'products/all_sales.html', {
        'sales': sales,
        'total': total,
        'change': change,
        'net': net,
    }
    )


def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request, 'products/receipt_detail.html', {'receipt': receipt})

@login_required
def delete_detail(request, product_id):
    delete = Product.objects.get(id = product_id)
    delete.delete()
    messages.success(request, 'The Product has been deleted successfully.')
    return HttpResponseRedirect(reverse('index'))

#appointment view
@login_required
def appointment(request):
    if request.method == 'POST':
        
        #use square brackets otherwise you'll encounter the 'query-list not callble' error
        your_name = request.POST['name']
        your_phone = request.POST['phone']
        your_email = request.POST['email']
        your_address = request.POST['address']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']
    #send an email.
        '''
        send_mail(
            your_name, #subject
            your_message, # message
            your_email,#from email
            ['brucemalloy36@gmail.com'], #To email
        )
        messages.success(request, 'your info has been submitted successfully')
        '''
        messages.success(request, "An email has been sent to the receptionist.\n We'll get back to you shortly, thank you for your patience")
        return render(request, 'products/appointment.html', 
                {'your_name':your_name,
                'your_phone':your_phone,
                'your_email':your_email,
                'your_address':your_address,
                'your_time':your_time,
                'your_message':your_message})
    else:
        return render(request, 'products/about.html')

def appointment_page(request):
    return render(request, 'products/appointment.html')








#adding a cart view

'''
def add_to_cart(request, product_id):
    #get the product that the user is adding to cart
    product = get_object_or_404(Product, id=product_id)
    #check if the user already has cart, if not create one
    if 'cart_id' in request.session:
        cart = Cart.objects.get(id=request.session['cart_id'])
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    #check if  the product keyis alreadycreated, if not add it
    cart_item, created = CartItem.objects.get_or_create(
        cart = cart,
        product=product,
    )
    #if the cart item was already created, increase its quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        #redirect the user back to the product page
        return redirect('product_detail', product_id=product.id)
    '''
@login_required
def add_to_cart(request, pk):
    issued_item = CartItem.objects.get(id = pk)
    form = AddForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()

            #To add to the remaining stock quantity is reducing
            print(added_quantity)
            print (issued_item.total_quantity)
            return redirect('index')

    return render (request, 'products/add_to_cart.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'products/custom_login.html'
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    # filter_type = request.GET.get("filter", "all")

    # if filter_type == "all":
    #     product_list = Product.objects.all()
    # else:
    #     product_list = Product.objects.filter(user=request.user)

    context = {
        "namaToko" : "Football Shop",
        "nama" : "Vanessa",
        "kelas" : "PBP B",
        # "product_list": product_list,
        "last_login" : request.COOKIES.get('last_login', 'Never')
        }

    return render(request, "main.html", context)

# def register(request):
#     form = UserCreationForm()

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your account has been successfully created!')
#             return redirect('main:login')
#     context = {'form':form}
#     return render(request, 'register.html', context)

@csrf_exempt
@require_POST
def register_user_ajax(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'message':  'Registration successful!'}, status=201)
    else:
        error_dict = {field: [str(error) for error in errors] for field, errors in form.errors.items()}
        return JsonResponse({'message': 'Registration failed', 'errors': error_dict}, status=400)

def render_register_page(request):
    if request.user.is_authenticated:
        return redirect('main:show_main')
    
    context = {'form': UserCreationForm()}
    return render(request, 'register.html', context)

# def login_user(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)

#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)

#             response = HttpResponseRedirect(reverse("main:show_main"))
#             response.set_cookie('last_login', str(datetime.datetime.now()))
#             return response
        
#             # return redirect('main:show_main')
#     else:
#         form = AuthenticationForm(request)
#     context = {'form':form}
#     return render(request, 'login.html', context)

@csrf_exempt
@require_POST
def login_user_ajax(request):
    form = AuthenticationForm(data=request.POST)

    if form.is_valid():
        user = form.get_user()
        login(request, user)

        response = JsonResponse({'message': 'Login successful!'})
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    else:
        error_message = form.errors.as_text().split('\n')[-1].strip() if form.errors else 'Username atau password salah!'
        return JsonResponse({'message': error_message}, status=400)

def render_login_page(request):
    if request.user.is_authenticated:
        return redirect('main:show_main')

    context = {'form': AuthenticationForm()}
    return render(request, 'login.html', context)

# def logout_user(request):
#     logout(request)

#     response = HttpResponseRedirect(reverse('main:login'))
#     response.delete_cookie('last_login')
#     return response

#     # return redirect('main:login')

@csrf_exempt
@require_POST
def logout_user_ajax(request):
    logout(request)
    response = JsonResponse({'message': 'Logged out successfully'})
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product':product
    }
    return render(request, "product_detail.html", context)

def show_xml(request):
    products_list = Product.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    # Buat objek baru 
    new_product = Product(
        name=name, 
        price=price, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    product.name = request.POST.get("name")
    product.price = request.POST.get("price")
    product.description = request.POST.get("description")
    product.category = request.POST.get("category")
    product.thumbnail = request.POST.get("thumbnail")
    product.is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    product.save()

    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_POST
def delete_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()

    return JsonResponse({'message': 'Product deleted successfully.'}, status=200)

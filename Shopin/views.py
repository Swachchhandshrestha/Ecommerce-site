from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View,DetailView,TemplateView
from .models import Item,Order,OrderItem, Mobile,  Brand, Ad
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# Create your views here.


class BaseView(View):
    template_context={
        'items' : Item.objects.all(),
        'mobiles': Mobile.objects.all()

    }

#making of with context variable


class HomeView(BaseView):
    def get(self,request):
        self.template_context['items']=Item.objects.all()
        self.template_context['brands']=Brand.objects.all()
        self.template_context['ads']=Ad.objects.all()
        self.template_context['sale_items'] = Item.objects.filter(labels = 'sale')
        self.template_context['hot_items'] = Item.objects.filter(labels = 'hot')
        return render(request,'shop-index.html',self.template_context)


class ItemDetailView(DetailView):
    model = Item
    template_name = "shop-item.html"


class ProductView(BaseView):
    def get(self, request):
        self.template_context['mobiles']=Mobile.objects.all()
        return render(request,'shop-product-list.html',self.template_context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.error(request,"This username is already taken.")
                return redirect('home:signup')

            elif User.objects.filter(email = email).exists():
                messages.error(request, "This email is already taken.")
                return redirect('home:signup')

            else:
                user = User.objects.create_user(
                 username = username,
                 first_name = first_name,
                 last_name = last_name,
                 email = email,
                 password = password
               )
            user.save()
            messages.info(request,"sucessfully registered.")
            return redirect('/accounts/login')

        else:
            messages.error(request, "password does not match")
            return redirect('home:signup')

    else:
        return render(request,'signup.html')


class SearchView(BaseView):
    def get(self, request):
        query = request.GET.get('query', 'none')
        if not query:
            return redirect('/')

        self.template_context['search_result'] = Item.objects.filter(
            title__icontains= query
        )
        self.template_context['search_name'] = query
        return render(request,'shop-search-result.html',self.template_context)

# add to cart
@login_required
def add_to_cart(request,slug):
    item = get_object_or_404(Item,slug = slug)
    order_item = OrderItem.objects.get_or_create(
        item = item,
        user = request.user,
        ordered = False
    )[0]
    orders = Order.objects.filter(
        user = request.user,
        ordered = False
    )
    if orders.exists():
        order = orders[0]
        if order.items.filter(item__slug = item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.success(request,'Quantity Updated')
            return redirect("Shopin:orders")
        else:
            order.items.add(order_item)
            messages.info(request,'The item is added')
            return redirect("Shopin:orders")
    else:
        order_date = timezone.now()
        order = Order.objects.create(
            user = request.user,
            order_date = order_date
        )
        order.items.add(order_item)
        messages.success(request,'The new iem is added in your cart')
        return redirect("Shopin:orders")


class OrderSummery(BaseView):
    def get(self,*arg,**kwargs):
        try:
            order=Order.objects.get(user = self.request.user,ordered = False)
            self.template_context['object'] = order
            return render(self.request,'shop-shopping-cart.html',self.template_context)

        except ObjectDoesNotExist:
            messages.info("Your cart is empty")
            return render("/")


def remove_from_cart(request,slug):
    item = get_object_or_404(Item,slug = slug)
    orders = Order.objects.filter(
        user = request.user,
        ordered = False
    )
    if orders.exists():
        order = orders[0]
        if order.items.filter(item__slug = item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )
            order_item.delete()
            messages.info(request,"The item is removed from your cart")
            return redirect("Shopin:orders")
    else:
        messages.info(request,"This item does not exists")
        return redirect("Shopin:orders")


def remove_single_item(request,slug):
    item = get_object_or_404(Item,slug = slug)
    orders = Order.objects.filter(
        user = request.user,
        ordered = False

    )
    if orders.exists():
        order = orders[0]
        if(order.items.filter(item__slug= item.slug)).exists():
            order_item = OrderItem.objects.filter(
                item = item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
    else:
        messages.info(request, "This item is not in your cart")
        return redirect("Shopin:orders")

    return redirect("Shopin:orders")


def checkout(request):
    return render(request,'shop-checkout.html')













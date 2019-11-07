from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.
LABELS =(('sale','sale'),
         ('new','new'),
         ('hot','hot'),
         ('','default'))
STATUS=(('active','active'),
        ('','default'))
ACTIVE=(('In Stock','In Stock'),('out of Stock','Out of Stock'))


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    discounted_price = models.IntegerField(blank=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images',blank=True)
    slug = models.TextField(max_length=300)
    labels = models.CharField(choices=LABELS, max_length=10, blank=True)
    status = models.CharField(choices=STATUS, max_length=20, blank=True)
    add_date = models.DateTimeField(blank=True, null=True)
    stock = models.CharField(choices=ACTIVE, max_length=50, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home:product",kwargs={'slug':self.slug})

    def get_add_to_cart(self):
        return reverse("home:add-to-cart", kwargs= {'slug': self.slug})


class Mobile(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    discounted_price = models.IntegerField(blank=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='mobiles',blank=True)
    slug = models.TextField(max_length=300)
    labels = models.CharField(choices=LABELS, max_length=10, blank=True)
    status = models.CharField(choices=STATUS, max_length=20, blank=True)
    add_date = models.DateTimeField(blank=True, null=True)
    stock = models.CharField(choices=ACTIVE, max_length=50, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home:product",kwargs={'slug':self.slug})

    def get_add_to_cart(self):
        return reverse("home:add-to-cart", kwargs= {'slug': self.slug})


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brands',blank=True)
    description = models.TextField()
    add_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)
    description = models.TextField()
    rank = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS,max_length=10,blank=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)
    description = models.TextField()
    rank = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=10, blank=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item,on_delete=True) #individual item deleted
    quantity = models.IntegerField(default= 1)
    order_date = models.DateTimeField(blank = True, null=True)

    def __str__(self):
        return self.item.title

    def get_unit_total_price(self):
        return self.quantity.self.item.price

    def get_total_discounted_price(self):
        return self.quantity*self.item.discounted_price

    def get_total_price(self):
        if self.item.discounted_price:
            return self.get_total_discounted_price()
        else:
            return self.get_unit_total_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    order_date = models.DateTimeField(blank= True)
    ordered = models.BooleanField(default= False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total_price = 0
        for orders in self.items.all():
            total_price +=orders.get_total_price()
        return total_price

    def get_total_final_price(self):
        return self.get_total()+ 50











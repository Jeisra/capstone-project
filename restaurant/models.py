from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Booking(models.Model):

    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateTimeField(default=now)
    

    def __str__(self): 
        return f"Booking - {self.name}"

# class Menu(models.Model):

#     title = models.CharField(max_length=255, default="Default Title")
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     inventory = models.IntegerField(default=0)
#     menu_item_description = models.TextField(max_length=1000, default='')

#     def __str__(self): 
#         return f"{self.title} - ${self.price:.2f}"
    
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True, default=1)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    inventory = models.IntegerField(default=0)
    menu_item_description = models.TextField(max_length=1000, default='')
    
    def __str__(self):
        return self.title
    
    def get_item(self):
        return f"{self.title} : {self.price}"
    
    def __str__(self): 
        return f"{self.title} - ${self.price:.2f}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = ('menuitem', 'user')
        
    def __str__(self):
        return f"Cart of {self.user.username} - {self.quantity} x {self.menuitem.title} (${self.price})"
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True)  
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)
    
    def __str__(self):
        return f"Order #{self.id} by {self.user.username} - Total: ${self.total} - Status: {'Completed' if self.status else 'Pending'}"

class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = ('order', 'menuitem')
        
    def __str__(self):
        return f"{self.menuitem.title} (Order: {self.order.id})"
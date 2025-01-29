from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, MenuItem, Category, Cart, Order, OrderItem

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ManagerListSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['id','username','email']

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    
    class Meta:
        # model = MenuItem
        # fields = ['id','title','price', 'inventory', 'featured','category'] 
        model = MenuItem
        fields = ['id', 'title','price', 'featured', 'category', 'inventory', 'menu_item_description'] 
    
    def validate_category(self, value):
        if not value:
            raise serializers.ValidationError("The category field is required.")
        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ['slug']

class CartHelpSerializer(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = ['id','title','price']

class CartSerializer(serializers.ModelSerializer):
    menuitem = CartHelpSerializer()
    class Meta():
        model = Cart
        fields = ['menuitem','quantity','price']
        
class CartAddSerializer(serializers.ModelSerializer):
    class Meta():
        model = Cart
        fields = ['menuitem','quantity']
        extra_kwargs = {
            'quantity': {'min_value': 1},
        }
class CartRemoveSerializer(serializers.ModelSerializer):
    class Meta():
        model = Cart
        fields = ['menuitem']

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta():
        model = Order
        fields = ['id','user','total','status','delivery_crew','date']

class SingleHelperSerializer(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = ['title','price']
        
class SingleOrderSerializer(serializers.ModelSerializer):
    menuitem = SingleHelperSerializer()
    class Meta():
        model = OrderItem
        fields = ['menuitem','quantity']


class OrderInsertSerializer(serializers.ModelSerializer):
    class Meta():
        model = Order
        fields = ['delivery_crew']
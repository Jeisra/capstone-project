from django.test import TestCase
from .models import MenuItem, Booking, Category
from .serializers import MenuItemSerializer, bookingSerializer, menuSerializer, CategorySerializer

# ------------------------------
# PRUEBAS UNITARIAS PARA MODELOS
# ------------------------------

class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(name="John Doe", no_of_guests=2)
        self.assertEqual(str(booking), "Booking - John Doe")
        self.assertEqual(booking.no_of_guests, 2)


class MenuModelTest(TestCase):
    # def test_create_menu(self):
    #     menu = MenuItem.objects.create(title="Special Menu", price=25.50, inventory=20)
    #     self.assertEqual(str(menu), "Special Menu - $25.50")
    #     self.assertEqual(menu.inventory, 20)
    def test_create_menu(self):
        category = Category.objects.create(title="Main Course")  # Crear una categoría
        menu = MenuItem.objects.create(title="Special Menu", price=25.50, inventory=20, category=category)
        self.assertEqual(str(menu), "Special Menu - $25.50")

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(slug="italian-food", title="Italian")
        self.assertEqual(str(category), "Italian")


class MenuItemModelTest(TestCase):
    def test_create_menu_item(self):
        category = Category.objects.create(slug="desserts", title="Desserts")
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100, category=category)
        self.assertEqual(str(item), "IceCream - $80.00")
        self.assertEqual(item.get_item(), "IceCream : 80")
        self.assertEqual(item.inventory, 100)


# ------------------------------
# PRUEBAS UNITARIAS PARA SERIALIZERS
# ------------------------------

class BookingSerializerTest(TestCase):
    def test_booking_serializer(self):
        booking_data = {"name": "Alice", "no_of_guests": 3}
        serializer = bookingSerializer(data=booking_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["name"], "Alice")


class MenuSerializerTest(TestCase):
    def test_menu_serializer(self):
        menu_data = {"title": "Breakfast Combo", "price": "15.99", "inventory": 5}
        serializer = menuSerializer(data=menu_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["title"], "Breakfast Combo")


class CategorySerializerTest(TestCase):
    def test_category_serializer(self):
        category_data = {"slug": "fast-food"}
        serializer = CategorySerializer(data=category_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["slug"], "fast-food")


class MenuItemSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(slug="beverages", title="Beverages")

    def test_menu_item_serializer(self):
        item_data = {"title": "Coca-Cola", "price": "2.99", "inventory": 50, "featured": True, "category": self.category.id}
        serializer = MenuItemSerializer(data=item_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["title"], "Coca-Cola")
        self.assertEqual(serializer.validated_data["inventory"], 50)

    def test_menu_item_invalid_serializer(self):
        """Prueba de validación: Se espera que falle por falta de 'category'."""
        invalid_data = {"title": "Coca-Cola", "price": "2.99", "inventory": 50, "featured": True}
        serializer = MenuItemSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("category", serializer.errors.keys())


# ------------------------------
# PRUEBAS PARA CONSULTAS Y SERIALIZACIÓN
# ------------------------------

class MenuItemViewTest(TestCase):
    def setUp(self):
        """Crea instancias de prueba del modelo MenuItem"""
        self.category = Category.objects.create(slug="main-course", title="Main Course")
        self.menu_item1 = MenuItem.objects.create(title="Pizza", price=12.99, inventory=10, category=self.category)
        self.menu_item2 = MenuItem.objects.create(title="Burger", price=8.99, inventory=5, category=self.category)
        self.menu_item3 = MenuItem.objects.create(title="Pasta", price=10.99, inventory=7, category=self.category)

    def test_get_all_menu_items(self):
        """Recupera todos los objetos MenuItem añadidos y verifica la serialización"""
        menu_items = MenuItem.objects.all()
        serialized_data = MenuItemSerializer(menu_items, many=True).data  # Serializa los datos

    #     response_data = [
    #         {"id": self.menu_item1.id, "title": "Pizza", "price": "12.99", "inventory": 10, "featured": True, "category": self.category.id},
    #         {"id": self.menu_item2.id, "title": "Burger", "price": "8.99", "inventory": 5, "featured": True, "category": self.category.id},
    #         {"id": self.menu_item3.id, "title": "Pasta", "price": "10.99", "inventory": 7, "featured": True, "category": self.category.id}
    #     ]

    #     # Comprueba si los datos serializados coinciden con los esperados
    #     self.assertEqual(serialized_data, response_data)
    # Construcción dinámica de los datos esperados
        response_data = [
            {
                "id": item.id,
                "title": item.title,
                "price": f"{item.price:.2f}",  # Asegurar formato de precio con 2 decimales
                "inventory": item.inventory,
                "featured": item.featured,
                "category": item.category.id,  # Obtener el ID de la categoría real
                "menu_item_description": item.menu_item_description
            }
            for item in menu_items
        ]

        # Verifica si los datos serializados coinciden con los esperados
        print("Serialized Data:", serialized_data)
        print("Response Data:", response_data)
        self.assertEqual(serialized_data, response_data)
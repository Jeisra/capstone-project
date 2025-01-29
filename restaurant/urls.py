from django.urls import path
from . import views
from .views import MenuItemsView, SingleMenuItemView, securedview
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name='menu'),
    #path('home/', views.index, name='home'),
    #path('menu-items/<int:pk>/', views.MenuItemsView.as_view(), name='menu-items'),
    #path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/category', views.CategoriesView.as_view()),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('menu/<int:pk>/', views.display_menu_item, name='menu_item'),
    path('api-token-auth/', obtain_auth_token),
    path('message/', views.securedview),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('groups/managers/users', views.ManagersView.as_view()),
    path('groups/managers/users/<int:pk>', views.ManagersRemoveView.as_view()),
    path('groups/delivery-crew/users', views.DeliveryCrewView.as_view()),
    path('groups/delivery-crew/users/<int:pk>', views.DeliveryCrewRemoveView.as_view()),
    path('cart/menu-items', views.CartView.as_view()),
    path('order', views.OrderView.as_view()),
    path('orders/<int:pk>', views.SingleOrderView.as_view()),
]

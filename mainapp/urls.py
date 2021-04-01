from django.urls import path, include
from .views import (
    BaseView,
    ProductDetailView,
    GameCategoryDetailView,
    CartView,
    AddToCartView,
    DeleteCartView,
    ChangeQTYView,
    CheckOutView,
    MakeOrderView
)

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', GameCategoryDetailView.as_view(), name='game_category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('make_order/', MakeOrderView.as_view(), name='make_order')
]

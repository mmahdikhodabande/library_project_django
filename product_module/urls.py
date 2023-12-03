from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListview.as_view(), name='product_list'),
    path('category/<cat>', views.ProductListview.as_view(), name='product_categories_list'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('books/<int:category_id>/', views.categories_list, name='categories_list'),
]

from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, ProductCategory
from site_setting.models import SiteBanner


# Create your views here.


class ProductListview(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['products'] = Product.objects.filter(is_active=True).all()
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.PositionBannerChoices.article_list)
        return context

    def get_queryset(self):
        query = super(ProductListview, self).get_queryset()
        category_name = self.kwargs.get('cat')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product


def categories_list(request, category_id):
    category = ProductCategory.objects.get(pk=category_id)
    books = Product.objects.filter(category=category)
    context = {
        'category': category,
        'books': books
    }
    return render(request, 'product_module/product_list_category.html', context)


# class Product_list_category_View(ListView):
#     template_name = 'product_module/product_list_category.html'
#     model = ProductCategory
#
#     def get_queryset(self):
#         query = super(Product_list_category_View, self).get_queryset()
#         category_name = self.kwargs.get('slug')
#         if category_name is not None:
#             query = query.filter(selected_books__slug__iexact=category_name)
#         return query


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_categories
    }
    return render(request, 'product_module/component/product_categories.html', context)

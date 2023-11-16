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
        query = super().get_queryset()
        category_name = self.kwargs.get('cat')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_categories
    }
    return render(request, 'product_module/component/product_categories.html', context)

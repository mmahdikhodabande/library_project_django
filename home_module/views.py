import datetime

from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView

from product_module.models import ProductCategory, Product, Auther, Product_time_free
from site_setting.models import SiteSetting, FooterLinkBox


class HomePageView(TemplateView):
    template_name = 'shared/index_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data()
        category_product = ProductCategory.objects.filter(is_active=True, is_delete=False)
        newest_product = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:6]
        authors = Auther.objects.all()
        free_products = Product_time_free.objects.all()
        li_free_product = []
        for product in free_products:
            if not product.is_discount_expired():
                li_free_product.append(product)
        context['category_product'] = category_product
        context['newest_product'] = newest_product
        context['authors'] = authors
        context['free_product'] = li_free_product
        categories = list(ProductCategory.objects.annotate(
            products_count=Count('product_categories')).filter(is_active=True,
                                                               is_delete=False,
                                                               products_count__gt=0)[:6])
        category_products = []
        for i in categories:
            item = {
                'id': i.id,
                'title': i.title,
                'products': list(i.product_categories.all()[:4])

            }
            category_products.append(item)
        context['category_products'] = category_products
        return context


def header_references_component(request):
    return render(request, 'shared/header_references_component.html')


def footer_references_component(request):
    return render(request, 'shared/footer_references_component.html')


def site_footer_partial(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_active_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set
    context = {
        'setting': setting,
        'footer_link_boxs': footer_link_boxes
    }
    return render(request, 'shared/site_footer_partial.html', context)


def site_header_partial(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_active_setting=True).first()
    category_product = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'setting': setting,
        'category_product': category_product
    }
    return render(request, 'shared/site_header_partial.html', context)


class AboutUsView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['site_setting'] = SiteSetting.objects.filter(is_active_setting=True).first()
        return context

from django.shortcuts import render
from django.views.generic import TemplateView

from site_setting.models import SiteSetting, FooterLinkBox


class HomePageView(TemplateView):
    template_name = 'shared/index_page.html'


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
    context = {
        'setting': setting
    }
    return render(request, 'shared/site_header_partial.html', context)


class AboutUsView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['site_setting'] = SiteSetting.objects.filter(is_active_setting=True).first()
        return context

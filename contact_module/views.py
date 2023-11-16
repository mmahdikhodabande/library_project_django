from django.views.generic import CreateView

from .forms import ContactUsForm
from .models import ContactUsModel
from site_setting.models import SiteSetting


# Create your views here.

class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    model = ContactUsModel
    form_class = ContactUsForm
    success_url = '/contact-us/'
    context_object_name = 'form'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['site_setting'] = SiteSetting.objects.filter(is_active_setting=True).first()
        return context

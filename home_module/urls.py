from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    # path('categori/<cat>', views.HomePageView.as_view(), name='home_page'),
    path('about-us', views.AboutUsView.as_view(), name='about_us_page')
]

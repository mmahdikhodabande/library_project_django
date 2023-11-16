from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Article, ArticleCategory, ArticleCommend
from site_setting.models import SiteBanner


# Create your views here.

class ArticleListView(ListView):
    template_name = 'article_module/article_list.html'
    model = Article
    paginate_by = 2
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['banners'] = SiteBanner.objects.filter(is_active=True, position__iexact=SiteBanner.PositionBannerChoices.article_list)
        context['articles_numbers'] = Article.objects.filter(is_active=True).order_by('-id')
        return context

    def get_queryset(self):
        query = super().get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query


class ArticleDetailView(DetailView):
    template_name = 'article_module/article_detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article: Article = kwargs.get('object')
        context['comments'] = ArticleCommend.objects.filter(article_id=article.id, parent=None).prefetch_related(
            'articlecommend_set')
        return context


def article_categories_component(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)
    context = {
        'articles_categories': article_main_categories
    }
    return render(request, 'article_module/component/article_category_component.html', context)


# def add_article_comment(request: HttpRequest):
#     return HttpResponse('hello')

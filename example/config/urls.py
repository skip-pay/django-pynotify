from django.urls import re_path as url

from articles.views import ArticleCreateView, ArticleListView, ArticleUpdateView


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article_list'),
    url(r'^articles/create/', ArticleCreateView.as_view(), name='article_create'),
    url(r'^articles/(?P<pk>\d+)/', ArticleUpdateView.as_view(), name='article_detail'),
]

from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import Template, Context
import articles, sys
sys.path.append('/home/merbroussard/axis2/stacked-up/articles/')
from articles.models import Article

register = template.Library()

@register.inclusion_tag('articles.html', takes_context=True)
def article_list(context):
    request = context['request']
    articles = Article.objects.all().order_by('sort_order')
    paginator = Paginator(articles, 7)
    if 'p' in request.GET:
        page = request.GET['p']
    else:
        page = 1
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    # if the url field is set, use that, otherwise /article/id
    for article in articles:
        if not article.url:
            article.url = "/article/%s"%(article.id)
    return {'items' : articles}
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from articles.models import Article
from django.shortcuts import render, render_to_response, redirect
from django.template import Context, loader, RequestContext
from django import template
register = template.Library()

import logging

logger = logging.getLogger(__name__)
logger.debug("Foo ")

def TestView(request, id):
    article = Article.objects.get(id=id)
    return render_to_response("article.html", {'id' : id, 'article' : article}, RequestContext(request))

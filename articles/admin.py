from django.db import models
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from adminsortable.admin import SortableAdminMixin

from django import forms
from .models import Article

class AdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Article

class ArticleAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = AdminForm

admin.site.register(Article, ArticleAdmin)
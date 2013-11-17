# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Article.body'
        db.alter_column('articles_article', 'body', self.gf('django.db.models.fields.CharField')(max_length=1000000))

    def backwards(self, orm):

        # Changing field 'Article.body'
        db.alter_column('articles_article', 'body', self.gf('django.db.models.fields.CharField')(max_length=100000))

    models = {
        'articles.article': {
            'Meta': {'ordering': "('sort_order',)", 'object_name': 'Article'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['articles']
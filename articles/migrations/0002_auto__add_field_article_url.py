# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.url'
        db.add_column('articles_article', 'url',
                      self.gf('django.db.models.fields.CharField')(default='#', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.url'
        db.delete_column('articles_article', 'url')


    models = {
        'articles.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'#'", 'max_length': '200'})
        }
    }

    complete_apps = ['articles']
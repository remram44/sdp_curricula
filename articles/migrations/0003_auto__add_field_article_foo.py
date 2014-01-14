# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.foo'
        db.add_column('articles_article', 'foo',
                      self.gf('aloha.fields.HTMLField')(styles=[], tags=[], default='', classes=set([]), blank=True, attributes={}, iframe_origins=[]),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.foo'
        db.delete_column('articles_article', 'foo')


    models = {
        'articles.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'foo': ('aloha.fields.HTMLField', [], {'styles': '[]', 'tags': '[]', 'classes': 'set([])', 'blank': 'True', 'attributes': '{}', 'iframe_origins': '[]'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['articles']
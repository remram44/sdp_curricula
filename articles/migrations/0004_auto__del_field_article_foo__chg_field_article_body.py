# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Article.foo'
        db.delete_column('articles_article', 'foo')


        # Changing field 'Article.body'
        db.alter_column('articles_article', 'body', self.gf('django.db.models.fields.CharField')(max_length=100000))

    def backwards(self, orm):
        # Adding field 'Article.foo'
        db.add_column('articles_article', 'foo',
                      self.gf('aloha.fields.HTMLField')(styles=[], tags=[], default='', classes=set([]), blank=True, attributes={}, iframe_origins=[]),
                      keep_default=False)


        # Changing field 'Article.body'
        db.alter_column('articles_article', 'body', self.gf('django.db.models.fields.TextField')())

    models = {
        'articles.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '100000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['articles']
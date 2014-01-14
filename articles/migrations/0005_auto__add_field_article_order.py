# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.order'
        db.add_column('articles_article', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)
        for index, article in enumerate(orm['Articles.Article'].objects.all()):
            article.order = index + 1
            article.save()

    def backwards(self, orm):
        # Deleting field 'Article.order'
        db.delete_column('articles_article', 'order')


    models = {
        'articles.article': {
            'Meta': {'ordering': "['order']", 'object_name': 'Article'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '100000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['articles']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field district on 'Vendor'
        db.delete_table('vendors_vendor_district')

        # Adding M2M table for field districts on 'Vendor'
        db.create_table('vendors_vendor_districts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vendor', models.ForeignKey(orm['vendors.vendor'], null=False)),
            ('district', models.ForeignKey(orm['schools.district'], null=False))
        ))
        db.create_unique('vendors_vendor_districts', ['vendor_id', 'district_id'])


    def backwards(self, orm):
        # Adding M2M table for field district on 'Vendor'
        db.create_table('vendors_vendor_district', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vendor', models.ForeignKey(orm['vendors.vendor'], null=False)),
            ('district', models.ForeignKey(orm['schools.district'], null=False))
        ))
        db.create_unique('vendors_vendor_district', ['vendor_id', 'district_id'])

        # Removing M2M table for field districts on 'Vendor'
        db.delete_table('vendors_vendor_districts')


    models = {
        'curricula.learningmaterial': {
            'Meta': {'object_name': 'LearningMaterial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isTeacherEdition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'material_type': ('django.db.models.fields.CharField', [], {'default': "'Book'", 'max_length': '20'}),
            'ordering_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'curricula.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.PublisherGroup']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publisher_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'curricula.publishergroup': {
            'Meta': {'object_name': 'PublisherGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schools.district': {
            'Meta': {'object_name': 'District'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schools.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'grade_end': ('django.db.models.fields.IntegerField', [], {}),
            'grade_start': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'school_id': ('django.db.models.fields.IntegerField', [], {}),
            'school_level': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'school_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.SchoolType']", 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_addr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        'schools.schooltype': {
            'Meta': {'object_name': 'SchoolType'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'vendors.inventoryrecord': {
            'Meta': {'object_name': 'InventoryRecord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.LearningMaterial']"}),
            'qty_lost_stolen': ('django.db.models.fields.IntegerField', [], {}),
            'qty_onsite': ('django.db.models.fields.IntegerField', [], {}),
            'qty_reallocated': ('django.db.models.fields.IntegerField', [], {}),
            'qty_to_student_class': ('django.db.models.fields.IntegerField', [], {}),
            'qty_to_student_home': ('django.db.models.fields.IntegerField', [], {}),
            'qty_unusable': ('django.db.models.fields.IntegerField', [], {}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.School']"})
        },
        'vendors.negotiatedprice': {
            'Meta': {'object_name': 'NegotiatedPrice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'negotiated_for_school_type': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'school_types'", 'symmetrical': 'False', 'to': "orm['schools.SchoolType']"}),
            'negotiated_year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2012', 'max_length': '4'}),
            'value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vendors.Vendor']", 'null': 'True'})
        },
        'vendors.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'districts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'districts'", 'symmetrical': 'False', 'to': "orm['schools.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['vendors']
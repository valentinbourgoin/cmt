# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Sponsor.logo'
        db.alter_column(u'core_sponsor', 'logo', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Sponsor.logo'
        db.alter_column(u'core_sponsor', 'logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'core.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.TeamSite']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'core.teamsite': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'TeamSite', '_ormbases': [u'sites.Site']},
            u'site_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True', 'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Team']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'team.championship': {
            'Meta': {'object_name': 'Championship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'team.team': {
            'Meta': {'object_name': 'Team'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Championship']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
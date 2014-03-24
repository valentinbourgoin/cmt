# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Skill.type'
        db.add_column(u'team_skill', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['team.SkillType']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Skill.type'
        db.delete_column(u'team_skill', 'type_id')


    models = {
        u'team.championship': {
            'Meta': {'object_name': 'Championship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'team.player': {
            'Meta': {'object_name': 'Player'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birthplace': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'feet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'positions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['team.Position']", 'through': u"orm['team.PlayerPosition']", 'symmetrical': 'False'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['team.Skill']", 'through': u"orm['team.PlayerSkill']", 'symmetrical': 'False'})
        },
        u'team.playerposition': {
            'Meta': {'object_name': 'PlayerPosition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Player']"}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Position']"}),
            'preference': ('django.db.models.fields.IntegerField', [], {})
        },
        u'team.playerskill': {
            'Meta': {'object_name': 'PlayerSkill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Player']"}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Skill']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'team.position': {
            'Meta': {'object_name': 'Position'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'team.skill': {
            'Meta': {'object_name': 'Skill'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.SkillType']"})
        },
        u'team.skilltype': {
            'Meta': {'object_name': 'SkillType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'team.team': {
            'Meta': {'object_name': 'Team'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['team']
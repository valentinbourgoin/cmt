# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Championship'
        db.create_table(u'team_championship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'team', ['Championship'])

        # Adding model 'Skill'
        db.create_table(u'team_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'team', ['Skill'])

        # Adding model 'Team'
        db.create_table(u'team_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'team', ['Team'])

        # Adding model 'PlayerPosition'
        db.create_table(u'team_playerposition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('preference', self.gf('django.db.models.fields.IntegerField')()),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Position'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Player'])),
        ))
        db.send_create_signal(u'team', ['PlayerPosition'])

        # Adding model 'Position'
        db.create_table(u'team_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'team', ['Position'])

        # Adding model 'Player'
        db.create_table(u'team_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('birthplace', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('feet', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'team', ['Player'])

        # Adding model 'SkillType'
        db.create_table(u'team_skilltype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'team', ['SkillType'])

        # Adding model 'PlayerSkill'
        db.create_table(u'team_playerskill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Skill'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Player'])),
        ))
        db.send_create_signal(u'team', ['PlayerSkill'])


    def backwards(self, orm):
        # Deleting model 'Championship'
        db.delete_table(u'team_championship')

        # Deleting model 'Skill'
        db.delete_table(u'team_skill')

        # Deleting model 'Team'
        db.delete_table(u'team_team')

        # Deleting model 'PlayerPosition'
        db.delete_table(u'team_playerposition')

        # Deleting model 'Position'
        db.delete_table(u'team_position')

        # Deleting model 'Player'
        db.delete_table(u'team_player')

        # Deleting model 'SkillType'
        db.delete_table(u'team_skilltype')

        # Deleting model 'PlayerSkill'
        db.delete_table(u'team_playerskill')


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
            'order': ('django.db.models.fields.IntegerField', [], {})
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
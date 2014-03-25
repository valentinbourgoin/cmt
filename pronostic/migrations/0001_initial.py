# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MatchDay'
        db.create_table(u'pronostic_matchday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('championship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Championship'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'pronostic', ['MatchDay'])

        # Adding model 'Match'
        db.create_table(u'pronostic_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match_day', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pronostic.MatchDay'])),
            ('date_min', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_max', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('team_home', self.gf('django.db.models.fields.related.ForeignKey')(related_name='team_home', to=orm['team.Team'])),
            ('team_away', self.gf('django.db.models.fields.related.ForeignKey')(related_name='team_away', to=orm['team.Team'])),
        ))
        db.send_create_signal(u'pronostic', ['Match'])

        # Adding model 'Pronostic'
        db.create_table(u'pronostic_pronostic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pronostic.Match'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('score_home', self.gf('django.db.models.fields.IntegerField')()),
            ('score_away', self.gf('django.db.models.fields.IntegerField')()),
            ('points', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'pronostic', ['Pronostic'])

        # Adding model 'PronosticPosition'
        db.create_table(u'pronostic_pronosticposition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pronostic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pronostic.Pronostic'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Player'])),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Position'])),
        ))
        db.send_create_signal(u'pronostic', ['PronosticPosition'])

        # Adding model 'PronosticGoal'
        db.create_table(u'pronostic_pronosticgoal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pronostic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pronostic.Pronostic'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Player'])),
            ('goal_number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pronostic', ['PronosticGoal'])

        # Adding model 'Result'
        db.create_table(u'pronostic_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pronostic.Match'])),
            ('score_home', self.gf('django.db.models.fields.IntegerField')()),
            ('score_away', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pronostic', ['Result'])

        # Adding model 'ResultPosition'
        db.create_table(u'pronostic_resultposition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('result', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pronostic.Result'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Player'])),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Position'])),
        ))
        db.send_create_signal(u'pronostic', ['ResultPosition'])

        # Adding model 'ResultGoal'
        db.create_table(u'pronostic_resultgoal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('result', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pronostic.Result'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Player'])),
            ('goal_number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pronostic', ['ResultGoal'])


    def backwards(self, orm):
        # Deleting model 'MatchDay'
        db.delete_table(u'pronostic_matchday')

        # Deleting model 'Match'
        db.delete_table(u'pronostic_match')

        # Deleting model 'Pronostic'
        db.delete_table(u'pronostic_pronostic')

        # Deleting model 'PronosticPosition'
        db.delete_table(u'pronostic_pronosticposition')

        # Deleting model 'PronosticGoal'
        db.delete_table(u'pronostic_pronosticgoal')

        # Deleting model 'Result'
        db.delete_table(u'pronostic_result')

        # Deleting model 'ResultPosition'
        db.delete_table(u'pronostic_resultposition')

        # Deleting model 'ResultGoal'
        db.delete_table(u'pronostic_resultgoal')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pronostic.match': {
            'Meta': {'object_name': 'Match'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'date_max': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_min': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pronostic.MatchDay']"}),
            'team_away': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_away'", 'to': u"orm['team.Team']"}),
            'team_home': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_home'", 'to': u"orm['team.Team']"})
        },
        u'pronostic.matchday': {
            'Meta': {'object_name': 'MatchDay'},
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Championship']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'pronostic.pronostic': {
            'Meta': {'object_name': 'Pronostic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pronostic.Match']"}),
            'points': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'positions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['team.Position']", 'through': u"orm['pronostic.PronosticPosition']", 'symmetrical': 'False'}),
            'score_away': ('django.db.models.fields.IntegerField', [], {}),
            'score_home': ('django.db.models.fields.IntegerField', [], {}),
            'scorers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['team.Player']", 'through': u"orm['pronostic.PronosticGoal']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'pronostic.pronosticgoal': {
            'Meta': {'object_name': 'PronosticGoal'},
            'goal_number': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Player']"}),
            'pronostic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pronostic.Pronostic']"})
        },
        u'pronostic.pronosticposition': {
            'Meta': {'object_name': 'PronosticPosition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Player']"}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Position']"}),
            'pronostic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pronostic.Pronostic']"})
        },
        u'pronostic.result': {
            'Meta': {'object_name': 'Result'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pronostic.Match']"}),
            'positions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['team.Position']", 'through': u"orm['pronostic.ResultPosition']", 'symmetrical': 'False'}),
            'score_away': ('django.db.models.fields.IntegerField', [], {}),
            'score_home': ('django.db.models.fields.IntegerField', [], {}),
            'scorers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['team.Player']", 'through': u"orm['pronostic.ResultGoal']", 'symmetrical': 'False'})
        },
        u'pronostic.resultgoal': {
            'Meta': {'object_name': 'ResultGoal'},
            'goal_number': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Player']"}),
            'result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pronostic.Result']"})
        },
        u'pronostic.resultposition': {
            'Meta': {'object_name': 'ResultPosition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Player']"}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Position']"}),
            'result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pronostic.Result']"})
        },
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
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['team.Skill']", 'through': u"orm['team.PlayerSkill']", 'symmetrical': 'False'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Team']", 'null': 'True', 'blank': 'True'})
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
            'championship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Championship']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pronostic']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table(u'biosensorsdb_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'biosensorsdb', ['Team'])

        # Adding model 'SensorInput'
        db.create_table(u'biosensorsdb_sensorinput', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'biosensorsdb', ['SensorInput'])

        # Adding model 'SensorOutput'
        db.create_table(u'biosensorsdb_sensoroutput', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'biosensorsdb', ['SensorOutput'])

        # Adding model 'Track'
        db.create_table(u'biosensorsdb_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'biosensorsdb', ['Track'])

        # Adding model 'Application'
        db.create_table(u'biosensorsdb_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'biosensorsdb', ['Application'])

        # Adding model 'CompetitionResult'
        db.create_table(u'biosensorsdb_competitionresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('result', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'biosensorsdb', ['CompetitionResult'])

        # Adding model 'Project'
        db.create_table(u'biosensorsdb_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['biosensorsdb.Team'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abstract', self.gf('django.db.models.fields.TextField')()),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['biosensorsdb.Track'])),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['biosensorsdb.Application'])),
        ))
        db.send_create_signal(u'biosensorsdb', ['Project'])

        # Adding M2M table for field inputs on 'Project'
        m2m_table_name = db.shorten_name(u'biosensorsdb_project_inputs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'biosensorsdb.project'], null=False)),
            ('sensorinput', models.ForeignKey(orm[u'biosensorsdb.sensorinput'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'sensorinput_id'])

        # Adding M2M table for field outputs on 'Project'
        m2m_table_name = db.shorten_name(u'biosensorsdb_project_outputs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'biosensorsdb.project'], null=False)),
            ('sensoroutput', models.ForeignKey(orm[u'biosensorsdb.sensoroutput'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'sensoroutput_id'])

        # Adding M2M table for field results on 'Project'
        m2m_table_name = db.shorten_name(u'biosensorsdb_project_results')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'biosensorsdb.project'], null=False)),
            ('competitionresult', models.ForeignKey(orm[u'biosensorsdb.competitionresult'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'competitionresult_id'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table(u'biosensorsdb_team')

        # Deleting model 'SensorInput'
        db.delete_table(u'biosensorsdb_sensorinput')

        # Deleting model 'SensorOutput'
        db.delete_table(u'biosensorsdb_sensoroutput')

        # Deleting model 'Track'
        db.delete_table(u'biosensorsdb_track')

        # Deleting model 'Application'
        db.delete_table(u'biosensorsdb_application')

        # Deleting model 'CompetitionResult'
        db.delete_table(u'biosensorsdb_competitionresult')

        # Deleting model 'Project'
        db.delete_table(u'biosensorsdb_project')

        # Removing M2M table for field inputs on 'Project'
        db.delete_table(db.shorten_name(u'biosensorsdb_project_inputs'))

        # Removing M2M table for field outputs on 'Project'
        db.delete_table(db.shorten_name(u'biosensorsdb_project_outputs'))

        # Removing M2M table for field results on 'Project'
        db.delete_table(db.shorten_name(u'biosensorsdb_project_results'))


    models = {
        u'biosensorsdb.application': {
            'Meta': {'object_name': 'Application'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'biosensorsdb.competitionresult': {
            'Meta': {'object_name': 'CompetitionResult'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'biosensorsdb.project': {
            'Meta': {'object_name': 'Project'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biosensorsdb.Application']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inputs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['biosensorsdb.SensorInput']", 'symmetrical': 'False'}),
            'outputs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['biosensorsdb.SensorOutput']", 'symmetrical': 'False'}),
            'results': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['biosensorsdb.CompetitionResult']", 'symmetrical': 'False'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biosensorsdb.Team']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biosensorsdb.Track']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'biosensorsdb.sensorinput': {
            'Meta': {'object_name': 'SensorInput'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'biosensorsdb.sensoroutput': {
            'Meta': {'object_name': 'SensorOutput'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'biosensorsdb.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'biosensorsdb.track': {
            'Meta': {'object_name': 'Track'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['biosensorsdb']
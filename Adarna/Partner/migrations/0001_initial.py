# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum', models.TextField(verbose_name='Curriculum :')),
            ],
        ),
        migrations.CreateModel(
            name='MemberDetails',
            fields=[
                ('UUID', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=20, verbose_name='First Name :')),
                ('lastName', models.CharField(max_length=20, verbose_name='Last Name :')),
                ('dob', models.DateField(verbose_name='Date of birth :')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender :')),
                ('Sap', models.IntegerField(verbose_name='SAP id :')),
                ('email', models.EmailField(max_length=254, verbose_name='Email id :')),
                ('phone', models.IntegerField(verbose_name='Phone Number :')),
                ('division', models.CharField(max_length=1, verbose_name='Division :')),
                ('year', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Year :')),
                ('course', models.CharField(choices=[('MBA(Tech)', 'MBATech'), ('BTech', 'BTech')], max_length=10, verbose_name='Course :')),
                ('stream', models.CharField(choices=[('IT', 'IT'), ('CS', 'CS'), ('EXTC', 'EXTC'), ('Civil', 'Civil'), ('Chemical', 'Chemical'), ('Mechanical', 'Mechanical')], max_length=10, verbose_name='Stream :')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('partner', models.CharField(max_length=30, verbose_name='Name :')),
                ('contact', models.IntegerField(verbose_name='Contact No. :')),
                ('email', models.EmailField(max_length=254, verbose_name='Email id :')),
                ('coordinatorName', models.CharField(max_length=30, verbose_name='Coordinator :')),
                ('location', models.CharField(max_length=10, verbose_name='Location:')),
                ('address', models.CharField(max_length=160, verbose_name='Address :')),
                ('spl', models.CharField(max_length=30, verbose_name='Specializations :')),
                ('SoS', models.IntegerField(verbose_name='Seats per slot :')),
                ('remark', models.TextField(verbose_name='Remark :')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Partner.MemberDetails')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeSlots', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkingDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workingDay', models.CharField(choices=[('Su', 'Sunday'), ('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('Th', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday')], max_length=2)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Partner.Partner')),
            ],
        ),
        migrations.AddField(
            model_name='timeslots',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Partner.WorkingDay'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Partner.Partner'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-25 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=64, verbose_name='\u516c\u53f8\u540d\u79f0')),
                ('company_phone_number', models.CharField(max_length=11, verbose_name='\u516c\u53f8\u7535\u8bdd')),
                ('license_num', models.CharField(max_length=124, verbose_name='\u5907\u6848\u53f7')),
                ('change_time', models.IntegerField(default=5, help_text='\u65f6\u95f4\u95f4\u9694,\u5355\u4f4d\u662f\u5206\u949f\uff01', verbose_name='\u5fae\u4fe1\u5207\u6362\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u516c\u53f8\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='LmobileproInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, verbose_name='\u79f0\u547c')),
                ('phone_number', models.CharField(max_length=11, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('image', models.ImageField(help_text='\u56fe\u7247\u5927\u5c0f169\xd7169px', upload_to='imgs/strategy/', verbose_name='\u5fae\u4fe1\u4e8c\u7ef4\u7801')),
                ('is_show', models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u767e\u5ea6(lmobilepro.html)',
            },
        ),
        migrations.CreateModel(
            name='LpcproInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, verbose_name='\u79f0\u547c')),
                ('phone_number', models.CharField(max_length=11, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('image', models.ImageField(help_text='\u56fe\u7247\u5927\u5c0f169\xd7169px', upload_to='imgs/strategy/', verbose_name='\u5fae\u4fe1\u4e8c\u7ef4\u7801')),
                ('is_show', models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u767e\u5ea6(lpcpro.html)',
            },
        ),
        migrations.CreateModel(
            name='YmobileproInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, verbose_name='\u79f0\u547c')),
                ('phone_number', models.CharField(max_length=11, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('image', models.ImageField(help_text='\u56fe\u7247\u5927\u5c0f169\xd7169px', upload_to='imgs/strategy/', verbose_name='\u5fae\u4fe1\u4e8c\u7ef4\u7801')),
                ('is_show', models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u795e\u9a6c(ymobilepro2.html)',
            },
        ),
        migrations.CreateModel(
            name='ZmobileStrategy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, verbose_name='\u79f0\u547c')),
                ('phone_number', models.CharField(max_length=11, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('image', models.ImageField(help_text='\u56fe\u7247\u5927\u5c0f169\xd7169px', upload_to='imgs/strategy/', verbose_name='\u5fae\u4fe1\u4e8c\u7ef4\u7801')),
                ('is_show', models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u795e\u9a6c(zmobilestrategy.html)',
            },
        ),
        migrations.CreateModel(
            name='ZpcproInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, verbose_name='\u79f0\u547c')),
                ('phone_number', models.CharField(max_length=11, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('image', models.ImageField(help_text='\u56fe\u7247\u5927\u5c0f169\xd7169px', upload_to='imgs/strategy/', verbose_name='\u5fae\u4fe1\u4e8c\u7ef4\u7801')),
                ('is_show', models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u767e\u5ea6(zpcpro.html)',
            },
        ),
    ]

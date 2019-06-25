# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_phone_number', 'license_num', 'change_time']


@admin.register(LpcproInfo)
class LpcproInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'is_show', 'add_time']


@admin.register(LmobileproInfo)
class LmobileproInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'is_show', 'add_time']


@admin.register(YmobileproInfo)
class YmobileproInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'is_show', 'add_time']


@admin.register(ZpcproInfo)
class ZpcproInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'is_show', 'add_time']


@admin.register(ZmobileStrategy)
class ZmobileStrategyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'is_show', 'add_time']

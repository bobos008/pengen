# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'phone_number', 'license_num', 'business_license']


@admin.register(SeasonalFineProducts)
class SeasonalFineProductsAdmin(admin.ModelAdmin):
    list_display = ['small_title', 'title']


@admin.register(SuperAffordable)
class SuperAffordableAdmin(admin.ModelAdmin):
    list_display = ['small_title', 'title']


@admin.register(ThemeRoute)
class ThemeRouteAdmin(admin.ModelAdmin):
    list_display = ['small_title', 'title']


@admin.register(PopularExplosions)
class PopularExplosionsAdmin(admin.ModelAdmin):
    list_display = ['small_title', 'title']


@admin.register(SceneryCulture)
class SceneryCultureAdmin(admin.ModelAdmin):
    list_display = ['small_title', 'title']


@admin.register(RaidersRoute)
class RaidersRouteAdmin(admin.ModelAdmin):
    list_display = ['small_title', 'title']


@admin.register(CustomRoute)
class CustomRouteAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'customer_name', 'customer_phone', 'from_location', 'customer_number', 'budget', 'number_day']


@admin.register(TripKnowledge)
class TripKnowledgeAdmin(admin.ModelAdmin):
    list_display = ['knowledge_id', 'knowledge_title', 'add_times']


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['about_id']


@admin.register(TripShare)
class TripShareAdmin(admin.ModelAdmin):
    list_display = ['id', 'add_times']

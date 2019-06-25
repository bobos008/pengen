# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver

# Create your models here.
class CompanyInfo(models.Model):
    """公司信息"""
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(u'公司名称', max_length=64)
    company_phone_number = models.CharField(u'公司电话', max_length=11)
    license_num = models.CharField(u'备案号', max_length=124)
    change_time = models.IntegerField(u'微信切换时间', help_text="时间间隔,单位是分钟！", default=5)

    class Meta:
        verbose_name_plural = u'公司信息'


class LpcproInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'称呼', max_length=120)
    phone_number = models.CharField(u'联系电话', max_length=11)
    image = models.ImageField(u'微信二维码', help_text="图片大小169×169px", upload_to='imgs/strategy/')
    is_show = models.BooleanField(u'是否显示', default=True)
    add_time = models.DateField(u'添加时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = u'百度(lpcpro.html)'


# 删除lpcproinfo图片文件
@receiver(pre_delete, sender=LpcproInfo)
def lpcproinfo_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class LmobileproInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'称呼', max_length=120)
    phone_number = models.CharField(u'联系电话', max_length=11)
    image = models.ImageField(u'微信二维码', help_text="图片大小169×169px", upload_to='imgs/strategy/')
    is_show = models.BooleanField(u'是否显示', default=True)
    add_time = models.DateField(u'添加时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = u'百度(lmobilepro.html)'


# 删除lmobileproinfo图片文件
@receiver(pre_delete, sender=LmobileproInfo)
def lmobileproinfo_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class YmobileproInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'称呼', max_length=120)
    phone_number = models.CharField(u'联系电话', max_length=11)
    image = models.ImageField(u'微信二维码', help_text="图片大小169×169px", upload_to='imgs/strategy/')
    is_show = models.BooleanField(u'是否显示', default=True)
    add_time = models.DateField(u'添加时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = u'神马(ymobilepro2.html)'


# 删除ymobileproinfo图片文件
@receiver(pre_delete, sender=YmobileproInfo)
def ymobilepro_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class ZpcproInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'称呼', max_length=120)
    phone_number = models.CharField(u'联系电话', max_length=11)
    image = models.ImageField(u'微信二维码', help_text="图片大小169×169px", upload_to='imgs/strategy/')
    is_show = models.BooleanField(u'是否显示', default=True)
    add_time = models.DateField(u'添加时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = u'百度(zpcpro.html)'


# 删除zpcproinfo图片文件
@receiver(pre_delete, sender=ZpcproInfo)
def zpcpro_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class ZmobileStrategy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'称呼', max_length=120)
    phone_number = models.CharField(u'联系电话', max_length=11)
    image = models.ImageField(u'微信二维码', help_text="图片大小169×169px", upload_to='imgs/strategy/')
    is_show = models.BooleanField(u'是否显示', default=True)
    add_time = models.DateField(u'添加时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = u'神马(zmobilestrategy.html)'


# 删除ZmobileStrategy图片文件
@receiver(pre_delete, sender=ZmobileStrategy)
def zmobilestr_delete(sender, instance, **kwargs):
    instance.image.delete(False)

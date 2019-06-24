# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver
from tinymce.models import HTMLField


# Create your models here.
class CompanyInfo(models.Model):
    """公司信息"""
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(u'公司名称', max_length=64)
    service_hotline = models.CharField(u'服务热线', max_length=11)
    phone_number = models.CharField(u'业务电话', max_length=11)
    qq = models.CharField(u'QQ号', max_length=32)
    wechat = models.CharField(u'微信号', max_length=64)
    website = models.CharField(u'公司网址', max_length=124)    
    license_num = models.CharField(u'许可证号', max_length=124)    
    business_license = models.CharField(u'营业执照号', max_length=124, default="null")
    account_name = models.CharField(u'开户名', max_length=32, default="null")
    Remittances_name = models.CharField(u'汇款名称', max_length=32, default="null")
    account_number = models.CharField(u'帐号', max_length=124)
    qrcode_img1 = models.ImageField(u'公司网页头部小的二维码', help_text="图片大小为76×76px", upload_to='imgs/')
    qrcode_img2 = models.ImageField(u'公司网页底部大的二维码', help_text="图片大小为122×122px", upload_to='imgs/')
    # qrcode_img3 = models.ImageField(u'公司网页中部的二维码', help_text="图片大小为237x237px", upload_to="imgs/")
    logo_img1 = models.ImageField(u'公司网页头部logo', help_text="图片大小为293×90px", upload_to='imgs/')
    logo_img2 = models.ImageField(u'公司网页底部logo', help_text="图片大小为114×145px", upload_to='imgs/')

    class Meta:
        verbose_name_plural = u'公司信息'


# 删除公司信息图片文件
@receiver(pre_delete, sender=CompanyInfo)
def companyinfo_delete(sender, instance, **kwargs):
    instance.qrcode_img1.delete(False)
    instance.qrcode_img2.delete(False)
    instance.logo_img1.delete(False)
    instance.logo_img2.delete(False)


class SeasonalFineProducts(models.Model):
    """当季精品"""
    TRIP_STYLE = (
        (0, u'请选择'),
        (1, u'纯玩团'),
        (2, u'精品游'),
        (3, u'品质游'),
        (4, u'全景游'),
        (5, u'深度游'),
    )
    id = models.AutoField(primary_key=True)
    small_title = models.CharField(u'小标题', help_text="小标题最多输入8个汉字！", max_length=8, null=True, blank=True)
    title = models.CharField(u'标题', help_text="标题最多输入12个汉字!", max_length=12)
    goods_add_time = models.DateField(u'添加时间', null=True)
    order_number = models.IntegerField(u'月订单数', default=0)
    popularity_num = models.IntegerField(u'人气数', default=0)
    route1 = models.CharField(u'路线1', null=True, blank=True, help_text="路线1最多输入32个汉字!", max_length=32)
    route2 = models.CharField(u'路线2', null=True, help_text="路线2最多输入32个汉字!", max_length=32, blank=True)
    route3 = models.CharField(u'路线3', null=True, help_text="路线3最多输入32个汉字!", max_length=32, blank=True)
    trip1_title = models.CharField(u'景点1', null=True, help_text="景点1最多输入64个汉字!", max_length=64, blank=True)
    trip1_introduce = models.TextField(u'景点介绍1', null=True, blank=True)
    trip2_title = models.CharField(u'景点2', null=True, help_text="景点2最多输入64个汉字!", max_length=64, blank=True)
    trip2_introduce = models.TextField(u'景点介绍2', null=True, blank=True)
    trip3_title = models.CharField(u'景点3', null=True, help_text="景点3最多输入64个汉字!", max_length=64, blank=True)
    trip3_introduce = models.TextField(u'景点介绍3', null=True, blank=True)
    trip4_title = models.CharField(u'景点4', null=True, help_text="景点4最多输入64个汉字!", max_length=64, blank=True)
    trip4_introduce = models.TextField(u'景点介绍4', null=True, blank=True)
    trip5_title = models.CharField(u'景点5', null=True, help_text="景点5最多输入64个汉字!", max_length=64, blank=True)
    trip5_introduce = models.TextField(u'景点介绍5', null=True, blank=True)
    contain_cost = models.TextField(u'费用包含', null=True, blank=True)
    not_contain_cost = models.TextField(u'费用不含', null=True, blank=True)
    self_funded_project = models.TextField(u'自费项目', null=True, blank=True)
    goods_image = models.ImageField(u'头图', help_text="图片大小为456×242px！", null=True, upload_to='imgs/')
    image1 = models.ImageField(u'详情图片1', help_text="图片大小为119×87px!", upload_to='imgs/')
    image2 = models.ImageField(u'详情图片2', help_text="图片大小为119×87px!", upload_to='imgs/')
    image3 = models.ImageField(u'详情图片3', help_text="图片大小为119×87px!", upload_to='imgs/')
    trip_style = models.IntegerField(u'旅游类型', choices=TRIP_STYLE, default=0)

    class Meta:
        verbose_name_plural = u'当季精品'


# 当季精品
@receiver(pre_delete, sender=SeasonalFineProducts)
def seasonfine_delete(sender, instance, **kwargs):
    instance.goods_image.delete(False)
    instance.image1.delete(False)
    instance.image2.delete(False)
    instance.image3.delete(False)


class SuperAffordable(models.Model):
    """超级特惠"""
    TRIP_STYLE = (
        (0, u'请选择'),
        (1, u'纯玩团'),
        (2, u'精品游'),
        (3, u'品质游'),
        (4, u'全景游'),
        (5, u'深度游'),
    )
    id = models.AutoField(primary_key=True)
    small_title = models.CharField(u'小标题', help_text="小标题最多输入8个汉字！", null=True, max_length=8, blank=True)
    title = models.CharField(u'标题', help_text="标题最多输入12个汉字!", max_length=12)
    goods_add_time = models.DateField(u'添加时间', null=True)
    order_number = models.IntegerField(u'月订单数', default=0)
    popularity_num = models.IntegerField(u'人气数', default=0)
    route1 = models.CharField(u'路线1', help_text="路线1最多输入32个汉字!", max_length=32)
    route2 = models.CharField(u'路线2', help_text="路线2最多输入32个汉字!", max_length=32)
    route3 = models.CharField(u'路线3', help_text="路线3最多输入32个汉字!", max_length=32)
    trip1_title = models.CharField(u'景点1',  null=True, help_text="景点1最多输入64个汉字!", max_length=64)
    trip1_introduce = models.TextField(u'景点介绍1', null=True)
    # trip1_introduce = HTMLField()
    trip2_title = models.CharField(u'景点2', help_text="景点2最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip2_introduce = models.TextField(u'景点介绍2', null=True, blank=True)
    trip3_title = models.CharField(u'景点3', help_text="景点3最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip3_introduce = models.TextField(u'景点介绍3', null=True, blank=True)
    trip4_title = models.CharField(u'景点4', help_text="景点4最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip4_introduce = models.TextField(u'景点介绍4', null=True, blank=True)
    trip5_title = models.CharField(u'景点5', help_text="景点5最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip5_introduce = models.TextField(u'景点介绍5', null=True, blank=True)
    contain_cost = models.TextField(u'费用包含', null=True, blank=True)
    not_contain_cost = models.TextField(u'费用不含', null=True, blank=True)
    self_funded_project = models.TextField(u'自费项目', null=True, blank=True)
    goods_image = models.ImageField(u'头图', help_text="图片大小为456×242px！", null=True, upload_to='imgs/', blank=True)
    image1 = models.ImageField(u'详情图片1', help_text="图片大小为119×87px!", upload_to='imgs/')
    image2 = models.ImageField(u'详情图片2', help_text="图片大小为119×87px!", upload_to='imgs/')
    image3 = models.ImageField(u'详情图片3', help_text="图片大小为119×87px!", upload_to='imgs/')
    trip_style = models.IntegerField(u'旅游类型', choices=TRIP_STYLE, default=0)

    class Meta:
        verbose_name_plural = u'超级特惠'


# 超级特惠 
@receiver(pre_delete, sender=SuperAffordable)
def superaffordable_delete(sender, instance, **kwargs):
    instance.goods_image.delete(False)
    instance.image1.delete(False)
    instance.image2.delete(False)
    instance.image3.delete(False)


class ThemeRoute(models.Model):
    """主题线路"""
    TRIP_STYLE = (
        (0, u'请选择'),
        (1, u'亲子游'),
        (2, u'商务游'),
        (3, u'蜜月游'),
        (4, u'毕业游'),
        (5, u'老年游'),
        (6, u'包团游'),
    )
    id = models.AutoField(primary_key=True)
    small_title = models.CharField(u'小标题', help_text="小标题最多输入8个汉字！", null=True, max_length=8, blank=True)
    title = models.CharField(u'标题', help_text="标题最多输入12个汉字!", max_length=12)
    goods_add_time = models.DateField(u'添加时间', null=True)
    order_number = models.IntegerField(u'月订单数', default=0)
    popularity_num = models.IntegerField(u'人气数', default=0)
    route1 = models.CharField(u'路线1', help_text="路线1最多输入32个汉字!", max_length=32)
    route2 = models.CharField(u'路线2', help_text="路线2最多输入32个汉字!", max_length=32)
    route3 = models.CharField(u'路线3', help_text="路线3最多输入32个汉字!", max_length=32)
    trip1_title = models.CharField(u'景点1', help_text="景点1最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip1_introduce = models.TextField(u'景点介绍1', null=True, blank=True)
    trip2_title = models.CharField(u'景点2', help_text="景点2最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip2_introduce = models.TextField(u'景点介绍2', null=True, blank=True)
    trip3_title = models.CharField(u'景点3', help_text="景点3最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip3_introduce = models.TextField(u'景点介绍3', null=True, blank=True)
    trip4_title = models.CharField(u'景点4', help_text="景点4最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip4_introduce = models.TextField(u'景点介绍4', null=True, blank=True)
    trip5_title = models.CharField(u'景点5', help_text="景点5最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip5_introduce = models.TextField(u'景点介绍5', null=True, blank=True)
    contain_cost = models.TextField(u'费用包含')
    not_contain_cost = models.TextField(u'费用不含')
    self_funded_project = models.TextField(u'自费项目')
    goods_image = models.ImageField(u'头图', help_text="图片大小为456×242px！", null=True, upload_to='imgs/', blank=True)
    image1 = models.ImageField(u'详情图片1', help_text="图片大小为119×87px!", upload_to='imgs/')
    image2 = models.ImageField(u'详情图片2', help_text="图片大小为119×87px!", upload_to='imgs/')
    image3 = models.ImageField(u'详情图片3', help_text="图片大小为119×87px!", upload_to='imgs/')
    trip_style = models.IntegerField(u'旅游类型', choices=TRIP_STYLE, default=0)

    class Meta:
        verbose_name_plural = u'主题线路'


# 主题线路 
@receiver(pre_delete, sender=ThemeRoute)
def themeroute_delete(sender, instance, **kwargs):
    instance.goods_image.delete(False)
    instance.image1.delete(False)
    instance.image2.delete(False)
    instance.image3.delete(False)


class PopularExplosions(models.Model):
    """人气爆款"""
    TRIP_STYLE = (
        (0, u'请选择'),
        (1, u'纯玩团'),
        (2, u'精品游'),
        (3, u'品质游'),
        (4, u'全景游'),
        (5, u'深度游'),
    )
    id = models.AutoField(primary_key=True)
    small_title = models.CharField(u'小标题', help_text="小标题最多输入8个汉字！", null=True, max_length=8, blank=True)
    title = models.CharField(u'标题', help_text="标题最多输入12个汉字!", max_length=12)
    goods_add_time = models.DateField(u'添加时间', null=True)
    order_number = models.IntegerField(u'月订单数', default=0)
    popularity_num = models.IntegerField(u'人气数', default=0)
    route1 = models.CharField(u'路线1', help_text="路线1最多输入32个汉字!", max_length=32)
    route2 = models.CharField(u'路线2', help_text="路线2最多输入32个汉字!", max_length=32)
    route3 = models.CharField(u'路线3', help_text="路线3最多输入32个汉字!", max_length=32)
    trip1_title = models.CharField(u'景点1', help_text="景点1最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip1_introduce = models.TextField(u'景点介绍1', null=True, blank=True)
    trip2_title = models.CharField(u'景点2', help_text="景点2最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip2_introduce = models.TextField(u'景点介绍2', null=True, blank=True)
    trip3_title = models.CharField(u'景点3', help_text="景点3最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip3_introduce = models.TextField(u'景点介绍3', null=True, blank=True)
    trip4_title = models.CharField(u'景点4', help_text="景点4最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip4_introduce = models.TextField(u'景点介绍4', null=True, blank=True)
    trip5_title = models.CharField(u'景点5', help_text="景点5最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip5_introduce = models.TextField(u'景点介绍5', null=True, blank=True)
    contain_cost = models.TextField(u'费用包含')
    not_contain_cost = models.TextField(u'费用不含')
    self_funded_project = models.TextField(u'自费项目')
    goods_image = models.ImageField(u'头图', help_text="图片大小为456×242px！", null=True, upload_to='imgs/')
    image1 = models.ImageField(u'详情图片1', help_text="图片大小为119×87px!", upload_to='imgs/')
    image2 = models.ImageField(u'详情图片2', help_text="图片大小为119×87px!", upload_to='imgs/')
    image3 = models.ImageField(u'详情图片3', help_text="图片大小为119×87px!", upload_to='imgs/')
    trip_style = models.IntegerField(u'旅游类型', choices=TRIP_STYLE, default='0')

    class Meta:
        verbose_name_plural = u'人气爆款'


# 人气爆款 
@receiver(pre_delete, sender=PopularExplosions)
def popularexplosions_delete(sender, instance, **kwargs):
    instance.goods_image.delete(False)
    instance.image1.delete(False)
    instance.image2.delete(False)
    instance.image3.delete(False)


class SceneryCulture(models.Model):
    """景点文化"""
    id = models.AutoField(primary_key=True)
    small_title = models.CharField(u'小标题', help_text="小标题最多输入4个汉字！", null=True, max_length=4, blank=True)
    title = models.CharField(u'标题', help_text="标题最多输入12个汉字!", max_length=12)
    goods_add_time = models.DateField(u'添加时间', null=True)
    order_number = models.IntegerField(u'月订单数', default=0)
    popularity_num = models.IntegerField(u'人气数', default=0)
    route1 = models.CharField(u'路线1', help_text="路线1最多输入32个汉字!", max_length=32)
    route2 = models.CharField(u'路线2', help_text="路线2最多输入32个汉字!", max_length=32)
    route3 = models.CharField(u'路线3', help_text="路线3最多输入32个汉字!", max_length=32)
    trip1_title = models.CharField(u'景点1', help_text="景点1最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip1_introduce = models.TextField(u'景点介绍1', null=True, blank=True)
    trip2_title = models.CharField(u'景点2', help_text="景点2最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip2_introduce = models.TextField(u'景点介绍2', null=True, blank=True)
    trip3_title = models.CharField(u'景点3', help_text="景点3最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip3_introduce = models.TextField(u'景点介绍3', null=True, blank=True)
    trip4_title = models.CharField(u'景点4', help_text="景点4最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip4_introduce = models.TextField(u'景点介绍4', null=True, blank=True)
    trip5_title = models.CharField(u'景点5', help_text="景点5最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip5_introduce = models.TextField(u'景点介绍5', null=True, blank=True)
    contain_cost = models.TextField(u'费用包含')
    not_contain_cost = models.TextField(u'费用不含')
    self_funded_project = models.TextField(u'自费项目')
    goods_image = models.ImageField(u'头图', help_text="图片大小为456×242px！", null=True, upload_to='imgs/')
    image1 = models.ImageField(u'详情图片1', help_text="图片大小为119×87px!", upload_to='imgs/')
    image2 = models.ImageField(u'详情图片2', help_text="图片大小为119×87px!", upload_to='imgs/')
    image3 = models.ImageField(u'详情图片3', help_text="图片大小为119×87px!", upload_to='imgs/')

    class Meta:
        verbose_name_plural = u'景点文化'


# 景点文化 
@receiver(pre_delete, sender=SceneryCulture)
def sceneryculture_delete(sender, instance, **kwargs):
    instance.goods_image.delete(False)
    instance.image1.delete(False)
    instance.image2.delete(False)
    instance.image3.delete(False)


class RaidersRoute(models.Model):
    """攻略路线"""
    id = models.AutoField(primary_key=True)
    small_title = models.CharField(u'小标题', help_text="小标题最多输入4个汉字！", null=True, max_length=4, blank=True)
    title = models.CharField(u'标题', help_text="标题最多输入12个汉字!", max_length=12)
    goods_add_time = models.DateField(u'添加时间', null=True)
    order_number = models.IntegerField(u'月订单数', default=0)
    popularity_num = models.IntegerField(u'人气数', default=0)
    route1 = models.CharField(u'路线1', help_text="路线1最多输入32个汉字!", max_length=32)
    route2 = models.CharField(u'路线2', help_text="路线2最多输入32个汉字!", max_length=32)
    route3 = models.CharField(u'路线3', help_text="路线3最多输入32个汉字!", max_length=32)
    trip1_title = models.CharField(u'景点1', help_text="景点1最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip1_introduce = models.TextField(u'景点介绍1', null=True, blank=True)
    trip2_title = models.CharField(u'景点2', help_text="景点2最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip2_introduce = models.TextField(u'景点介绍2', null=True, blank=True)
    trip3_title = models.CharField(u'景点3', help_text="景点3最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip3_introduce = models.TextField(u'景点介绍3', null=True, blank=True)
    trip4_title = models.CharField(u'景点4', help_text="景点4最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip4_introduce = models.TextField(u'景点介绍4', null=True, blank=True)
    trip5_title = models.CharField(u'景点5', help_text="景点5最多输入64个汉字!", max_length=64, null=True, blank=True)
    trip5_introduce = models.TextField(u'景点介绍5', null=True, blank=True)
    contain_cost = models.TextField(u'费用包含')
    not_contain_cost = models.TextField(u'费用不含')
    self_funded_project = models.TextField(u'自费项目')
    goods_image = models.ImageField(u'头图', help_text="图片大小为456×242px！", null=True, upload_to='imgs/')
    image1 = models.ImageField(u'详情图片1', help_text="图片大小为119×87px!", upload_to='imgs/')
    image2 = models.ImageField(u'详情图片2', help_text="图片大小为119×87px!", upload_to='imgs/')
    image3 = models.ImageField(u'详情图片3', help_text="图片大小为119×87px!", upload_to='imgs/')

    class Meta:
        verbose_name_plural = u'攻略路线'


# 攻略线路 
@receiver(pre_delete, sender=RaidersRoute)
def raidersroute_delete(sender, instance, **kwargs):
    instance.goods_image.delete(False)
    instance.image1.delete(False)
    instance.image2.delete(False)
    instance.image3.delete(False)


class CustomRoute(models.Model):
    """定制个人路线"""
    customer_id = models.AutoField(primary_key=True)
    from_location = models.CharField(u'出发城市', max_length=124, null=True)
    customer_name = models.CharField(u'客户名字', max_length=124, default='null')
    customer_phone = models.CharField(u'客户手机号', max_length=11)
    customer_number = models.IntegerField(u'客户人数', null=True)
    budget = models.IntegerField(u'预算', null=True)
    number_day = models.IntegerField(u'出游天数', null=True)

    class Meta:
        verbose_name_plural = u'定制个人路线'


class TripKnowledge(models.Model):
    """旅游知识"""
    knowledge_id = models.AutoField(primary_key=True)
    knowledge_title = models.CharField(u'旅游标题', max_length=16)
    knowledge_image = models.ImageField(u'图片', help_text="图片大小为463×335px!", upload_to='imgs/')
    add_times = models.DateField(u'添加时间')
    part_content = models.TextField(u'部分文章内容', help_text='文章部分内容,用于首页显示，字数最多260个字', max_length=260)
    knowledge_content = HTMLField('文章全部内容')

    class Meta:
        verbose_name_plural = u'旅游知识'


# 旅游知识
@receiver(pre_delete, sender=TripKnowledge)
def tripknowledge_delete(sender, instance, **kwargs):
    isinstance.knowledge_image.delete(False)


class AboutUs(models.Model):
    """关于我们"""
    about_id = models.AutoField(primary_key=True)
    brief_introduction = HTMLField('公司简介')
    contact = HTMLField('联系方式')
    Travel_contract = HTMLField('旅游合同')
    booking = HTMLField('预订方式')
    faq = HTMLField('常见问题')
    join_explain = HTMLField('参团说明')
    server_explain = HTMLField('服务说明')

    class Meta:
        verbose_name_plural = u'关于我们'


class TripShare(models.Model):
    """旅游分享"""
    id = models.AutoField(primary_key=True)
    add_times = models.DateField(u'添加时间')
    content = HTMLField('内容')

    class Meta:
        verbose_name_plural = u'旅游分享'

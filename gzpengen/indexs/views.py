# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from models import *


# Create your views here.
def index(request):
    ''' 加载首页 '''
    try:
        companyInfo = CompanyInfo.objects.get(pk='1')
        tripShare = TripShare.objects.get(pk='1')
    except:
        companyInfo = ''
        tripShare = ''
    SA_set = select_data(SuperAffordable)
    SF_set = select_data(SeasonalFineProducts)
    SF_left_set = SF_set[:2]
    SF_right_set = SF_set[2:4]

    popular_set1 = select_data(PopularExplosions, trip_style=1)
    popular_set2 = select_data(PopularExplosions, trip_style=2)
    popular_set3 = select_data(PopularExplosions, trip_style=3)
    popular_set4 = select_data(PopularExplosions, trip_style=4)
    popular_set5 = select_data(PopularExplosions, trip_style=5)

    TR_set1 = select_data(ThemeRoute, trip_style=1)
    TR_set2 = select_data(ThemeRoute, trip_style=2)
    TR_set3 = select_data(ThemeRoute, trip_style=3)
    TR_set4 = select_data(ThemeRoute, trip_style=4)
    TR_set5 = select_data(ThemeRoute, trip_style=5)
    TR_set6 = select_data(ThemeRoute, trip_style=6)

    datas = {
        'SA_set': SA_set,
        'sf_left_set': SF_left_set,
        'sf_right_set': SF_right_set,
        'popular_set1': popular_set1,
        'popular_set2': popular_set2,
        'popular_set3': popular_set3,
        'popular_set4': popular_set4,
        'popular_set5': popular_set5,
        'TR_set1': TR_set1,
        'TR_set2': TR_set2,
        'TR_set3': TR_set3,
        'TR_set4': TR_set4,
        'TR_set5': TR_set5,
        'TR_set6': TR_set6,
        'companyInfo': companyInfo,
        'tripShare': tripShare,
        'showMenu': True
    }
    return render(request, 'home/index.html', datas)


def select_data(current_model, choose_kw='index', trip_style=None, limits=4):
    '''
    查询
    current_model: 数据表模型
    trip_style: 旅游类型选择
    limits: 查询个数
    choose_kw: 选择查询字段
    '''
    try:
        if trip_style:
            current_select_obj = current_model.objects.filter(trip_style=trip_style)
        else:
            current_select_obj = current_model.objects
        if choose_kw == 'index':
            select_set = current_select_obj.values(
                'id',
                'title',
                'order_number',
                'goods_image'
            ).order_by('-id')[:limits]
        elif choose_kw == 'more':
            select_set = current_select_obj.values(
                'id',
                'title',
                'route1',
                'route2',
                'route3',
                'goods_image'
            ).order_by('-id')[:limits]
        else:
            select_set = current_select_obj.all().order_by('-id')[:limits]
        return select_set
    except:
        return ''


def boutique(request):
    ''' 当季精品 '''
    try:
        companyInfo = CompanyInfo.objects.get(pk='1')
        data_set = SeasonalFineProducts.objects
        data_sets = data_set.values(
            'id',
            'title',
            'route1',
            'route2',
            'route3',
            'goods_image'
        ).order_by('-id')[:4]
        data_num = len(data_set.values('id').all())
    except:
        companyInfo = '' 
        data_sets = ''
        data_num = 0
    data_set1 = select_data(SeasonalFineProducts, choose_kw='more', trip_style=1) 
    data_set2 = select_data(SeasonalFineProducts, choose_kw='more', trip_style=2) 
    data_set3 = select_data(SeasonalFineProducts, choose_kw='more', trip_style=3) 
    data_set4 = select_data(SeasonalFineProducts, choose_kw='more', trip_style=4) 
    data_set5 = select_data(SeasonalFineProducts, choose_kw='more', trip_style=5) 

    datas = {
        'data_num': data_num,
        'data_sets': data_sets,
        'data_sets1': data_set1,
        'data_sets2': data_set2,
        'data_sets3': data_set3,
        'data_sets4': data_set4,
        'data_sets5': data_set5,
        'companyInfo': companyInfo
    }
    return render(request, 'home/boutique.html', datas)


def concerning(request):
    ''' 关于我们 '''
    try:
        companyInfo = CompanyInfo.objects.get(pk='1')
        aboutus_set = AboutUs.objects.get(pk=1)
    except:
        aboutus_set = ''
        companyInfo = ''
    datas = {
        'aboutus_set': aboutus_set,
        'companyInfo': companyInfo
    }
    return render(request, 'home/concerning.html', datas)


def customizedc(request):
    ''' 定制出游 '''
    try:
        companyInfo = CompanyInfo.objects.get(pk='1')
    except:
        companyInfo = ''
    datas = {
        'companyInfo': companyInfo
    }
    return render(request, 'home/customizedc.html', datas)


def addcustom(request):
    ''' 添加定制个人信息 '''
    result = True
    customer_name = request.POST.get('customer_name', '')
    customer_phone = request.POST.get('customer_phone', '')
    if (not customer_name) or (not customer_phone):
        return JsonResponse({'res': False})
    from_location = request.POST.get('from_location', '')
    customer_number = request.POST.get('customer_number', 0)
    budget = request.POST.get('budget', 0)
    number_day = request.POST.get('number_day', 0)
    try:
        CustomRoute.objects.create(
            from_location=from_location,
            customer_name=customer_name,
            customer_phone=customer_phone,
            customer_number=int(customer_number) if customer_number else 0,
            budget=int(budget) if budget else 0,
            number_day=int(number_day) if number_day else 0
        )
    except:
        result = False
    datas = {
        'res': result
    }
    return JsonResponse(datas)


def detail(request, table_name, new_id):
    ''' 详情页 '''
    data_set = ''
    try:
        if table_name == 'SuperAffordable':
            if new_id:
                data_set = SuperAffordable.objects.get(pk=new_id)
        elif table_name == 'SeasonalFineProducts':
            if new_id:
                data_set = SeasonalFineProducts.objects.get(pk=new_id)
        elif table_name == 'PopularExplosions':
            if new_id:
                data_set = PopularExplosions.objects.get(pk=new_id)
        elif table_name == 'ThemeRoute':
            if new_id:
                data_set = ThemeRoute.objects.get(pk=new_id)
        companyInfo = CompanyInfo.objects.get(pk='1')
    except:
        data_set = ''
        companyInfo = ''
    datas = {
        'data': data_set,
        'companyInfo': companyInfo
    }
    return render(request, 'home/details.html', datas)


def indulgence(request):
    ''' 超级特惠 '''
    try:
        companyInfo = CompanyInfo.objects.get(pk='1')
        data_set = SuperAffordable.objects
        data_sets = data_set.values(
            'id',
            'title',
            'route1',
            'route2',
            'route3',
            'goods_image'
        ).order_by('-id')[:4]
        data_num = len(data_set.values('id').all())
    except:
        companyInfo = ''
        data_num = 0
        data_sets = ''
    data_set1 = select_data(SuperAffordable, choose_kw='more', trip_style=1)
    data_set2 = select_data(SuperAffordable, choose_kw='more', trip_style=2)
    data_set3 = select_data(SuperAffordable, choose_kw='more', trip_style=3)
    data_set4 = select_data(SuperAffordable, choose_kw='more', trip_style=4)
    data_set5 = select_data(SuperAffordable, choose_kw='more', trip_style=5)
    datas = {
        'data_num': data_num,
        'data_sets': data_sets,
        'data_sets1': data_set1,
        'data_sets2': data_set2,
        'data_sets3': data_set3,
        'data_sets4': data_set4,
        'data_sets5': data_set5,
        'companyInfo': companyInfo
    }
    return render(request, 'home/indulgence.html', datas)


def itinerary(request):
    ''' 主题路线 '''
    try:
        companyInfo = CompanyInfo.objects.get(pk='1')
        data_set = ThemeRoute.objects
        data_sets = data_set.values(
            'id',
            'title',
            'route1',
            'route2',
            'route3',
            'goods_image'
        ).order_by('-id')[:4]
        data_num = len(data_set.values('id').all())
    except:
        companyInfo = ''
        data_num = 0
        data_sets = ''
    data_set1 = select_data(ThemeRoute, choose_kw='more', trip_style=1)
    data_set2 = select_data(ThemeRoute, choose_kw='more', trip_style=2)
    data_set3 = select_data(ThemeRoute, choose_kw='more', trip_style=3)
    data_set4 = select_data(ThemeRoute, choose_kw='more', trip_style=4)
    data_set5 = select_data(ThemeRoute, choose_kw='more', trip_style=5)
    data_set6 = select_data(ThemeRoute, choose_kw='more', trip_style=6)
    datas = {
        'data_num': data_num,
        'data_sets': data_sets,
        'data_sets1': data_set1,
        'data_sets2': data_set2,
        'data_sets3': data_set3,
        'data_sets4': data_set4,
        'data_sets5': data_set5,
        'data_sets6': data_set6,
        'companyInfo': companyInfo
    }
    return render(request, 'home/itinerary.html', datas)


def knowledge(request):
    ''' 旅游知识 '''
    try:
        companyInfo = CompanyInfo.objects.get(pk='1')
        tk_set = TripKnowledge.objects.values(
            'knowledge_id',
            'knowledge_title',
            'knowledge_image',
            'add_times',
            'part_content',
        ).order_by('-knowledge_id')[:3]
    except:
        companyInfo = ''
        tk_set = ''
    datas = {
        'tk_data': tk_set,
        'companyInfo': companyInfo
    }
    return render(request, 'home/knowledge.html', datas)


def popular(request):
    ''' 人气爆款 '''
    try:
        companyInfo = CompanyInfo.objects.get(pk='1')
        data_set = PopularExplosions.objects
        data_sets = data_set.values(
            'id',
            'title',
            'route1',
            'route2',
            'route3',
            'goods_image'
        ).order_by('-id')[:4]
        data_num = len(data_set.values('id').all())
    except:
        data_num = 0
        data_sets = ''
        companyInfo = ''
    data_set1 = select_data(PopularExplosions, choose_kw='more', trip_style=1)
    data_set2 = select_data(PopularExplosions, choose_kw='more', trip_style=2)
    data_set3 = select_data(PopularExplosions, choose_kw='more', trip_style=3)
    data_set4 = select_data(PopularExplosions, choose_kw='more', trip_style=4)
    data_set5 = select_data(PopularExplosions, choose_kw='more', trip_style=5)
    datas = {
        'data_num': data_num,
        'data_sets': data_sets,
        'data_sets1': data_set1,
        'data_sets2': data_set2,
        'data_sets3': data_set3,
        'data_sets4': data_set4,
        'data_sets5': data_set5,
        'companyInfo': companyInfo
    }
    return render(request, 'home/popular.html', datas)


def scenic(request):
    ''' 景点文化 '''
    try:
        companyInfo = CompanyInfo.objects.get(pk='1')
        data_set = SceneryCulture.objects.values(
            'id',
            'title',
            'route1',
            'route2',
            'route3',
            'goods_image'
        ).order_by('-id')
        data_num = len(data_set)
        data_set = data_set[:4]
    except:
        companyInfo = ''
        data_num = 0 
        data_set = ''

    datas = {
        'data_num': data_num,
        'data_set': data_set,
        'companyInfo': companyInfo
    }
    return render(request, 'home/scenic.html', datas)


def strategy(request):
    ''' 攻略路线 '''
    try:
        companyInfo = CompanyInfo.objects.get(pk='1')
        data_set = RaidersRoute.objects.values(
            'id',
            'title',
            'route1',
            'route2',
            'route3',
            'goods_image'
        ).order_by('-id')
        data_num = len(data_set)
        data_set = data_set[:4]
    except:
        companyInfo = ''
        data_num = 0 
        data_set = ''

    datas = {
        'data_num': data_num,
        'data_set': data_set,
        'companyInfo': companyInfo
    }
    return render(request, 'home/strategy.html', datas)

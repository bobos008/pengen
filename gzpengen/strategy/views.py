# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from models import *

# Create your views here.
def lpcpro(request):
    company_info = CompanyInfo.objects.all()[:1]
    if len(company_info) > 0:
        company_info = company_info[0]
    datas = {
        'company_info': company_info,
    }
    return render(request, 'strategy/lpcpro.html', datas)


def lpcpro_data(request):

    username = request.COOKIES.get('lpcpro_name', '')
    phone_number = request.COOKIES.get('lpcpro_phone_number', '')
    img_url = request.COOKIES.get('lpcpro_image', '')

    if (not username) and (not phone_number) and (not img_url) :
        company_set = CompanyInfo.objects.all()[:1]
        change_minute = 0
        if len(company_set) > 0:
            change_minute = company_set[0].change_time
        if (not change_minute) and (not change_minute.isdigit()):
            change_minute = 5
        else:
            change_minute = int(change_minute)
        current_minute = time.localtime().tm_min
        lpcpro_datas = LpcproInfo.objects.filter(
            is_show=True
        ).all().values()
        data_count = len(lpcpro_datas)
        list_index = int(current_minute/change_minute)%data_count
        lpcpro_list =  list(lpcpro_datas)
        lpcpro_data = lpcpro_list[list_index]
        username = lpcpro_data.get('name', '')
        phone_number = lpcpro_data.get('phone_number', '')
        img_url = lpcpro_data.get('image', '')
        datas = {
            'username': username,
            'phone_number': phone_number,
            'img_url': img_url
        }
        exist_time = 3600 * 1
        response = JsonResponse(datas)
        response.set_cookie('lpcpro_name', username, max_age=exist_time)
        response.set_cookie('lpcpro_phone_number', phone_number, max_age=exist_time)
        response.set_cookie('lpcpro_image', img_url, max_age=exist_time)
        return response

    datas = {
        'username': username,
        'phone_number': phone_number,
        'img_url': img_url
    }
    return JsonResponse(datas)


def lmobilepro(request):
    company_info = CompanyInfo.objects.all()[:1]
    if len(company_info) > 0:
        company_info = company_info[0]
    datas = {
        'company_info': company_info,
    }
    return render(request, 'strategy/lmobilepro.html', datas)


def lmobilepro_data(request):

    username = request.COOKIES.get('lmobilepro_name', '')
    phone_number = request.COOKIES.get('lmobilepro_phone_number', '')
    img_url = request.COOKIES.get('lmobilepro_image', '')

    if (not username) and (not phone_number) and (not img_url) :
        company_set = CompanyInfo.objects.all()[:1]
        change_minute = 0
        if len(company_set) > 0:
            change_minute = company_set[0].change_time
        if (not change_minute) and (not change_minute.isdigit()):
            change_minute = 5
        else:
            change_minute = int(change_minute)
        current_minute = time.localtime().tm_min
        lpcpro_datas = LmobileproInfo.objects.filter(
            is_show=True
        ).all().values()
        data_count = len(lpcpro_datas)
        list_index = int(current_minute/change_minute)%data_count
        lpcpro_list =  list(lpcpro_datas)
        lpcpro_data = lpcpro_list[list_index]
        username = lpcpro_data.get('name', '')
        phone_number = lpcpro_data.get('phone_number', '')
        img_url = lpcpro_data.get('image', '')
        datas = {
            'username': username,
            'phone_number': phone_number,
            'img_url': img_url
        }
        exist_time = 3600 * 1
        response = JsonResponse(datas)
        response.set_cookie('lmobilepro_name', username, max_age=exist_time)
        response.set_cookie('lmobilepro_phone_number', phone_number, max_age=exist_time)
        response.set_cookie('lmobilepro_image', img_url, max_age=exist_time)
        return response

    datas = {
        'username': username,
        'phone_number': phone_number,
        'img_url': img_url
    }
    return JsonResponse(datas)


def zpcpro(request):
    company_info = CompanyInfo.objects.all()[:1]
    if len(company_info) > 0:
        company_info = company_info[0]
    datas = {
        'company_info': company_info,
    }
    return render(request, 'strategy/zpcpro.html', datas)


def zpcpro_data(request):

    username = request.COOKIES.get('zpcpro_name', '')
    phone_number = request.COOKIES.get('zpcpro_phone_number', '')
    img_url = request.COOKIES.get('zpcpro_image', '')

    if (not username) and (not phone_number) and (not img_url) :
        company_set = CompanyInfo.objects.all()[:1]
        change_minute = 0
        if len(company_set) > 0:
            change_minute = company_set[0].change_time
        if (not change_minute) and (not change_minute.isdigit()):
            change_minute = 5
        else:
            change_minute = int(change_minute)
        current_minute = time.localtime().tm_min
        lpcpro_datas = ZpcproInfo.objects.filter(
            is_show=True
        ).all().values()
        data_count = len(lpcpro_datas)
        list_index = int(current_minute/change_minute)%data_count
        lpcpro_list =  list(lpcpro_datas)
        lpcpro_data = lpcpro_list[list_index]
        username = lpcpro_data.get('name', '')
        phone_number = lpcpro_data.get('phone_number', '')
        img_url = lpcpro_data.get('image', '')
        datas = {
            'username': username,
            'phone_number': phone_number,
            'img_url': img_url
        }
        exist_time = 3600 * 1
        response = JsonResponse(datas)
        response.set_cookie('zpcpro_name', username, max_age=exist_time)
        response.set_cookie('zpcpro_phone_number', phone_number, max_age=exist_time)
        response.set_cookie('zpcpro_image', img_url, max_age=exist_time)
        return response

    datas = {
        'username': username,
        'phone_number': phone_number,
        'img_url': img_url
    }
    return JsonResponse(datas)


def zmobilestrategy(request):
    company_info = CompanyInfo.objects.all()[:1]
    if len(company_info) > 0:
        company_info = company_info[0]
    datas = {
        'company_info': company_info,
    }
    return render(request, 'strategy/zmobilestrategy.html', datas)


def zmobilestrategy_data(request):

    username = request.COOKIES.get('zmobilestr_name', '')
    phone_number = request.COOKIES.get('zmobilestr_phone_number', '')
    img_url = request.COOKIES.get('zmobilestr_image', '')

    if (not username) and (not phone_number) and (not img_url) :
        company_set = CompanyInfo.objects.all()[:1]
        change_minute = 0
        if len(company_set) > 0:
            change_minute = company_set[0].change_time
        if (not change_minute) and (not change_minute.isdigit()):
            change_minute = 5
        else:
            change_minute = int(change_minute)
        current_minute = time.localtime().tm_min
        lpcpro_datas = ZmobileStrategy.objects.filter(
            is_show=True
        ).all().values()
        data_count = len(lpcpro_datas)
        list_index = int(current_minute/change_minute)%data_count
        lpcpro_list =  list(lpcpro_datas)
        lpcpro_data = lpcpro_list[list_index]
        username = lpcpro_data.get('name', '')
        phone_number = lpcpro_data.get('phone_number', '')
        img_url = lpcpro_data.get('image', '')
        datas = {
            'username': username,
            'phone_number': phone_number,
            'img_url': img_url
        }
        exist_time = 3600 * 1
        response = JsonResponse(datas)
        response.set_cookie('zmobilestr_name', username, max_age=exist_time)
        response.set_cookie('zmobilestr_phone_number', phone_number, max_age=exist_time)
        response.set_cookie('zmobilestr_image', img_url, max_age=exist_time)
        return response

    datas = {
        'username': username,
        'phone_number': phone_number,
        'img_url': img_url
    }
    return JsonResponse(datas)


def ymobilepro2(request):
    company_info = CompanyInfo.objects.all()[:1]
    if len(company_info) > 0:
        company_info = company_info[0]
    datas = {
        'company_info': company_info,
    }
    return render(request, 'strategy/ymobilepro2.html', datas)


def ymobilepro2_data(request):

    username = request.COOKIES.get('ymobilepro2_name', '')
    phone_number = request.COOKIES.get('ymobilepro2_phone_number', '')
    img_url = request.COOKIES.get('ymobilepro2_image', '')

    if (not username) and (not phone_number) and (not img_url) :
        company_set = CompanyInfo.objects.all()[:1]
        change_minute = 0
        if len(company_set) > 0:
            change_minute = company_set[0].change_time
        if (not change_minute) and (not change_minute.isdigit()):
            change_minute = 5
        else:
            change_minute = int(change_minute)
        current_minute = time.localtime().tm_min
        lpcpro_datas = YmobileproInfo.objects.filter(
            is_show=True
        ).all().values()
        data_count = len(lpcpro_datas)
        list_index = int(current_minute/change_minute)%data_count
        lpcpro_list =  list(lpcpro_datas)
        lpcpro_data = lpcpro_list[list_index]
        username = lpcpro_data.get('name', '')
        phone_number = lpcpro_data.get('phone_number', '')
        img_url = lpcpro_data.get('image', '')
        datas = {
            'username': username,
            'phone_number': phone_number,
            'img_url': img_url
        }
        exist_time = 3600 * 1
        response = JsonResponse(datas)
        response.set_cookie('ymobilepro2_name', username, max_age=exist_time)
        response.set_cookie('ymobilepro2_phone_number', phone_number, max_age=exist_time)
        response.set_cookie('ymobilepro2_image', img_url, max_age=exist_time)
        return response

    datas = {
        'username': username,
        'phone_number': phone_number,
        'img_url': img_url
    }
    return JsonResponse(datas)

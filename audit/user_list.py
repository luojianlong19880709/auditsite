# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from audit.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage,InvalidPage
import re
import time
from tools import get_date,mysqlconn




def user_list(req):


	datas = User.objects.all()
	limit = 20
	paginator = Paginator(datas, limit)

	try:
		page = int(req.GET.get('page','1'))

	except ValueError:
		page = 1

	try:
		datas = paginator.page(page)

	except (EmptyPage, InvalidPage):
		
		datas = paginator.page(paginator.num_pages)
	
	if 'user_name' in req.GET:
		user_name = req.GET.get('user_name')
		datas = User.objects.filter(user_name=user_name)

		return render_to_response('user_list.html',{'datas':datas})


	return render_to_response('user_list.html',{'datas':datas})

		
	



def user_reg(req):
	if 'user_name' in req.GET:
		user_name = req.GET.get('user_name')
		cmd = 'select * from audit_user where user_name="%s"' %user_name
		result = mysqlconn.mysql_conn(cmd)
		if len(result)!=0:
			return HttpResponse('用户名已存在')
			exit()				
		applicant = req.GET.get('applicant')
		department = req.GET.get('department')
		leader = req.GET.get('leader')
		mobile_phone = req.GET.get('mobile_phone')
		tel_number = req.GET.get('tel_number')
		email = req.GET.get('email')
		storage = req.GET.get('storage')
		hadoop_client_ip = req.GET.get('hadoop_client_ip')
		if storage == '':
			storage = 0.0
		storage_per_month = req.GET.get('storage_per_month')
		if storage_per_month == '':
			storage_per_month = 0.0
		access_business_range = req.GET.get('access_business_range')
		description = req.GET.get('description')
		apply_date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
		reginfo = User(user_name=user_name, applicant=applicant, department=department, leader=leader, mobile_phone=mobile_phone, tel_number=tel_number, email=email, storage=storage, storage_per_month=storage_per_month, access_business_range=access_business_range, description=description, apply_date=apply_date, hadoop_client_ip=hadoop_client_ip)
		reginfo.save()

		if reginfo:
			return HttpResponse('注册成功')
			
		else:
			return HttpResponse('注册失败')

	return render_to_response('user_register.html',{})

		



def user_del(req,user_name):
	userinfo = User.objects.get(user_name=user_name)
	userinfo.delete()


	
	return render_to_response('user_list.html',{'datas':User.objects.all()})




def user_update(req,user_name):
	userinfo = User.objects.filter(user_name=user_name)
	if 'user_name' in req.GET:
		applicant = req.GET.get('applicant')
		department = req.GET.get('department')
		leader = req.GET.get('leader')
		mobile_phone = req.GET.get('mobile_phone')
		tel_number = req.GET.get('tel_number')
		email = req.GET.get('email')
		storage = req.GET.get('storage')
		storage_per_month = req.GET.get('storage_per_month')
		access_business_range = req.GET.get('access_business_range')
		description = req.GET.get('description')
		hadoop_client_ip = req.GET.get('hadoop_client_ip')
		userinfo.update(applicant=applicant)
		userinfo.update(department=department)
		userinfo.update(leader=leader)
		userinfo.update(mobile_phone=mobile_phone)
		userinfo.update(tel_number=tel_number)
		userinfo.update(email=email)
		userinfo.update(storage=storage)
		userinfo.update(storage_per_month=storage_per_month)
		userinfo.update(access_business_range=access_business_range)
		userinfo.update(description=description)
		userinfo.update(hadoop_client_ip=hadoop_client_ip)
		
				
	return render_to_response('user_info.html',{'userinfo':userinfo})


def user_info(req,user_name):
	userinfo = User.objects.filter(user_name=user_name)
	
	return render_to_response('user_profile.html',{'userinfo':userinfo})











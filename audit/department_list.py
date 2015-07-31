# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from audit.models import Department,User
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage,InvalidPage
import re
import time
from tools import get_date,mysqlconn


def department_list(req):


	datas = Department.objects.all()
	limit = 5
	paginator = Paginator(datas, limit)

	try:
		page = int(req.GET.get('page','1'))

	except ValueError:
		page = 1

	try:
		datas = paginator.page(page)

	except (EmptyPage, InvalidPage):
		
		datas = paginator.page(paginator.num_pages)
	
	if 'department' in req.GET:
		department = req.GET.get('department')
		datas = Department.objects.filter(department=department)

		return render_to_response('department_list.html',{'datas':datas})


	return render_to_response('department_list.html',{'datas':datas})

		
	



def department_reg(req):
	if 'department' in req.GET:
		department = req.GET.get('department')
		cmd = 'select * from audit_department where department="%s"' %department
		result = mysqlconn.mysql_conn(cmd)
		if len(result)!=0:
			return HttpResponse('部门已存在')
			exit()				
		leader = req.GET.get('leader')
		depart_mail = req.GET.get('depart_mail')
		leader_mobile = req.GET.get('leader_mobile')
		leader_mail = req.GET.get('leader_mail')

		reginfo = Department(department=department, leader=leader, depart_mail=depart_mail, leader_mobile=leader_mobile, leader_mail=leader_mail)
		reginfo.save()

		if reginfo:
			return HttpResponse('注册成功')
		else:
			return HttpResponse('注册失败')

	return render_to_response('department_register.html',{})

		



def department_del(req,department):
	departmentinfo = Department.objects.get(department=department)
	departmentinfo.delete()


	
	return render_to_response('department_list.html',{'datas':Department.objects.all()})




def department_update(req,department):
	departmentinfo = Department.objects.filter(department=department)
	if 'department' in req.GET:
		department = req.GET.get('department')
		leader = req.GET.get('leader')
		depart_mail = req.GET.get('depart_mail')
		leader_mobile = req.GET.get('leader_mobile')
		leader_mail = req.GET.get('leader_mail')
		departmentinfo.update(leader=leader)
		departmentinfo.update(depart_mail=depart_mail)
		departmentinfo.update(leader_mobile=leader_mobile)
		departmentinfo.update(leader_mail=leader_mail)
		
		
				
	return render_to_response('department_info.html',{'departmentinfo':departmentinfo})


def department_info(req,department):
	departmentinfo = User.objects.filter(department=department)
	limit = 5
        paginator = Paginator(departmentinfo, limit)

        try:
                page = int(req.GET.get('page','1'))

        except ValueError:
                page = 1

        try:
                departmentinfo = paginator.page(page)

        except (EmptyPage, InvalidPage):

                departmentinfo = paginator.page(paginator.num_pages)

	
	return render_to_response('department_profile.html',{'departmentinfo':departmentinfo})











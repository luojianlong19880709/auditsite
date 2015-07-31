# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from audit.models import Department1,User1
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage,InvalidPage
import re
import time



def department_list(req):


	datas = Department1.objects.all()
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
		datas = Department1.objects.filter(department=department)

		return render_to_response('department_list1.html',{'datas':datas})


	return render_to_response('department_list1.html',{'datas':datas})

		
	



def department_reg(req):
	if 'department' in req.GET:
		department = req.GET.get('department')
		cmd = 'select * from audit_department1 where department="%s"' %department
		result = mysql_conn(cmd)
		if len(result)!=0:
			return HttpResponse('部门已存在')
			exit()				
		leader = req.GET.get('leader')
		depart_mail = req.GET.get('depart_mail')
		leader_mobile = req.GET.get('leader_mobile')
		leader_mail = req.GET.get('leader_mail')

		reginfo = Department1(department=department, leader=leader, depart_mail=depart_mail, leader_mobile=leader_mobile, leader_mail=leader_mail)
		reginfo.save()

		if reginfo:
			return HttpResponse('注册成功')
		else:
			return HttpResponse('注册失败')

	return render_to_response('department_register1.html',{})

		



def department_del(req,department):
	departmentinfo = Department1.objects.get(department=department)
	departmentinfo.delete()


	
	return render_to_response('department_list1.html',{'datas':Department1.objects.all()})




def department_update(req,department):
	departmentinfo = Department1.objects.filter(department=department)
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
		
		
				
	return render_to_response('department_info1.html',{'departmentinfo':departmentinfo})


def department_info(req,department):
	departmentinfo = User1.objects.filter(department=department)
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

	
	return render_to_response('department_profile1.html',{'departmentinfo':departmentinfo})











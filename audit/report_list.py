# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from audit.models import Depart_report,Detail_report
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage,InvalidPage
import re
import time


	


def report_list(req):
	departmentlist = Detail_report.objects.values('department').distinct()
	datas = Depart_report.objects.all()
	limit = 10
	paginator = Paginator(datas, limit)
	try:
		page = int(req.GET.get('page','1'))

	except ValueError:
        	page = 1
	try:
                datas = paginator.page(page)
	except (EmptyPage, InvalidPage):
                        datas = paginator.page(paginator.num_pages)
#	return render_to_response('report_list.html',{'datas':datas,'departmentlist':departmentlist})

	if 'department' in req.GET:
		department = req.GET.get('department')
		datas_detail = Detail_report.objects.filter(department=department)
		paginator_detail = Paginator(datas_detail, limit)
		try:
			page_detail = int(req.GET.get('page_detail','1'))
		except ValueError:

			page_detail = 1
		
		try:
			datas_detail = paginator_detail.page(page_detail)

		except (EmptyPage, InvalidPage):

                        datas_detail = paginator_detail.page(paginator_detail.num_pages)


		return render_to_response('report_list.html',{'datas_detail':datas_detail,'departmentlist':departmentlist,'datas':datas,'department':department})


	else:
		

		return render_to_response('report_list.html',{'departmentlist':departmentlist,'datas':datas})


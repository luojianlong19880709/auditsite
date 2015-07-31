from django.shortcuts import render_to_response
from audit.models import Job_status_yz1,Job_total_yz1
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
import time
import re
import time
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage,InvalidPage


	

def user_status(req):
	userlist = Job_status_yz1.objects.values('jobuser').distinct()
	datas_sort = Job_total_yz1.objects.order_by('-computeTime')[0:10]
	if 'beginTimeshow' in req.GET and 'endTimeshow' in req.GET:
		startTime1 = req.GET.get('beginTimeshow')
		startTime2 = req.GET.get('endTimeshow')
		jobuser = req.GET.get('user_name')
		jobstate = req.GET.get('status')
		limit = 10
		if jobstate == 'total':
			datas = Job_status_yz1.objects.filter(startTime__gt=startTime1).filter(startTime__lt=startTime2).filter(jobuser=jobuser)
		else:

			datas = Job_status_yz1.objects.filter(startTime__gt=startTime1).filter(startTime__lt=startTime2).filter(jobuser=jobuser).filter(jobstate=jobstate)
		paginator = Paginator(datas, limit)
	
		try:
			page = int(req.GET.get('page','1'))

		except ValueError:
			page = 1

		try:
			datas = paginator.page(page)
		except (EmptyPage, InvalidPage):
			datas = paginator.page(paginator.num_pages)

		return render_to_response('user_statistic1.html',{'userlist':userlist,'datas':datas,'startTime1':startTime1,'startTime2':startTime2,'jobuser':jobuser,'jobstate':jobstate})
	



	if 'beginTimeshow_sort' in req.GET and 'endTimeshow_sort' in req.GET:
		if req.GET.has_key('search_sort'):
			startTime_sort1 = req.GET.get('beginTimeshow_sort')
			startTime_sort2 = req.GET.get('endTimeshow_sort')
			sort_type = req.GET.get('sort_type')
			sort_dim = req.GET.get('sort_dim')		
			if sort_type == '20-':

				datas_sort = Job_total_yz1.objects.filter(startTime__gt=startTime_sort1).filter(startTime__lt=startTime_sort2).order_by(sort_dim)[0:20]

				return render_to_response('user_statistic1.html',{'userlist':userlist,'datas_sort':datas_sort})

			elif sort_type == '10-':

				datas_sort = Job_total_yz1.objects.filter(startTime__gt=startTime_sort1).filter(startTime__lt=startTime_sort2).order_by(sort_dim)[0:10]

				return render_to_response('user_statistic1.html',{'userlist':userlist,'datas_sort':datas_sort})

			elif sort_type == '20+':

				datas_sort = Job_total_yz1.objects.filter(startTime__gt=startTime_sort1).filter(startTime__lt=startTime_sort2).order_by('-'+sort_dim)[0:20]

				return render_to_response('user_statistic1.html',{'userlist':userlist,'datas_sort':datas_sort})
			
			elif sort_type == '10+':

				datas_sort = Job_total_yz1.objects.filter(startTime__gt=startTime_sort1).filter(startTime__lt=startTime_sort2).order_by('-'+sort_dim)[0:10]

				return render_to_response('user_statistic1.html',{'userlist':userlist,'datas_sort':datas_sort})



			return render_to_response('user_statistic1.html',{'userlist':userlist})

	
	else:
		return render_to_response('user_statistic1.html',{'userlist':userlist,'datas_sort':datas_sort})

# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from audit.models import Depart_report,Detail_report
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage,InvalidPage
from tools import get_date,mysqlconn
import re
import time




def spend_list(req):
	now_startTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	now_time = time.strftime("%H:%M:%S",time.localtime(time.time()))
	one_month_startTime = get_date.get_today_month(-1) + ' ' + now_time
	cmd = 'select u.department,count(us.jobuser) as usernum, sum(us.jobnum) as jobnum, sum(us.mapnum) as mapnum, sum(us.reducenum) as reducenum, sum(us.totaltime) as totaltime, sum(us.totalcpucost) as totalcpucost from(select jd.jobuser,count(1) as jobnum, sum(mapsTotal) as  mapnum, sum(reducesTotal) as reducenum, sum(computeTime) as totaltime, sum(cpu_cost_time) as totalcpucost from audit_job_status_yz jd force index(startTime) where jd.startTime >= "%s" and jd.startTime <= "%s"  group by jd.jobuser) us, audit_user u where us.jobuser=u.user_name group by u.department  order by totaltime desc limit 10' %(one_month_startTime,now_startTime)

	datas = mysqlconn.mysql_conn(cmd)
		
#	return render_to_response('spend_list.html',{'datas':datas})
	
	if 'beginTime' in req.GET and 'endTime' in req.GET:
		startTime1 = req.GET.get('beginTime')
		startTime2 = req.GET.get('endTime')
		cmd1 = 'select u.department,count(us.jobuser) as usernum, sum(us.jobnum) as jobnum, sum(us.mapnum) as mapnum, sum(us.reducenum) as reducenum, sum(us.totaltime) as totaltime, sum(us.totalcpucost) as totalcpucost from(select jd.jobuser,count(1) as jobnum, sum(mapsTotal) as  mapnum, sum(reducesTotal) as reducenum, sum(computeTime) as totaltime, sum(cpu_cost_time) as totalcpucost from audit_job_status_yz jd force index(startTime) where jd.startTime >= "%s" and jd.startTime <= "%s"  group by jd.jobuser) us, audit_user u where us.jobuser=u.user_name group by u.department  order by totaltime desc limit 10' %(startTime1,startTime2)

		datas = mysqlconn.mysql_conn(cmd1)


		return render_to_response('spend_list.html',{'datas':datas})





	return render_to_response('spend_list.html',{'datas':datas})
		

from django.shortcuts import render_to_response
from audit.models import Job_status_yz1,Job_total_yz1
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from tools import mysqlconn
import re
import time

	


def job_time_status(req):
        timelist = []
	userlist = Job_status_yz1.objects.values('jobuser').distinct()
        startTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        for i in range(24):
                time1 = startTime + ' ' + str(i)
                time2 = startTime + ' ' + str(i+1)
                cmd = 'select sum(computeTime) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s"' %(time1,time2)
                data1 = mysqlconn.mysql_conn(cmd)
                if data1[0][0]:
                        timelist.append(int(data1[0][0]))
		
		else:
			timelist.append(0)
		if 'beginTimeshow' in req.GET:
			timelist = []
			startTime = req.GET.get('beginTimeshow')
			st = re.split(" ",startTime)[0]
			for i in range(24):
				time1 = st + ' ' + str(i)
				time2 = st + ' ' + str(i+1)
				cmd = 'select sum(computeTime) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s"' %(time1,time2)
				data1 = mysqlconn.mysql_conn(cmd)
				if data1[0][0]:
					timelist.append(int(data1[0][0]))
				else:
					timelist.append(0)

        		return render_to_response('job_time1.html',{'userlist':userlist,'startTime':startTime,'timelist':timelist})


		if 'beginTimeshow_user' in req.GET:
			timelist_user = []
			if req.GET.has_key('search_user'):
				startTime = req.GET.get('beginTimeshow_user')
				jobuser = req.GET.get('user_name_graph')
				st = re.split(" ",startTime)[0]
				for i in range(24):
					time1 = st + ' ' + str(i)
					time2 = st + ' ' + str(i+1)
					cmd = 'select sum(computeTime) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s" and jobuser="%s"' %(time1,time2,jobuser)
					data1 = mysqlconn.mysql_conn(cmd)
					if data1[0][0]:
						timelist_user.append(int(data1[0][0]))
					else:
						timelist_user.append(0)
		

				return render_to_response('job_time1.html',{'userlist':userlist,'jobuser':jobuser,'st':st,'timelist_user':timelist_user})

	return render_to_response('job_time1.html',{'userlist':userlist,'startTime':startTime,'timelist':timelist})








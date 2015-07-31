from django.shortcuts import render_to_response
from audit.models import Job_status_yz1,Job_total_yz1
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from tools import mysqlconn
import re
import time




def job_status(req):
	maplist = []
        redlist = []
        suclist = []
        failist = []
	userlist = Job_status_yz1.objects.values('jobuser').distinct()
        startTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
#        now_time = '2015-05-11'
        for i in range(24):
                time1 = startTime + ' ' + str(i)
                time2 = startTime + ' ' + str(i+1)
                cmd = 'select sum(mapsTotal),sum(reducesTotal) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s"' %(time1,time2)
                data1 = mysqlconn.mysql_conn(cmd)
                if data1[0][0] or data1[0][1]:
                        maplist.append(int(data1[0][0]))
                        redlist.append(int(data1[0][1]))
		else:
			maplist.append(0)
			redlist.append(0)

                cmd = 'select sum(sucesscount),sum(failcount) from audit_job_total_yz1 where finishTime>="%s" and finishTime<"%s"' %(time1,time2)
                data2 = mysqlconn.mysql_conn(cmd)
                if data2[0][0] or data2[0][1]:
                        suclist.append(int(data2[0][0]))
                        failist.append(int(data2[0][1]))
		else:
			suclist.append(0)
			failist.append(0)

		if 'beginTimeshow' in req.GET:
			maplist = []
			redlist = []
			suclist = []
			failist = []
			startTime = req.GET.get('beginTimeshow')
			st = re.split(" ",startTime)[0]
			for i in range(24):
				time1 = st + ' ' + str(i)
				time2 = st + ' ' + str(i+1)
				cmd = 'select sum(mapsTotal),sum(reducesTotal) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s"' %(time1,time2)
				data1 = mysqlconn.mysql_conn(cmd)
				if data1[0][0] or data1[0][1]:
					maplist.append(int(data1[0][0]))
					redlist.append(int(data1[0][1]))
				else:
					maplist.append(0)
					redlist.append(0)
		
				cmd = 'select sum(sucesscount),sum(failcount) from audit_job_total_yz1 where finishTime>="%s" and finishTime<"%s"' %(time1,time2)
				data2 = mysqlconn.mysql_conn(cmd)
				if data2[0][0] or data2[0][1]:
					suclist.append(int(data2[0][0]))
					failist.append(int(data2[0][1]))
				else:
					suclist.append(0)
					failist.append(0)

        		return render_to_response('job_statistic1.html',{'userlist':userlist,'startTime':startTime,'maplist':maplist,'redlist':redlist,'suclist':suclist,'failist':failist})


		if 'beginTimeshow_user' in req.GET:
			maplist_user = []
			redlist_user = []
			suclist_user = []
			failist_user = []
			if req.GET.has_key('search_user'):
				startTime = req.GET.get('beginTimeshow_user')
				jobuser = req.GET.get('user_name_graph')
				st = re.split(" ",startTime)[0]
				for i in range(24):
					time1 = st + ' ' + str(i)
					time2 = st + ' ' + str(i+1)
					cmd = 'select sum(mapsTotal),sum(reducesTotal) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s" and jobuser="%s"' %(time1,time2,jobuser)
					data1 = mysqlconn.mysql_conn(cmd)
					if data1[0][0] or data1[0][1]:
						maplist_user.append(int(data1[0][0]))
						redlist_user.append(int(data1[0][1]))
					else:
						maplist_user.append(0)
						redlist_user.append(0)

					cmd = 'select sum(sucesscount),sum(failcount) from audit_job_total_yz1 where finishTime>="%s" and finishTime<"%s" and jobuser="%s"' %(time1,time2,jobuser)
					data2 = mysqlconn.mysql_conn(cmd)
					if data2[0][0] or data2[0][1]:
						suclist_user.append(int(data2[0][0]))
						failist_user.append(int(data2[0][1]))
		
					else:
						suclist_user.append(0)
						failist_user.append(0)

				return render_to_response('job_statistic1.html',{'userlist':userlist,'jobuser':jobuser,'st':st,'maplist_user':maplist_user,'redlist_user':redlist_user,'suclist_user':suclist_user,'failist_user':failist_user})

	return render_to_response('job_statistic1.html',{'userlist':userlist,'startTime':startTime,'maplist':maplist,'redlist':redlist,'suclist':suclist,'failist':failist})








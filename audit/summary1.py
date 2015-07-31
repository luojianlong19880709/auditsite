from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from tools import mysqlconn
import re
import time
	


def summary(req):
	usercount_list = []
	mapsTotal_list = []
	reducesTotal_list = []
	computeTime_list = []
	sucesscount_list = []
	failcount_list = []
	
        startTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        for i in range(24):
                time1 = startTime + ' ' + str(i)
                time2 = startTime + ' ' + str(i+1)
                cmd = 'select count(distinct jobuser),sum(mapsTotal),sum(reducesTotal),sum(computeTime)/60/60 from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s"' %(time1,time2)
                data1 = mysqlconn.mysql_conn(cmd)
                if data1[0][0] or data1[0][1] or data1[0][2] or data1[0][3]:
	                usercount_list.append(int(data1[0][0]))
			mapsTotal_list.append(int(data1[0][1]))
			reducesTotal_list.append(int(data1[0][2]))
			computeTime_list.append(int(data1[0][3]))
		else:
			usercount_list.append(0)
                        mapsTotal_list.append(0)
                        reducesTotal_list.append(0)
                        computeTime_list.append(0)

		cmd = 'select sum(sucesscount),sum(failcount) from audit_job_total_yz1 where finishTime>="%s" and finishTime<"%s"' %(time1,time2)

		data2 = mysqlconn.mysql_conn(cmd)
		if data2[0][0] or data2[0][1]:
			sucesscount_list.append(int(data2[0][0]))
			failcount_list.append(int(data2[0][1]))
		
		else:
			sucesscount_list.append(0)
                        failcount_list.append(0)
		
		



	return render_to_response('summary1.html',{'startTime':startTime,'usercount_list':usercount_list,'mapsTotal_list':mapsTotal_list,'reducesTotal_list':reducesTotal_list,'sucesscount_list':sucesscount_list,'failcount_list':failcount_list,'computeTime_list':computeTime_list,'data2':data2})





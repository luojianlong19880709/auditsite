from django.shortcuts import render_to_response
from audit.models import Job_status_yz,Job_total_yz
from django.http import HttpResponse,HttpResponseRedirect
import mysql.connector
import re
import datetime
import time
from tools import get_date,mysqlconn



def get_one_week_date():
	today = datetime.datetime.today()
	aWeekDelta = datetime.timedelta(weeks=1)
	aWeekAgo = today - aWeekDelta
	formated = '%d-%d-%d' % (aWeekAgo.year, aWeekAgo.month, aWeekAgo.day)


	return formated



def get_three_month_computeTime():
	now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
	three_month_ago = get_date.get_today_month(-3)
	cmd = 'select sum(computeTime) from audit_job_status_yz where finishTime>="%s" and finishTime<"%s"' %(three_month_ago,now_date)
	data = mysqlconn.mysql_conn(cmd)
	if data[0][0]:
		computeTime_three_month_ago = int(data[0][0])
	else:
		computeTime_three_month_ago = 0
        
 	return computeTime_three_month_ago


def get_three_month_computeTime1():
        now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        three_month_ago = get_date.get_today_month(-3)
        cmd = 'select sum(computeTime) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s"' %(three_month_ago,now_date)
        data = mysqlconn.mysql_conn(cmd)
        if data[0][0]:
		computeTime_three_month_ago1 = int(data[0][0])
	else:
		computeTime_three_month_ago1 = 0
	
	return computeTime_three_month_ago1



def get_one_week_computeTime():
	now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
	one_week_ago = get_one_week_date()
        cmd = 'select sum(computeTime) from audit_job_status_yz where finishTime>="%s" and finishTime<"%s"' %(one_week_ago,now_date)
	data = mysqlconn.mysql_conn(cmd)
        if data[0][0]:
                computeTime_one_week_ago = int(data[0][0])
	else:
		computeTime_one_week_ago = 0

        return computeTime_one_week_ago

def get_one_week_computeTime1():
        now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        one_week_ago = get_one_week_date()
        cmd = 'select sum(computeTime) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s"' %(one_week_ago,now_date)
        data = mysqlconn.mysql_conn(cmd)
        if data[0][0]:
                computeTime_one_week_ago1 = int(data[0][0])

	else:
		computeTime_one_week_ago1 = 0

        return computeTime_one_week_ago1



def get_three_month_job():
	now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
	three_month_ago = get_date.get_today_month(-3)
	cmd = 'select count(*) from audit_job_status_yz where finishTime>="%s" and finishTime<"%s"' %(three_month_ago,now_date)
	data = mysqlconn.mysql_conn(cmd)
	if data[0][0]:
		jobcount_three_month_ago = int(data[0][0])
	else:
		jobcount_three_month_ago = 0 
	
	return	jobcount_three_month_ago


def get_three_month_job1():
        now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        three_month_ago = get_date.get_today_month(-3)
        cmd = 'select count(*) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s"' %(three_month_ago,now_date)
        data = mysqlconn.mysql_conn(cmd)
        if data[0][0]:
                jobcount_three_month_ago1 = int(data[0][0])

	else:
		jobcount_three_month_ago1 = 0

        return  jobcount_three_month_ago1





def get_one_week_job():
	now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
	one_week_ago = get_one_week_date()
	cmd = 'select count(*) from audit_job_status_yz where finishTime>="%s" and finishTime<"%s"' %(one_week_ago,now_date)
	data = mysqlconn.mysql_conn(cmd)
	if data[0][0]:
                jobcount_one_week_ago = int(data[0][0])
	else:
		jobcount_one_week_ago = 0
        
        return  jobcount_one_week_ago



def get_one_week_job1():
        now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        one_week_ago = get_one_week_date()
        cmd = 'select count(*) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s"' %(one_week_ago,now_date)
        data = mysqlconn.mysql_conn(cmd)
        if data[0][0]:
                jobcount_one_week_ago1 = int(data[0][0])

	else:
		jobcount_one_week_ago1 = 0

        return  jobcount_one_week_ago1




def get_three_month_user():
	now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
	three_month_ago = get_date.get_today_month(-3)
	cmd = 'select count(distinct jobuser) from audit_job_status_yz where finishTime>="%s" and finishTime<"%s"' %(three_month_ago,now_date)
	data = mysqlconn.mysql_conn(cmd)
	if data[0][0]:
                usercount_three_month_ago = int(data[0][0])

	else:
		usercount_three_month_ago = 0

        return  usercount_three_month_ago


def get_three_month_user1():
        now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        three_month_ago = get_date.get_today_month(-3)
        cmd = 'select count(distinct jobuser) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s"' %(three_month_ago,now_date)
        data = mysqlconn.mysql_conn(cmd)
        if data[0][0]:
                usercount_three_month_ago1 = int(data[0][0])

	else:
		usercount_three_month_ago1 = 0

        return  usercount_three_month_ago1



def get_one_week_user():
	now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
	one_week_ago = get_one_week_date()
	cmd = 'select count(distinct jobuser) from audit_job_status_yz where finishTime>="%s" and finishTime<"%s"' %(one_week_ago,now_date)
	data = mysqlconn.mysql_conn(cmd)
        if data[0][0]:
                usercount_one_week_ago = int(data[0][0])

	else:
		usercount_one_week_ago = 0

        return  usercount_one_week_ago


def get_one_week_user1():
        now_date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        one_week_ago = get_one_week_date()
        cmd = 'select count(distinct jobuser) from audit_job_status_yz1 where finishTime>="%s" and finishTime<"%s"' %(one_week_ago,now_date)
        data = mysqlconn.mysql_conn(cmd)
        if data[0][0]:
                usercount_one_week_ago1 = int(data[0][0])

	else:
		usercount_one_week_ago1 = 0

        return  usercount_one_week_ago1



	
def total_status(req):
	computeTime_three_month_ago = get_three_month_computeTime()
	computeTime_three_month_ago_hou = computeTime_three_month_ago/60
	computeTime_three_month_ago_min = computeTime_three_month_ago - computeTime_three_month_ago_hou*60 	

	computeTime_avg_three_month_ago = computeTime_three_month_ago/90
	computeTime_avg_three_month_ago_hou = computeTime_avg_three_month_ago/60
	computeTime_avg_three_month_ago_min = computeTime_avg_three_month_ago - computeTime_avg_three_month_ago_hou*60

	computeTime_one_week_ago = get_one_week_computeTime()
	computeTime_one_week_ago_hou = computeTime_one_week_ago/60
	computeTime_one_week_ago_min = computeTime_one_week_ago - computeTime_one_week_ago_hou*60
	
	computeTime_avg_one_week_ago = computeTime_one_week_ago/7
	computeTime_avg_one_week_ago_hou = computeTime_avg_one_week_ago/60
	computeTime_avg_one_week_ago_min = computeTime_avg_one_week_ago - computeTime_avg_one_week_ago_hou*60

	jobcount_three_month_ago = get_three_month_job()
	jobcount_avg_three_month_ago = jobcount_three_month_ago/90
	
	jobcount_one_week_ago = get_one_week_job()
	jobcount_avg_one_week_ago = jobcount_one_week_ago/7

	usercount_three_month_ago = get_three_month_user()
	usercount_avg_three_month_ago = usercount_three_month_ago/90
	
	usercount_one_week_ago = get_one_week_user()
	usercount_avg_one_week_ago = usercount_one_week_ago/7


	computeTime_three_month_ago1 = get_three_month_computeTime1()
        computeTime_three_month_ago_hou1 = computeTime_three_month_ago1/60
        computeTime_three_month_ago_min1 = computeTime_three_month_ago1 - computeTime_three_month_ago_hou1*60

        computeTime_avg_three_month_ago1 = computeTime_three_month_ago1/90
        computeTime_avg_three_month_ago_hou1 = computeTime_avg_three_month_ago1/60
        computeTime_avg_three_month_ago_min1 = computeTime_avg_three_month_ago1 - computeTime_avg_three_month_ago_hou1*60

        computeTime_one_week_ago1 = get_one_week_computeTime1()
        computeTime_one_week_ago_hou1 = computeTime_one_week_ago1/60
        computeTime_one_week_ago_min1 = computeTime_one_week_ago1 - computeTime_one_week_ago_hou1*60

        computeTime_avg_one_week_ago1 = computeTime_one_week_ago1/7
        computeTime_avg_one_week_ago_hou1 = computeTime_avg_one_week_ago1/60
        computeTime_avg_one_week_ago_min1 = computeTime_avg_one_week_ago1 - computeTime_avg_one_week_ago_hou1*60

        jobcount_three_month_ago1 = get_three_month_job1()
        jobcount_avg_three_month_ago1 = jobcount_three_month_ago1/90

        jobcount_one_week_ago1 = get_one_week_job1()
        jobcount_avg_one_week_ago1 = jobcount_one_week_ago1/7

        usercount_three_month_ago1 = get_three_month_user1()
        usercount_avg_three_month_ago1 = usercount_three_month_ago1/90

        usercount_one_week_ago1 = get_one_week_user1()
        usercount_avg_one_week_ago1 = usercount_one_week_ago1/7
	
	
	return render_to_response('welcome.html',{'computeTime_three_month_ago_hou':computeTime_three_month_ago_hou,'computeTime_three_month_ago_min':computeTime_three_month_ago_min,'computeTime_avg_three_month_ago_hou':computeTime_avg_three_month_ago_hou,'computeTime_avg_three_month_ago_min':computeTime_avg_three_month_ago_min,'computeTime_one_week_ago_hou':computeTime_one_week_ago_hou,'computeTime_one_week_ago_min':computeTime_one_week_ago_min,'computeTime_avg_one_week_ago_hou':computeTime_avg_one_week_ago_hou,'computeTime_avg_one_week_ago_min':computeTime_avg_one_week_ago_min,'jobcount_three_month_ago':jobcount_three_month_ago,'jobcount_avg_three_month_ago':jobcount_avg_three_month_ago,'jobcount_one_week_ago':jobcount_one_week_ago,'jobcount_avg_one_week_ago':jobcount_avg_one_week_ago,'usercount_three_month_ago':usercount_three_month_ago,'usercount_avg_three_month_ago':usercount_avg_three_month_ago,'usercount_one_week_ago':usercount_one_week_ago,'usercount_avg_one_week_ago':usercount_avg_one_week_ago,'computeTime_three_month_ago_hou1':computeTime_three_month_ago_hou1,'computeTime_three_month_ago_min1':computeTime_three_month_ago_min1,'computeTime_avg_three_month_ago_hou1':computeTime_avg_three_month_ago_hou1,'computeTime_avg_three_month_ago_min1':computeTime_avg_three_month_ago_min1,'computeTime_one_week_ago_hou1':computeTime_one_week_ago_hou1,'computeTime_avg_one_week_ago_hou1':computeTime_avg_one_week_ago_hou1,'computeTime_avg_one_week_ago_min1':computeTime_avg_one_week_ago_min1,'jobcount_three_month_ago1':jobcount_three_month_ago1,'jobcount_avg_three_month_ago1':jobcount_avg_three_month_ago1,'jobcount_one_week_ago1':jobcount_one_week_ago1,'jobcount_avg_one_week_ago1':jobcount_avg_one_week_ago1,'usercount_three_month_ago1':usercount_three_month_ago1,'usercount_avg_three_month_ago1':usercount_avg_three_month_ago1,'usercount_one_week_ago1':usercount_one_week_ago1,'usercount_avg_one_week_ago1':usercount_avg_one_week_ago1})








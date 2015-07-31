from django.shortcuts import render_to_response
from audit.models import Performance1
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from tools import mysqlconn
import re
import time
	


def performance(req):
	eth_in_list = []
        eth_out_list = []
        bytes_in_list = []
        bytes_out_list = []
	load_five_list = []
	cpu_user_list = []
	cpu_system_list = []
	
        startTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        for i in range(24):
                time1 = startTime + ' ' + str(i)
                time2 = startTime + ' ' + str(i+1)
                cmd = 'select avg(eth_in),avg(eth_out),avg(bytes_in),avg(bytes_out),avg(load_five),avg(cpu_user),avg(cpu_system) from audit_performance1 where collect_time >= (UNIX_TIMESTAMP("%s"))*1000 and collect_time < (UNIX_TIMESTAMP("%s"))*1000' %(time1,time2)
                data1 = mysqlconn.mysql_conn(cmd)
                if data1[0][0] or data1[0][1] or data1[0][2] or data1[0][3] or data1[0][4] or data1[0][5] or data1[0][6]:
	                eth_in_list.append(int(data1[0][0]))
	                eth_out_list.append(int(data1[0][1]))
		        bytes_in_list.append(int(data1[0][2]))
		        bytes_out_list.append(int(data1[0][3]))
			load_five_list.append(int(data1[0][4]))
			cpu_user_list.append(int(data1[0][5]))
			cpu_system_list.append(int(data1[0][6]))

		else:
			eth_in_list.append(0)
                        eth_out_list.append(0)
                        bytes_in_list.append(0)
                        bytes_out_list.append(0)
                        load_five_list.append(0)
                        cpu_user_list.append(0)
                        cpu_system_list.append(0)
		

		if 'beginTimeshow' in req.GET:
			eth_in_list = []
        		eth_out_list = []
        		bytes_in_list = []
        		bytes_out_list = []
        		load_five_list = []
        		cpu_user_list = []
        		cpu_system_list = []
			startTime = req.GET.get('beginTimeshow')
			st = re.split(" ",startTime)[0]
			for i in range(24):
				time1 = st + ' ' + str(i)
				time2 = st + ' ' + str(i+1)
				cmd = 'select sum(eth_in),sum(eth_out),sum(bytes_in),sum(bytes_out),sum(load_five),sum(cpu_user),sum(cpu_system) from audit_performance1 where collect_time >= (UNIX_TIMESTAMP("%s"))*1000 and collect_time < (UNIX_TIMESTAMP("%s"))*1000' %(time1,time2)
				data1 = mysqlconn.mysql_conn(cmd)
				if data1[0][0] or data1[0][1] or data1[0][2] or data1[0][3] or data1[0][4] or data1[0][5] or data1[0][6]:
					eth_in_list.append(int(data1[0][0]))
                        		eth_out_list.append(int(data1[0][1]))
                        		bytes_in_list.append(int(data1[0][2]))
                        		bytes_out_list.append(int(data1[0][3]))
                        		load_five_list.append(int(data1[0][4]))
                        		cpu_user_list.append(int(data1[0][5]))
                        		cpu_system_list.append(int(data1[0][6]))
				else:
					eth_in_list.append(0)
               				eth_out_list.append(0)
                        		bytes_in_list.append(0)
                        		bytes_out_list.append(0)
                        		load_five_list.append(0)
                        		cpu_user_list.append(0)
                        		cpu_system_list.append(0)
		

	       		return render_to_response('performance1.html',{'startTime':startTime,'eth_in_list':eth_in_list,'eth_out_list':eth_out_list,'bytes_in_list':bytes_in_list,'bytes_out_list':bytes_out_list,'load_five_list':load_five_list,'cpu_user_list':cpu_user_list,'cpu_system_list':cpu_system_list}) 


	return render_to_response('performance1.html',{'startTime':startTime,'eth_in_list':eth_in_list,'eth_out_list':eth_out_list,'bytes_in_list':bytes_in_list,'bytes_out_list':bytes_out_list,'load_five_list':load_five_list,'cpu_user_list':cpu_user_list,'cpu_system_list':cpu_system_list})





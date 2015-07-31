from django.shortcuts import render_to_response
from audit.models import Publisher,Total
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
import time
import re
import MySQLdb
import mysql.connector


username_errors = {
    'required': 'please input username',
    'invalid': 'Enter a valid value'
}
 


year_errors = {
    'required': 'please input years',
    'invalid': 'Enter a valid value'
}

month_errors = {
    'required': 'please input month',
    'invalid': 'Enter a valid value'
}

day_errors = {
    'required': 'please input days',
    'invalid': 'Enter a valid value'
}

dir_errors = {
    'required': 'please input dircount',
    'invalid': 'Enter a valid value'
}

class UserForm(forms.Form):

	conn = mysql.connector.connect(user='zabbix', db='audit', passwd='zabbixadmin', host='10.4.16.227', charset='utf8')
        cur=conn.cursor()
        cmd = 'select owner,owner from audit_total order by totalsize desc limit 20'
        cur.execute(cmd)
        userlist=cur.fetchall()
	user_tuple = tuple(userlist)
	

#	username = forms.CharField(error_messages=username_errors)
#	date = forms.CharField(error_messages=date_errors)
#	dircount = forms.CharField(error_messages=dir_errors)


	dircount = forms.ChoiceField(choices=((2,2),(3,3),(4,4),(5,5)),error_messages=dir_errors)
	username = forms.ChoiceField(choices=user_tuple,error_messages=username_errors)
	
	cmd = 'select year,year2 from tb_admin'
	cur.execute(cmd)
	year_list = cur.fetchall()
	year_tuple =  tuple(year_list) 
	year = forms.ChoiceField(choices=year_tuple,error_messages=year_errors)

	cmd = 'select month,month2 from tb_admin1'
	cur.execute(cmd)
	month_list = cur.fetchall()
        month_tuple =  tuple(month_list)
        month = forms.ChoiceField(choices=month_tuple,error_messages=month_errors)
	

	cmd = 'select day,day2 from tb_admin2'
        cur.execute(cmd)
        day_list = cur.fetchall()
        day_tuple =  tuple(day_list)
        day = forms.ChoiceField(choices=day_tuple,error_messages=day_errors)
	
	conn.close()
	

class GraphForm(forms.Form):
	date = forms.CharField()


	
	


def search(req):
	if req.method == 'POST':
		form = UserForm(req.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
#                	time = form.cleaned_data['date']
			year = form.cleaned_data['year']
			day =  form.cleaned_data['day']
			month = form.cleaned_data['month']
			time = str(year)+'-'+ month + '-' + day
                	dircount = form.cleaned_data['dircount']
			
                	IsYear = re.search("-",time)
			if req.POST.has_key('datasearch'):
				if IsYear:		
					datas = Publisher.objects.filter(dircount=dircount).filter(m_year__lt=time).filter(owner=username).order_by('m_year')[0:100]
					return render_to_response('datainfo.html', {'datas': datas})
				else:
					start_time = form.cleaned_data['date']+'-01-01'
					end_time = form.cleaned_data['date']+'-12-31'
				
					datas = Publisher.objects.filter(dircount=dircount).filter(m_year__range=(start_time,end_time)).filter(owner=username).order_by('m_year')[0:100]
					return render_to_response('datainfo.html', {'datas': datas})

			if req.POST.has_key('filesize'):
                                if IsYear:
                                        datas = Publisher.objects.filter(dircount=dircount).filter(m_year__lt=time).filter(owner=username).order_by('-size')[0:100]
                                        return render_to_response('datainfo.html', {'datas': datas})
                                else:
                                        start_time = form.cleaned_data['date']+'-01-01'
                                        end_time = form.cleaned_data['date']+'-12-31'

                                        datas = Publisher.objects.filter(dircount=dircount).filter(m_year__range=(start_time,end_time)).filter(owner=username).order_by('-size')[0:100]
                                        return render_to_response('datainfo.html', {'datas': datas})


	else:
		form = UserForm()
	return render_to_response('datainfo.html',{'form':form})


def graph(req):
	conn = mysql.connector.connect(user='root', db='audit', passwd='', host='localhost', charset='utf8')
	cur=conn.cursor()
	cmd = 'select owner,totalsize from audit_total order by totalsize desc limit 10'
	cur.execute(cmd)
	result=cur.fetchall()
	d = {}
	for i in result:
		d[i[0].encode('utf8')] = i[1]
	categories = d.keys()
	data = d.values()
	if req.method == 'POST':
		form = GraphForm(req.POST)
		if form.is_valid():
			searchdate = form.cleaned_data['date']
			d2 = {}
			for username in categories:
				cmd = 'select owner,sum(size) from audit_publisher where owner="%s" and m_year<"%s"' %(username,searchdate)
				cur.execute(cmd)
				result2 = cur.fetchall()
				for A in result2:
					d2[A[0].encode('utf8')] = int(A[1])
				
			categories_date = d2.keys()
			data_date = d2.values()	
			return render_to_response('graph.html',{'user':req.user,'categories':categories,'data':data,'categories_date':categories_date,'data_date':data_date,'searchdate':searchdate})

	else:
		form = GraphForm()
	conn.commit()
	cur.close()
	conn.close()
	return render_to_response('graph.html',{'user':req.user,'categories':categories,'data':data,'form':form})
	



def graph_search(req,user,date,aaa):

	if aaa == 'sortbysize':
		datas = Publisher.objects.filter(m_year__lt=date).filter(owner=user).order_by('-size')[0:100]
	
		return render_to_response('datainfo2.html',{'datas':datas})
	else:
		datas = Publisher.objects.filter(m_year__lt=date).filter(owner=user).order_by('m_year')[0:100]

		return render_to_response('datainfo2.html',{'datas':datas})


def login(req):
	datas='222'
	return render_to_response('login.html',{'datas':datas})






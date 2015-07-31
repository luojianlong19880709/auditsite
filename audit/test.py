from django.shortcuts import render_to_response
from audit.models import Job_status_yz,Job_total_yz
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
import time
import re
import time
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage,InvalidPage


	

def test(req):
#	datas = Job_status_yz.objects.all()
	return render_to_response('test.html',{})

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


#import MySQLdb
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auditsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^audit/index/$', 'audit.views.data_list'),
    url(r'^audit/search/$', 'audit.views.search'),
#    url(r'^audit/hadoop/index/$', 'audit.hadoop.index'),
    url(r'^$', 'audit.hadoop.index'),
    url(r'^audit/hadoop/user_status/$', 'audit.job_total.user_status'),
    url(r'^audit/hadoop/user_status1/$', 'audit.job_total1.user_status'),
    url(r'^audit/graph/$', 'audit.views.graph'),
#    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    url(r'^audit/graph_search/(.+)/(.+)/(.+)/$', 'audit.views.graph_search'),
    url(r'^audit/hadoop/job_status/$', 'audit.job_status.job_status'),
    url(r'^audit/hadoop/job_status1/$', 'audit.job_status1.job_status'),
    url(r'^audit/hadoop/job_time_status/$', 'audit.job_time.job_time_status'),
    url(r'^audit/hadoop/job_time_status1/$', 'audit.job_time1.job_time_status'),
    url(r'^audit/hadoop/welcome/$', 'audit.welcome.total_status'),
    url(r'^audit/hadoop/user_list/$', 'audit.user_list.user_list'),
    url(r'^audit/hadoop/user_list1/$', 'audit.user_list1.user_list'),
    url(r'^audit/hadoop/user_reg/$', 'audit.user_list.user_reg'),
    url(r'^audit/hadoop/user_reg1/$', 'audit.user_list1.user_reg'),
    url(r'^audit/hadoop/user_del/(.+)/$', 'audit.user_list.user_del'),
    url(r'^audit/hadoop/user_del1/(.+)/$', 'audit.user_list1.user_del'),
    url(r'^audit/hadoop/user_update/(.+)/$', 'audit.user_list.user_update'),
    url(r'^audit/hadoop/user_update1/(.+)/$', 'audit.user_list1.user_update'),
    url(r'^audit/hadoop/user_info/(.+)/$', 'audit.user_list.user_info'),
    url(r'^audit/hadoop/user_info1/(.+)/$', 'audit.user_list1.user_info'),
    url(r'^audit/hadoop/report_list/$', 'audit.report_list.report_list'),
    url(r'^audit/hadoop/report_list1/$', 'audit.report_list1.report_list'),
    url(r'^audit/hadoop/spend_list/$', 'audit.spend_list.spend_list'),
    url(r'^audit/hadoop/spend_list1/$', 'audit.spend_list1.spend_list'),
    url(r'^audit/hadoop/department_list/$', 'audit.department_list.department_list'),
    url(r'^audit/hadoop/department_list1/$', 'audit.department_list1.department_list'),
    url(r'^audit/hadoop/department_reg/$', 'audit.department_list.department_reg'),
    url(r'^audit/hadoop/department_reg1/$', 'audit.department_list1.department_reg'),
    url(r'^audit/hadoop/department_del/(.+)/$', 'audit.department_list.department_del'),
    url(r'^audit/hadoop/department_del1/(.+)/$', 'audit.department_list1.department_del'),
    url(r'^audit/hadoop/department_update/(.+)/$', 'audit.department_list.department_update'),
    url(r'^audit/hadoop/department_update1/(.+)/$', 'audit.department_list1.department_update'),
    url(r'^audit/hadoop/department_info/(.+)/$', 'audit.department_list.department_info'),
    url(r'^audit/hadoop/department_info1/(.+)/$', 'audit.department_list1.department_info'),
    url(r'^audit/hadoop/performance/$', 'audit.performance.performance'),
    url(r'^audit/hadoop/performance1/$', 'audit.performance1.performance'),
    url(r'^audit/hadoop/summary/$', 'audit.summary.summary'),
    url(r'^audit/hadoop/summary1/$', 'audit.summary1.summary'),
    url(r'^audit/hadoop/test/$', 'audit.test.test'),
)

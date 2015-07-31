from django.db import models

class Publisher(models.Model):
	owner = models.CharField(max_length=300)
	size = models.CharField(max_length=300)
	m_year = models.DateTimeField()
	path = models.CharField(max_length=300)
	dircount = models.CharField(max_length=300)
	def __unicode__(self):
        	return self.name


class Total(models.Model):
	owner = models.CharField(max_length=300)
	totalsize = models.CharField(max_length=300)
	def __unicode__(self):
		return self.name

class Job_status_yz(models.Model):
	startTime = models.DateTimeField()
	finishTime = models.DateTimeField()
	submitTime = models.DateTimeField()
	computeTime = models.CharField(max_length=300)
	jobname = models.CharField(max_length=300)
	jobuser = models.CharField(max_length=300)
	jobid = models.CharField(max_length=300)
	jobstate = models.CharField(max_length=300)
	mapsTotal = models.CharField(max_length=300)
	mapsCompleted = models.CharField(max_length=300)
	reducesTotal = models.CharField(max_length=300)
	reducesCompleted = models.CharField(max_length=300)
	failedReduceAttempts = models.CharField(max_length=300)
	killedReduceAttempts = models.CharField(max_length=300)
	failedMapAttempts = models.CharField(max_length=300)
	killedMapAttempts = models.CharField(max_length=300)
	cpu_cost_time = models.CharField(max_length=300)
	def __unicode__(self):
		return self.name

class Job_total_yz(models.Model):
	startTime = models.DateTimeField()
	finishTime = models.DateTimeField()
	submitTime = models.DateTimeField()
	computeTime = models.CharField(max_length=300)
	jobname = models.CharField(max_length=300)
	jobuser = models.CharField(max_length=300)
	jobid = models.CharField(max_length=300)
	sucesscount = models.CharField(max_length=300)
	failcount = models.CharField(max_length=300)
	killcount = models.CharField(max_length=300)
	def __unicode__(self):
		return self.name

class Job_status_yz1(models.Model):
        startTime = models.DateTimeField()
        finishTime = models.DateTimeField()
	submitTime = models.DateTimeField()
        computeTime = models.CharField(max_length=300)
        jobname = models.CharField(max_length=300)
        jobuser = models.CharField(max_length=300)
        jobid = models.CharField(max_length=300)
        jobstate = models.CharField(max_length=300)
        mapsTotal = models.CharField(max_length=300)
        mapsCompleted = models.CharField(max_length=300)
        reducesTotal = models.CharField(max_length=300)
        reducesCompleted = models.CharField(max_length=300)
        failedReduceAttempts = models.CharField(max_length=300)
        killedReduceAttempts = models.CharField(max_length=300)
        failedMapAttempts = models.CharField(max_length=300)
        killedMapAttempts = models.CharField(max_length=300)
	cpu_cost_time = models.CharField(max_length=300)
        def __unicode__(self):
                return self.name

class Job_total_yz1(models.Model):
        startTime = models.DateTimeField()
        finishTime = models.DateTimeField()
	submitTime = models.DateTimeField()
        computeTime = models.CharField(max_length=300)
        jobname = models.CharField(max_length=300)
        jobuser = models.CharField(max_length=300)
        jobid = models.CharField(max_length=300)
        sucesscount = models.CharField(max_length=300)
        failcount = models.CharField(max_length=300)
        killcount = models.CharField(max_length=300)
        def __unicode__(self):
                return self.name



class User(models.Model):
	user_name = models.CharField(max_length=300)
	applicant = models.CharField(max_length=300)
	department = models.CharField(max_length=300)
	leader = models.CharField(max_length=300)
	apply_date = models.DateTimeField()
	mobile_phone = models.CharField(max_length=300)
	tel_number = models.CharField(max_length=300)
	email = models.CharField(max_length=300)
	storage = models.CharField(max_length=300)
	storage_per_month =  models.CharField(max_length=300)
	access_business_range = models.CharField(max_length=300)
	description = models.CharField(max_length=300)
	hadoop_client_ip = models.CharField(max_length=300)
	def __unicode__(self):
                return self.name


class User1(models.Model):
        user_name = models.CharField(max_length=300)
        applicant = models.CharField(max_length=300)
        department = models.CharField(max_length=300)
        leader = models.CharField(max_length=300)
        apply_date = models.DateTimeField()
        mobile_phone = models.CharField(max_length=300)
        tel_number = models.CharField(max_length=300)
        email = models.CharField(max_length=300)
        storage = models.CharField(max_length=300)
        storage_per_month =  models.CharField(max_length=300)
        access_business_range = models.CharField(max_length=300)
        description = models.CharField(max_length=300)
	hadoop_client_ip = models.CharField(max_length=300)
	def __unicode__(self):
                return self.name



class Depart_report(models.Model):
	user_count = models.CharField(max_length=300)
	job_count = models.CharField(max_length=300)
	map_count = models.CharField(max_length=300)
	reduce_count = models.CharField(max_length=300)
	date = models.CharField(max_length=300)
	department = models.CharField(max_length=300)
	cpu_cost_time = models.CharField(max_length=300)
	total_time = models.CharField(max_length=300)	
	def __unicode__(self):
                return self.name



class Depart_report1(models.Model):
        user_count = models.CharField(max_length=300)
        job_count = models.CharField(max_length=300)
        map_count = models.CharField(max_length=300)
        reduce_count = models.CharField(max_length=300)
        date = models.CharField(max_length=300)
        department = models.CharField(max_length=300)
        cpu_cost_time = models.CharField(max_length=300)
        total_time = models.CharField(max_length=300)
	def __unicode__(self):
                return self.name



class Detail_report(models.Model):
	user_count = models.CharField(max_length=300)
	job_count = models.CharField(max_length=300)
	job_success_count = models.CharField(max_length=300)
	job_failed_count = models.CharField(max_length=300)
	map_success_count = models.CharField(max_length=300)
	map_failed_count = models.CharField(max_length=300)
	map_killed_count = models.CharField(max_length=300)
	reduce_success_count = models.CharField(max_length=300)
	reduce_failed_count = models.CharField(max_length=300)
	reduce_killed_count = models.CharField(max_length=300)
	total_time = models.CharField(max_length=300)
	date = models.CharField(max_length=300)
	department = models.CharField(max_length=300)
	cpu_cost_time = models.CharField(max_length=300)
	def __unicode__(self):
                return self.name




class Detail_report1(models.Model):
        user_count = models.CharField(max_length=300)
        job_count = models.CharField(max_length=300)
        job_success_count = models.CharField(max_length=300)
        job_failed_count = models.CharField(max_length=300)
        map_success_count = models.CharField(max_length=300)
        map_failed_count = models.CharField(max_length=300)
        map_killed_count = models.CharField(max_length=300)
        reduce_success_count = models.CharField(max_length=300)
        reduce_failed_count = models.CharField(max_length=300)
        reduce_killed_count = models.CharField(max_length=300)
        total_time = models.CharField(max_length=300)
        date = models.CharField(max_length=300)
        department = models.CharField(max_length=300)
        cpu_cost_time = models.CharField(max_length=300)
	def __unicode__(self):
                return self.name


class Department(models.Model):
	department = models.CharField(max_length=300)
	leader = models.CharField(max_length=300)
	depart_mail = models.CharField(max_length=300)
	leader_mobile = models.CharField(max_length=300)
	leader_mail = models.CharField(max_length=300)
	def __unicode__(self):
                return self.name






class Department1(models.Model):
        department = models.CharField(max_length=300)
        leader = models.CharField(max_length=300)
        depart_mail = models.CharField(max_length=300)
        leader_mobile = models.CharField(max_length=300)
        leader_mail = models.CharField(max_length=300)
        def __unicode__(self):
                return self.name



class Performance(models.Model):
	eth_in = models.CharField(max_length=300)
	eth_out = models.CharField(max_length=300)
	bytes_in = models.CharField(max_length=300)
	bytes_out = models.CharField(max_length=300)
	load_five = models.CharField(max_length=300)
	cpu_user = models.CharField(max_length=300)
	cpu_system = models.CharField(max_length=300)
	collect_time = models.CharField(max_length=300)
	def __unicode__(self):
                return self.name




class Performance1(models.Model):
        eth_in = models.CharField(max_length=300)
        eth_out = models.CharField(max_length=300)
        bytes_in = models.CharField(max_length=300)
        bytes_out = models.CharField(max_length=300)
        load_five = models.CharField(max_length=300)
        cpu_user = models.CharField(max_length=300)
        cpu_system = models.CharField(max_length=300)
        collect_time = models.CharField(max_length=300)
        def __unicode__(self):
                return self.name


				











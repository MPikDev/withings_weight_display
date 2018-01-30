from django.db import models

class User(models.Model):
	email = models.CharField(max_length=200)
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	password = models.CharField(max_length=32)


	def __unicode__(self):  
		# string = 'email: %s first_name: %s' % (self.email, self.first_name)
   		# return string
   		return 'email: %s first_name: %s' % (self.email, self.first_name)



class DataAccount(models.Model):
	email = models.ForeignKey(User)
	data_account = models.CharField(max_length=200)
	data_login = models.CharField(max_length=200)
	data_password = models.CharField(max_length=200)

	def __unicode__(self):
		# string = 'data_account: %s data_login: %s' % (self.data_account, self.data_login)
		# return string  
		return 'data_account: %s data_login: %s' % (self.data_account, self.data_login)



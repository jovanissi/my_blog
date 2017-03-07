from django.db import models
from datetime import datetime

class headlines(models.Model):
	article_img = models.FileField(upload_to='uploads/images', default='null')
	title = models.CharField(max_length=110)
	body = models.TextField(blank=True)
	pub_date = models.DateTimeField(default=datetime.now, blank=True)
	Tech = 'Tech'
	Science = 'Science'
	Social = 'Social'
	classification_choices ={
	(Tech, 'Tech'),
	(Science, 'Science'),
	(Social, 'Social'),
	}
	classifications = models.CharField(max_length=200, choices=classification_choices, default="Tech")
	number_comments = models.IntegerField(default=0)
	number_view = models.IntegerField(default=0)
	author_name = models.CharField(max_length=100, blank=True)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)

	def __str__(self):
		return self.title

	def __str__(self):
		return self.classifications

class user_comment(models.Model):
	user_name = models.CharField(max_length=50, blank=False)
	comment = models.TextField(blank=False)
	comment_date = models.DateTimeField(auto_now_add=True)
	reference = models.IntegerField(default=0)
	
	def __str__(self):
		return self.user_name
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AboutMe(models.Model):

	position = models.CharField(max_length=128, default="Full Stack Web Developer")
	text = models.TextField()



	class Meta:
		verbose_name_plural='About Me'

	def __str__(self):
		return 'About Me'

class SocialLink(models.Model):

	url = models.URLField(blank=True)
	fa_class = models.CharField(max_length=24)

	def __str__(self):
		text = self.fa_class.split('-')[1]
		return text


class SkillCategory(models.Model):

	text = models.CharField(max_length=128)

	def __str__(self):
		return self.text

	class Meta:
		verbose_name_plural='Skill Categories'

class Skill(models.Model):

	category = models.ForeignKey(SkillCategory)
	text = models.CharField(max_length=128)

	def __str__(self):
		return self.text

class PortfolioApp(models.Model):

	title = models.CharField(max_length=128)
	modal_target = models.CharField(max_length=128)
	description = models.TextField()
	description2 = models.TextField(blank=True)
	modal_img_url = models.URLField(blank=True)
	img_url = models.URLField()
	app_url = models.URLField()
	app_url_text = models.CharField(max_length=128, default="View Application")
	rank = models.PositiveSmallIntegerField()

	class Meta:
		ordering = ('rank',)

	def __str__(self):
		return self.title

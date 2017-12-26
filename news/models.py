from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Column(models.Model):
	name = models.CharField('Column Name', max_length=256)
	slug = models.CharField('Column Site', max_length=256, db_index=True)
	intro = models.CharField('Column Intro', default='', max_length=256)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Column'
		verbose_name_plural = 'Column'
		ordering = ['name'] #order by which column

@python_2_unicode_compatible
class Article(models.Model):
	column = models.ManyToManyField(Column,verbose_name='Column')

	title = models.CharField('Title',max_length=256)
	slug = models.CharField('Site', max_length=256, db_index=True)
	author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='Author')
	content = models.TextField('Content',default='',blank=True)
	published = models.BooleanField('Published', default=True)

	pub_date = models.DateTimeField('Publish Date', auto_now_add=True, editable=True)
	update_date = models.DateTimeField('Update Date', auto_now_add=True, null=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Article'

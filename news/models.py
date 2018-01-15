# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from markdown import markdown
from markdownx.models import MarkdownxField
from markdownx.widgets import AdminMarkdownxWidget
import datetime
# Create your models here.



@python_2_unicode_compatible
class Column(models.Model):
	name = models.CharField('Column Name', max_length=256)
	slug = models.CharField('Column Site', max_length=256, unique=True)
	intro = models.CharField('Column Intro', default='', max_length=256)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('column',args=(self.slug,))
		#注意 args 参数为元组，写 args=(self.slug) 这样是错的，注意后面有一个逗号 args=(self.slug,)

	class Meta:
		verbose_name = 'Column'
		verbose_name_plural = 'Column'
		ordering = ['name'] #order by which column

@python_2_unicode_compatible
class Article(models.Model):
	column = models.ManyToManyField(Column,verbose_name='Column')

	title = models.CharField('Title',max_length=256)
	slug = models.CharField('Site', max_length=256, unique=True)
	author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='Author')
	content = MarkdownxField()

	published = models.BooleanField('Published', default=True)

	pub_date = models.DateTimeField('Publish Date', auto_now_add=True, editable=True)
	update_date = models.DateTimeField('Update Date', auto_now_add=True, null=True)

	def __str__(self):
		return self.title

	def get_content(self):
		return markdown(self.content)

	def get_absolute_url(self):
		return reverse('article',args=(self.pk,self.slug,))#add pk to avoid multiple returned values

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Article'

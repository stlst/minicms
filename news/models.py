from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from markdown import markdown
from markdownx.models import MarkdownxField
from markdownx.widgets import AdminMarkdownxWidget
import datetime
import uuid
# Create your models here.



@python_2_unicode_compatible
class Column(models.Model):
	name = models.CharField('Column Name', max_length=256)
	slug = models.CharField('Column Site', max_length=256, unique=True)
	intro = models.CharField('Column Intro', default='', max_length=256)

	def __str__(self):
		return self.name

	def get_column_count(self,keyword):
		try:
			c=Column.objects.get(slug=keyword)
		except Exception as e:
			raise e
		len_a = c.article_set.all()
		return len_a

	def get_absolute_url(self):
		return reverse('column',args=(self.slug,))
		#attention that args is a tuple, it is wrong to use ` args=(self.slug) `, there is a ',' behind.

	class Meta:
		verbose_name = 'Column'
		verbose_name_plural = 'Column'
		ordering = ['name'] #order by which column

@python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField('Title',max_length=256)
	slug = models.SlugField('Site', max_length=256,unique=True)
	column = models.ForeignKey(Column,verbose_name='Column')
	author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='Author')
	content = MarkdownxField()
	description = models.CharField('Article description', default='This is the description for article.', max_length=256)
	published = models.BooleanField('Published', default=True)

	pub_date = models.DateTimeField('Publish Date', auto_now_add=True, editable=True)
	update_date = models.DateTimeField('Update Date', auto_now_add=True, null=True)

	def get_column_slug(self):
		return self.column.slug

	def __str__(self):
		return self.title

	def get_content(self):
		return markdown(self.content)

	def get_absolute_url(self):
		return reverse('article',args=(self.pk,self.slug,))#add pk to avoid multiple returned values

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Article'

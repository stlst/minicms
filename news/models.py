from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from markdown import markdown
import bleach
from markdownx.models import MarkdownxField
from markdownx.widgets import AdminMarkdownxWidget
import datetime
import uuid
from bs4 import BeautifulSoup
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
	published = models.BooleanField('Published', default=True)
	pub_date = models.DateTimeField('Publish Date', auto_now_add=True, editable=True)
	update_date = models.DateTimeField('Update Date', auto_now_add=True, null=True)
	html_body=models.TextField('Html',default='This is html_body')
	description = models.TextField('Article description', default='This is the description for article.', max_length=256)
	def get_column_slug(self):
		return self.column.slug
	def __str__(self):
		return self.title
	def get_content(self):
		return markdown(self.content)
	def get_absolute_url(self):
		return reverse('article',args=(self.pk,self.slug,))#add pk to avoid multiple returned values
	def save(self,*args,**kwargs):
		self.html_body=markdown(self.content,output_format='html')
		soup=BeautifulSoup(self.html_body,"html5lib")
		self.html_body=soup.get_text()
		if len(self.html_body) >= 255:
			self.description=self.html_body[:255]
		else:
			self.description=self.html_body
		super(Article, self).save(*args,**kwargs)
	#@staticmethod
	#def on_body_change(self,value,oldvalue,initiator):  
	#	allowed_tags=['a','ul','strong','p','h1','h2','h3']  
	#	html_body=markdown(value,output_format='html')  
	#	html_body=bleach.clean(html_body,tags=allowed_tags,strip=True)  
	#	html_body=bleach.linkify(html_body)
	#	self.html_body=html_body  
	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Article'


  
#models.event.listen(Article.content,'set',Article.on_body_change)  





















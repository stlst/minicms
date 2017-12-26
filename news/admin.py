from django.contrib import admin

# Register your models here.
from .models import Column, Article

class ColumnAdmin(admin.ModelAdmin):
	list_display = ('name','slug','intro')

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','slug','author','pub_date','update_date')


admin.site.register(Column, ColumnAdmin)
admin.site.register(Article,ArticleAdmin)
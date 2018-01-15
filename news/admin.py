from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
from .models import Column, Article

#Create CloumnAdmin class, inherit admin.ModelAdmin,showing column's name, slug, intro
class ColumnAdmin(admin.ModelAdmin):
	list_display = ('name','slug','intro')

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','slug','author','pub_date','update_date')
	search_fields = ('title','slug')
	#Setting columns that admin UI will show


admin.site.register(Column, ColumnAdmin)
admin.site.register(Article,ArticleAdmin)
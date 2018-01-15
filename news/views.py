from django.shortcuts import render,redirect #import redirect function
from django.http import HttpResponse
from news.models import Column, Article

# Create your views here.

def index(request):
	columns = Column.objects.all()
	#return HttpResponse('Welcome!')
	return render(request, 'index.html', {'columns':columns})

def column_detail(request,column_slug):
	#return HttpResponse('column slug: ' + column_slug)
	column = Column.objects.get(slug=column_slug)
	return render(request,'news/column.html',{'column':column})

def article_detail(request,pk,article_slug):
	#return HttpResponse('article slug: ' + article_slug)
	try:
		pk = int(pk)
	except:
		return HttpResponse("Invalid Article Number...")

	article = Article.objects.get(pk=pk)
	if article_slug != article.slug:
		return redirect(article,permanent=True) #use function 'get_absolute_url() directly'
	'''
	redirect
redirect(to, permanent=False, *args, **kwargs)[source]
Returns an HttpResponseRedirect to the appropriate URL for the arguments passed.
The arguments could be:
A model: the model's get_absolute_url() function will be called.
A view name, possibly with arguments: urlresolvers.reverse will be used to reverse-resolve the name.
An absolute or relative URL, which will be used as-is for the redirect location.
By default issues a temporary redirect; pass permanent=True to issue a permanent redirect.
	'''
	return render(request,'news/article.html',{'article':article})
	#return HttpResponse(article.get_content())   #return markdown style
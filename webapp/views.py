from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import headlines
from webapp.models import user_comment
from webapp.models import headlines
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm


def index(request):
	
	return render(request, 'blablabla.html')


def home(request):

	blog_list_page = headlines.objects.all().order_by("-pub_date")
	page = request.GET.get('page',1)

	paginator = Paginator(blog_list_page, 3)
	try:
		blog_list = paginator.page(page)
	except PageNotAnInteger:
		blog_list = paginator.page(1)
	except EmptyPage:
		blog_list = paginator.page(paginator.num_page)

	return render(request, 'home.html',{'blog_list':blog_list, 'page':page})



def tech(request):
	blog_list_page = headlines.objects.filter(classifications='Tech').order_by("-pub_date")
	page = request.GET.get('page',1)

	paginator = Paginator(blog_list_page, 3)
	try:
		blog_list = paginator.page(page)
	except PageNotAnInteger:
		blog_list = paginator.page(1)
	except EmptyPage:
		blog_list = paginator.page(paginator.num_page)
	return render(request, 'tech.html',{'blog_list':blog_list, 'page':page})



def science(request):
	blog_list_page = headlines.objects.filter(classifications='Science').order_by("-pub_date")
	page = request.GET.get('page',1)

	paginator = Paginator(blog_list_page, 3)
	try:
		blog_list = paginator.page(page)
	except PageNotAnInteger:
		blog_list = paginator.page(1)
	except EmptyPage:
		blog_list = paginator.page(paginator.num_page)
	return render(request, 'science.html',{'blog_list':blog_list, 'page':page})



def social(request):
	blog_list_page = headlines.objects.filter(classifications='Social').order_by("-pub_date")
	page = request.GET.get('page',1)

	paginator = Paginator(blog_list_page, 3)
	try:
		blog_list = paginator.page(page)
	except PageNotAnInteger:
		blog_list = paginator.page(1)
	except EmptyPage:
		blog_list = paginator.page(paginator.num_page)
	return render(request, 'social.html',{'blog_list':blog_list, 'page':page})

def blank_page(request):

	return render(request, 'blank_page.html')


def article_view(request, full_article):
	view_article = headlines.objects.get(pk=full_article)
	view_counter = view_article.number_view + 1
	headlines.objects.filter(pk = full_article).update(number_view = view_counter)
	context_dict_all = {}
	context_dict_all['view_article'] = headlines.objects.get(pk=full_article)
	context_dict_all['comments'] = user_comment.objects.filter(reference=full_article)
	context_dict_all['comments_number'] = user_comment.objects.filter(reference=full_article).count()
	return render(request, 'article.html', context_dict_all)

def add_comment(request):
	user_name = request.POST['user_name']
	comment = request.POST['comment']
	post_id = request.POST['article_id']
	user_comment.objects.create(
		user_name = user_name,
		comment = comment,
		reference = post_id,
		)
	return HttpResponseRedirect('blank_page')

# def all_likes(request):
# 	comments_id = request.POST.get('comments_id', None)
# 	if(comments_id):
# 		view_article = headlines.objects.get(pk=int(comments_id))
# 		if view_article is not None:
# 			likes = view_article.likes +1
# 			view_article.likes = likes
# 			likes = view_article.likes
# 			view_article.save()

# 	return HttpResponse(likes)

def like(request):
	
	if request.method == 'POST':
		specific_pk = request.POST['article_pk']
		article = headlines.objects.get(pk = specific_pk)
		liked = article.likes + 1
		headlines.objects.filter(pk = specific_pk).update(likes = liked)

	return HttpResponse('')

def dislike(request):
	
	if request.method == 'POST':
		specific_pk = request.POST['article_pk']
		article = headlines.objects.get(pk = specific_pk)
		disliked = article.dislikes + 1
		headlines.objects.filter(pk = specific_pk).update(dislikes = disliked)

	return HttpResponse('')








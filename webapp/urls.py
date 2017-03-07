from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from webapp.models import headlines
from webapp.models import user_comment
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$',views.home, name='index'),
    url(r'^tech$', views.tech, name='index'),
    url(r'^science$', views.science, name='index'),
    url(r'^social$', views.social, name='index'),
   	url(r'^0(?P<full_article>\d+)', views.article_view, name= 'article'),
   	url(r'^post$', views.add_comment, name= 'posted'),
    url(r'^blank_page$', views.blank_page, name='blank_page'),
    url(r'^like', views.like, name='likes'),
    url(r'^dislike', views.dislike, name='dislikes'),

]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
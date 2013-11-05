from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
#from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
	url(r'^media(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

	url(r'^'+settings.HOSTING+'/$', TemplateView.as_view(template_name="index.html")),
	url(r'^'+settings.HOSTING+'/about/$', TemplateView.as_view(template_name="about.html")),
	url(r'^'+settings.HOSTING+'/donate/$', TemplateView.as_view(template_name="donate.html")),
	url(r'^'+settings.HOSTING+'/register/$', TemplateView.as_view(template_name="register.html")),
	url(r'^'+settings.HOSTING+'/add/$', 'pessoas.views.pessoa_adicionar'),
	url(r'^'+settings.HOSTING+'/validation/(?P<codigo>\d+)', 'pessoas.views.pessoa_validarEmail'),
	url(r'^'+settings.HOSTING+'/login/$', 'pessoas.views.pessoa_login'),
	url(r'^'+settings.HOSTING+'/logout/$', 'pessoas.views.pessoa_logout'),
	url(r'^'+settings.HOSTING+'/donatetrue/$', TemplateView.as_view(template_name="donatetrue.html")),
	url(r'^'+settings.HOSTING+'/donatefalse/$', TemplateView.as_view(template_name="donatefalse.html")),
	url(r'^'+settings.HOSTING+'/home/$', 'pessoas.views.pessoa_url'),
	url(r'^'+settings.HOSTING+'/home/safari/$', 'pessoas.views.sarafi_url'),
	url(r'^'+settings.HOSTING+'/home/safari/add/$', 'pessoas.views.safari_adicionar'),
	url(r'^'+settings.HOSTING+'/home/friends/$', 'pessoas.views.friend_url'),
	url(r'^'+settings.HOSTING+'/home/friends/search/$', 'pessoas.views.friend_search'),
	url(r'^'+settings.HOSTING+'/home/friends/add/$', 'pessoas.views.pessoa_perfil'),	
	url(r'^'+settings.HOSTING+'/(?P<codigo>\d+)', 'pessoas.views.pessoa_perfil'),
)

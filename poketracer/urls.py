from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
#from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
	url(r'^media(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt")),
	url(r'^i18n/', include('django.conf.urls.i18n')),

	#url(r'^facebook/', include('django_facebook.urls')),
	#url(r'^accounts/', include('django_facebook.auth_urls')),

	url(r'^$', TemplateView.as_view(template_name="index.html")),
	url(r'^about/$', TemplateView.as_view(template_name="about.html")),
	url(r'^donate/$', TemplateView.as_view(template_name="donate.html")),
	url(r'^register/$', TemplateView.as_view(template_name="register.html")),
	url(r'^friend-codes/$', TemplateView.as_view(template_name="linkFriendCodes.html")),
	url(r'^friend-safari/$', TemplateView.as_view(template_name="linkFriendSafari.html")),
	url(r'^find-pokemon/$', TemplateView.as_view(template_name="linkFindPokemon.html")),
	url(r'^add/$', 'pessoas.views.pessoa_adicionar'),
	url(r'^validation/(?P<codigo>\d+)', 'pessoas.views.pessoa_validarEmail'),
	url(r'^login/$', 'pessoas.views.pessoa_login'),
	url(r'^logout/$', 'pessoas.views.pessoa_logout'),
	url(r'^forgot-email/$', 'pessoas.views.pessoa_lembrarEmail'),
	url(r'^donatetrue/$', TemplateView.as_view(template_name="donatetrue.html")),
	url(r'^donatefalse/$', TemplateView.as_view(template_name="donatefalse.html")),
	
	url(r'^home/$', 'pessoas.views.pessoa_url'),
	url(r'^(?P<codigo>\d+)', 'pessoas.views.pessoa_perfil'),
	url(r'^home/pokemon/$', 'pessoas.views.pokemon_url'),
	url(r'^home/chat/$', 'pessoas.views.pessoa_chat'),

	url(r'^home/user/update/$', 'pessoas.views.pessoa_editar'),

	url(r'^home/safari/$', 'pessoas.views.sarafi_url'),
	url(r'^home/safari/add/', 'pessoas.views.safari_adicionar'),  

	url(r'^home/friends/$', 'pessoas.views.friend_url'),
	url(r'^home/friends/search/$', 'pessoas.views.friend_search'),
	url(r'^home/friends/add/(?P<codigo>\d+)', 'pessoas.views.pessoa_add_amigo'),  
	url(r'^home/friends/update/$', 'pessoas.views.pessoa_atualiza_amigo'),	
	url(r'^home/friends/remove/(?P<codigo>\d+)', 'pessoas.views.pessoa_remove_amigo'),

	url(r'^home/list/added-friends/$', 'pessoas.views.friend_amigos1'),	
	url(r'^home/list/added-me/$', 'pessoas.views.friend_amigos2'),	
	url(r'^home/list/friends-reply/$', 'pessoas.views.friend_amigos3'),	
	url(r'^home/list/safari-updates/$', 'pessoas.views.friend_amigos4'),	
	url(r'^home/list/ranking/$', 'pessoas.views.friend_amigos5'),

	url(r'pokemons/seleciona_por_tipo/(?P<tipo>\w+)/$', 'pokemons.views.seleciona_por_tipo', name='seleciona_por_tipo'),
		
)

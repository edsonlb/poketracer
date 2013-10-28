from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
#from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
	url(r'^media(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

	url(r'^poketracer/$', TemplateView.as_view(template_name="index.html")),
	url(r'^poketracer/about/$', TemplateView.as_view(template_name="about.html")),
	url(r'^poketracer/donate/$', TemplateView.as_view(template_name="donate.html")),
	url(r'^poketracer/register/$', TemplateView.as_view(template_name="register.html")),

	url(r'^poketracer/add/$', 'pessoas.views.pessoa_adicionar'),
	#url(r'^poketracer/pokemon/', include('pokemons.urls')),
)

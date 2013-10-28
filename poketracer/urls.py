from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
#from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
	url(r'^media(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	#url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	#url(r'^admin/painel', include(admin.site.urls)),

	url(r'^poketracer/$', TemplateView.as_view(template_name="index.html")),
	url(r'^poketracer/about/$', TemplateView.as_view(template_name="about.html")),
	#url(r'^admin/funcionario/', include('sistema.urls_funcionario')),
)

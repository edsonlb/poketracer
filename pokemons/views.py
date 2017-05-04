<<<<<<< HEAD
from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson
from pokemons.models import Pokemon


def seleciona_por_tipo(request, tipo):
	tag = '#%s' % tipo

	try:
		pokemons_query = Pokemon.objects.filter(tags__icontains=tag).order_by('nome')

		pokemons = serializers.serialize('json', pokemons_query)

		return HttpResponse(pokemons)
	except pokemons_query.DoesNotExists:
		return None
=======
# Create your views here.
>>>>>>> c2168b8ddd783ef5829a38d8d43c6df367585c21

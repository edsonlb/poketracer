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
>>>>>>> a8c17f46a81f6565aebe88e96638a4306bbaa4c2

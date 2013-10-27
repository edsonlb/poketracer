from django.db import models

class Pokemons(models.Model):
    numero = models.IntegerField(max_length='50', blank=False)
    pokecode = models.CharField(max_length='100', blank=False)
    nome = models.CharField(max_length='200', blank=False)
    foto = models.CharField(max_length='400', blank=False)
    pokedex_link = models.CharField(max_length='400', blank=False)
    tags = models.CharField(max_length='400', blank=True)
    data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
    ativo = models.CharField(max_length='3', default='SIM') 
    codigo = models.AutoField(primary_key=True)





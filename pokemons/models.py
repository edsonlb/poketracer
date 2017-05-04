from django.db import models

class Pokemon(models.Model):
	codigo = models.AutoField(primary_key=True)
	numero = models.IntegerField(blank=False)
	pokecode = models.CharField(max_length='100', blank=True)
	nome = models.CharField(max_length='200', blank=False)
	foto = models.CharField(max_length='400', blank=True)
	pokedex_link = models.CharField(max_length='400', blank=True)
	tags = models.CharField(max_length='400', blank=True)
	data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
<<<<<<< HEAD
	ativo = models.CharField(max_length='3', default='SIM') 

	def __unicode__ (self):
		return unicode(self.numero+'  '+self.nome)
=======
	ativo = models.CharField(max_length='3', default='SIM') 
>>>>>>> c2168b8ddd783ef5829a38d8d43c6df367585c21

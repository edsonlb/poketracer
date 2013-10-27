# This Python file uses the following encoding: utf-8
from django.db import models

class Pessoa(models.Model):
	codigo = models.AutoField(primary_key=True)
	plano = models.CharField(max_length='200', blank=False, default='basic')
	nome = models.CharField(max_length='200', blank=False)
	nickname = models.CharField(max_length='200', blank=False)
	descricao = models.CharField(max_length='200', blank=True)
	codigo = models.CharField(max_length='200', blank=False)
	email = models.CharField(max_length='200', blank=False)
	senha = models.CharField(max_length='200', blank=False)
	badge = models.CharField(max_length='200', blank=True)
	pokemons = models.CharField(max_length='300', blank=True) #RETIRAR QUANDO O OBJ POKEMON ESTIVER PRONTO
	#amigos = models.ManyToManyField(Pessoa, through='Amigo') ESTA COMPLICADO ESSE RELACIONAMENTO DE MUITOS P MUITOS NA MESMA TABELA
	facebook = models.CharField(max_length='300', blank=True)
	twitter = models.CharField(max_length='300', blank=True)
	gplus = models.CharField(max_length='300', blank=True)
	skype = models.CharField(max_length='300', blank=True)
	avatar = models.CharField(max_length='300', blank=True)
	notificacoes = models.BooleanField(default=True)
	tags = models.CharField(max_length='400', blank=True)
	data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
	data_alteracao = models.DateTimeField(auto_now=True, auto_now_add=True)
	ativo = models.CharField(max_length='3', default='VAL') #VAL = Falta Validacao / SIM = Ativo / NAO = Excluido

	def __unicode__(self):
		return self.nome+'('+self.nickname+')'   


class Safari(models.Model):
	codigo = models.AutoField(primary_key=True)
	tipo = models.CharField(max_length='200', blank=False)
	pokemon1 = models.CharField(max_length='100', blank=True)
	pokemon2 = models.CharField(max_length='400', blank=True)
	pokemon3 = models.CharField(max_length='400', blank=True)
	data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
	ativo = models.CharField(max_length='3', default='SIM')

	def __unicode__ (self):
		return self.tipo 

class Amigo(models.Model):
	codigo = models.AutoField(primary_key=True)
	avaliacao = models.IntegerField()
	descricao = models.CharField(max_length='400', blank=True)
	pessoa_cadastro = models.ForeignKey(Pessoa, related_name='pessoa_cadastro_pessoa')
	pessoa_amiga = models.ForeignKey(Pessoa, related_name='pessoa_amiga_pessoa')
	safari = models.ForeignKey(Safari)
	tags = models.CharField(max_length='400', blank=True)
	data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
	data_alteracao = models.DateTimeField(auto_now=True, auto_now_add=True)
	ativo = models.CharField(max_length='3', default='SIM') 

	def __unicode__ (self):
		return self.pessoa_amiga.nome+'('+self.pessoa_amiga.nickname+')' 

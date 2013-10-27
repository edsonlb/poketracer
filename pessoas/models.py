# This Python file uses the following encoding: utf-8
from django.db import models

class Pessoa(models.model):
	plano = 
	nome =
	nickname = 
	descricao = 
	codigo = 
	email = 
	senha =
	badge = 
	safari =
	pokemons =
	amigos = 
	facebook = 
	twitter = 
	gplus = 
	skype = 
	avatar =
	notificacoes =
	tags = 
	data_cadastro =
	data_alteracao =
	ativo =


class Pessoa(models.Model):
	codigo = models.AutoField(primary_key=True)
	sistema = models.CharField(max_length='200', blank=False)
	versao = models.CharField(max_length='100', blank=True)
	observacao = models.CharField(max_length='400', blank=True)
	descricao = models.CharField(max_length='400', blank=True)
	gerente = models.CharField(max_length='200', blank=False)
	link = models.CharField(max_length='400', blank=True)
	download = models.CharField(max_length='400', blank=True)
	tags = models.CharField(max_length='400', blank=True)
	versionamento = models.CharField(max_length='400', blank=True)
	manual = models.CharField(max_length='400', blank=True)
	data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
	ativo = models.CharField(max_length='3', default='SIM')

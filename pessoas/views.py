# This Python file uses the following encoding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from pessoas.models import Pessoa, Safari, Amigo
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def render_response(req, *args, **kwargs):
	kwargs['context_instance'] = RequestContext(req)
	return render_to_response(*args, **kwargs)

def validaEmail(email):

	# Descobrir o código da pessoa, somar com mais 321 e enviar o link criado para o e-mail da pessoa.
	# Quando o e-mail voltar, ele habilita o ativo SIM no cadastro da pessoa e libera ela para entrar no sistema.
	
	mensagem = '<b>TESTE</b><br /> http://www.pokertrace.com/validation/321'

	if email:
		send_mail('PokeTracer: E-mail validation', mensagem, 'PokeTracer <mail@poketracer.com.br>',[email], fail_silently=False)
		return True
	else:
		return False

#===PESSOA=======================================================
#def pessoa_pesquisa(request, pagina=1):

def pessoa_mostrar(request, id = 0):
	pessoa = Pessoa.objects.get(codigo=id)
	return render_response(request,'pessoas/formulario.html', {'pessoa': pessoa, 'acao': 'salvar'} )

def pessoa_adicionar(request):
	pessoa = Pessoa(
		nome = request.POST.get('nome', '').upper(),
		nickname = request.POST.get('nickname', ''),
		codigo = request.POST.get('codigo', ''),
		email = request.POST.get('email', '').upper(),
		senha = request.POST.get('senha', '').upper(),
		)

	pessoa.save()
	validaEmail(pessoa.email)
		
	return render_response(request,'register.html', {'avisoTipo': 'alert-success', 'msg': 'Adicionado com sucesso!'} )

def pessoa_editar(request):
	
	if request.POST['codigo'] >= 1:
		pessoa = Pessoa.objects.get(codigo=request.POST['codigo'])
		pessoa.nome = request.POST['sistema'].upper()
		pessoa.nickname = request.POST['versao']
		pessoa.descricao = request.POST['observacao'].upper()
		pessoa.codigo = request.POST['descricao'].upper()
		#pessoa.email = request.POST['gerente'].upper()
		pessoa.senha = request.POST['link']
		#pessoa.badge = request.POST['download']
		pessoa.facebook = request.POST['tags']
		pessoa.twitter = request.POST['versionamento']
		pessoa.gplus = request.POST['manual']
		pessoa.skype = request.POST['manual']
		#pessoa.avatar = request.POST['manual']
		#pessoa.notificacoes = request.POST['manual']
		#pessoa.tags = request.POST['manual']
		#pessoa.ativo = request.POST['manual']
		pessoa.save()
		return render_response( request,'pessoas/listagem.html', {'avisoTipo': 'alert-success', 'msg': 'Success!'} )
	else:
		return render_response( request,'pessoas/listagem.html', {'avisoTipo': 'alert-danger', 'msg': 'Error!'} )

#===FIM PESSOA=======================================================

#===SAFARI=======================================================
#===FIM SAFARI=======================================================

#===AMIGO=======================================================
#===FIM AMIGO=======================================================

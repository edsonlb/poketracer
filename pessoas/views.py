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

def verificaLogin(request): 
	#PROVISORIO, DEPOIS IMPLEMENTAR AS FERRAMENTAS DO DJANGO
	#TODAS AS PÁGINAS INTERNAS DEVEM CHAMAR ESSA FUNCAO PARA VALIDAR SE JÁ FOI FEITO O LOGIN POR ENQUANTO	
	if not request.session['pessoa']:
		return render_response(request,'index.html')

#===PESSOA=======================================================
#def pessoa_pesquisa(request, pagina=1):

def pessoa_logout(request):
	request.session['pessoa'] = False
	return render_response(request,'index.html')


def pessoa_login(request):
	#RECUPERAR OBJETO DA PESSOA NO VISUAL
	#<div>{{ request.session.pessoa }}</div>

	request.session['pessoa'] = False

	#pessoaSessao = request.GET.get('pessoa')

	email = request.POST.get('email', '').upper().strip()
	senha = request.POST.get('senha', '').upper().strip()

	if len(email) > 3 and len(senha) > 3:
		pessoa = Pessoa.objects.filter(
			Q(email=email) | 
			Q(senha=senha) |
			Q(ativo='SIM'))

		if pessoa:
			request.session['pessoa'] = pessoa[0].codigo
			return render_response(request,'pessoas/home.html', {'pessoa': pessoa[0]} )
		else:
			return render_response(request,'index.html', {'avisoLogin': 'Error - Try Again!'} )
	else:
		return render_response(request,'index.html', {'avisoLogin': 'Error - Try Again!'} )

def pessoa_mostrar(request, id = 0):
	pessoa = Pessoa.objects.get(codigo=id)
	return render_response(request,'pessoas/formulario.html', {'pessoa': pessoa, 'acao': 'salvar'} )

def pessoa_adicionar(request):

	#VALIDAR DADOS QUE VEM DA TELA E VERIFICAR SE JA TEM PESSOA COM O MESMO EMAIL NO SISTEMA

	pessoa = Pessoa(
		nome = request.POST.get('nome', '').upper(),
		nickname = request.POST.get('nickname', ''),
		friendcode = request.POST.get('friendcode', ''),
		email = request.POST.get('email', '').upper(),
		senha = request.POST.get('senha', '').upper(),
		)

	pessoa.save()
	validaEmail(pessoa.email)
		
	return render_response(request,'register.html', {'avisoTipo': 'alert-success', 'msg': 'Verify your e-mail '+pessoa.email+' for confirmation!'} )

def pessoa_editar(request):
	
	if request.POST['codigo'] >= 1:
		pessoa = Pessoa.objects.get(codigo=request.POST['codigo'])
		pessoa.nome = request.POST['nome'].upper()
		pessoa.nickname = request.POST['nickname']
		pessoa.descricao = request.POST['descricao'].upper()
		pessoa.friendcode = request.POST['friendcode'].upper()
		#pessoa.email = request.POST['gerente'].upper()
		pessoa.senha = request.POST['senha']
		#pessoa.badge = request.POST['download']
		pessoa.facebook = request.POST['facebook']
		pessoa.twitter = request.POST['twitter']
		pessoa.gplus = request.POST['gplus']
		pessoa.skype = request.POST['skype']
		#pessoa.avatar = request.POST['manual']
		#pessoa.notificacoes = request.POST['manual']
		#pessoa.tags = request.POST['manual']
		#pessoa.ativo = request.POST['manual']
		pessoa.save()
		return render_response( request,'/pessoas/listagem.html', {'avisoTipo': 'alert-success', 'msg': 'Success!'} )
	else:
		return render_response( request,'/pessoas/listagem.html', {'avisoTipo': 'alert-danger', 'msg': 'Error!'} )

def pessoa_url(request): 
	verificaLogin(request)
	return render_response( request,'pessoas/home.html' )

#===FIM PESSOA=======================================================

#===SAFARI=======================================================
def sarafi_url(request): 
	verificaLogin(request)
	return render_response( request,'pessoas/registersafari.html' )

def safari_adicionar(request):
	safari = Safari(
		tipo = request.POST.get('tipo', '').upper(),
		pokemon1 = request.POST.get('pokemon1', '').upper(),
		pokemon2 = request.POST.get('pokemon2', '').upper(),
		pokemon3 = request.POST.get('pokemon3', '').upper(),
		data_cadastro = request.POST.get('data_cadastro', '').upper(),
		)

	safari.save()
		
	return render_response(request,'registersafari.html', {'avisoTipo': 'alert-success', 'msg': 'Thank you. Safari successfully registered.'} )

#===FIM SAFARI=======================================================

#===AMIGO=======================================================
#===FIM AMIGO=======================================================

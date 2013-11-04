# This Python file uses the following encoding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from pessoas.models import Pessoa, Safari, Amigo
from pokemons.models import Pokemon
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from datetime import date
from django.shortcuts import redirect
from django.conf import settings


def render_response(req, *args, **kwargs):
	kwargs['context_instance'] = RequestContext(req)
	return render_to_response(*args, **kwargs)

def validaEmail(email, codigo):

	# Descobrir o código da pessoa, somar com mais 321 e enviar o link criado para o e-mail da pessoa.
	# Quando o e-mail voltar, ele habilita o ativo SIM no cadastro da pessoa e libera ela para entrar no sistema.
	codigo = codigo + 321
	mensagem = 'Click on this link or Copy & Paste in your internet Browser to validate your registration at PokeTracer: http://www.pokertrace.com/validation/%d' % codigo 

	if email:
		send_mail('PokeTracer: E-mail validation', mensagem, 'PokeTracer <mail@poketracer.com.br>',[email], fail_silently=False)
		return True
	else:
		return False

def validaLogin(request):
	if request.session['pessoaCodigo']: 
		return True
	else:
		return False

#===PESSOA=======================================================

def pessoa_url(request): 

	if validaLogin(request):
		pessoa = Pessoa.objects.get(codigo=request.session['pessoaCodigo'])
<<<<<<< HEAD
		amigos1 = Amigo.objects.filter(pessoa_cadastro=pessoa,ativo='SIM').order_by('data_cadastro')[:5]
		amigos2 = Amigo.objects.filter(pessoa_cadastro=pessoa,ativo='SIM').order_by('data_cadastro')[:5]
		amigos3 = Amigo.objects.filter(pessoa_cadastro=pessoa,ativo='SIM').order_by('data_cadastro')[:5]
		amigos4 = Amigo.objects.filter(pessoa_cadastro=pessoa,ativo='SIM').order_by('data_cadastro')[:5]
		amigos5 = Amigo.objects.filter(pessoa_cadastro=pessoa,ativo='SIM').order_by('data_cadastro')[:5]

		return render_response(request,'pessoas/home.html', {'pessoa': pessoa,
															 'amigo1': amigos1,
															 'amigo2': amigos2,
															 'amigo3': amigos3,
															 'amigo4': amigos4,
															 'amigo5': amigos5 })
=======
		meuSafari = Amigo.objects.get(pessoa_cadastro_id=request.session['pessoaCodigo'],pessoa_amiga_id=request.session['pessoaCodigo'],ativo='SIM')
		return render_response(request,'pessoas/home.html', {'pessoa': pessoa, 'meuSafari': meuSafari} )
>>>>>>> 050b0d69d3d4f3d7ea488d277caca20a89397c65
	else:
		return render_response(request,'index.html')

def pessoa_validarEmail(request, codigo=0):
	try:
		codigo = int(codigo) - int(321)
		pessoa = Pessoa.objects.get(codigo=codigo, ativo='VAL')

		print '--->'+pessoa.nome

		if pessoa:
			pessoa.ativo = 'SIM'
			pessoa.save()
			return render_response(request,'index.html', {'avisoLogin': 'OK! You can Login now!'} )
	except Exception as e:
		return render_response(request,'index.html', {'avisoLogin': 'User already checked!'} )

def pessoa_logout(request):
	request.session['pessoaCodigo'] = False
	request.session.flush()
	return render_response(request,'index.html')


def pessoa_login(request):
	#RECUPERAR OBJETO DA PESSOA NO VISUAL
	#	<div>{{ request.session.pessoaCodigo }}</div>
	# RECUPERAR O CODIGO DA PESSOA NO PYTHON
	#	request.session['pessoaCodigo']

	if request.method == 'POST':
		request.session['pessoaCodigo'] = False
		email = request.POST.get('email', '').upper().strip()
		senha = request.POST.get('senha', '').upper().strip()

		if len(email) > 3 and len(senha) > 3:

			try:
				pessoa = Pessoa.objects.get(email=email, senha=senha, ativo='SIM')
			except Exception as e:
				return render_response(request,'index.html', {'avisoLogin': 'Error - Try Again!'} )

			if pessoa.codigo > 0:
				request.session['pessoaCodigo'] = pessoa.codigo
				return render_response(request,'pessoas/home.html', {'pessoa': pessoa } )
			else:
				return render_response(request,'index.html', {'avisoLogin': 'Error - Try Again!!'} )
		else:
			return render_response(request,'index.html', {'avisoLogin': 'Error - Try Again!!!'} )
	else:
		return render_response(request,'index.html', {'avisoLogin': 'Error - Try Again!!!!'} )

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
	validaEmail(pessoa.email, pessoa.codigo)
		
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

def pessoa_perfil(request, codigo=0):
	if codigo > 0:
		try:
			indicacoesSafari = Amigo.objects.filter(pessoa_amiga_id=codigo, ativo='SIM').order_by('data_cadastro')
		except Exception as e:
			indicacoesSafari = Amigo()

		try:
			#PRIMEIRO PROCURA O DADO MAIS COMPLETO DO SAFARI
			pessoa = Amigo.objects.get(pessoa_cadastro_id=codigo,pessoa_amiga_id=codigo,ativo='SIM')
			return render_response( request,'pessoas/user.html' , {'pessoa': pessoa, 'indicacoesSafari': indicacoesSafari}  )
		except Exception as e:
			#SE NAO RETORNAR NADA NO SAFARI, ELE TENTA DIRETO PELO PERFIL
			try:
				pessoa = Pessoa.objects.get(codigo=codigo,ativo='SIM')
				return render_response( request,'pessoas/user.html' , {'pessoa': pessoa, 'indicacoesSafari': indicacoesSafari} )
			except Exception as e:
				#SE NAO RETORNAR NADA MESMO ASSIM, ELE RETORNA PARA A PAGINA INICIAL
				return render_response( request,'index.html')

	else:
		return render_response( request,'index.html') #SE CASO PASSAR A URL SEM CODIGO

#===FIM PESSOA=======================================================

#===SAFARI=======================================================

def sarafi_url(request):
	if validaLogin(request):
		pokemons = Pokemon.objects.filter(ativo='SIM').order_by('numero')
		try:
			meuSafari = Amigo.objects.get(pessoa_cadastro_id=request.session['pessoaCodigo'],pessoa_amiga_id=request.session['pessoaCodigo'],ativo='SIM')
		except Exception as e:
			meuSafari = Amigo()

		try:
			indicacoesSafari = Amigo.objects.filter(pessoa_amiga_id=request.session['pessoaCodigo'],ativo='SIM').order_by('data_cadastro')[:5]
		except Exception as e:
			indicacoesSafari = Amigo()


		return render_response( request,'pessoas/registersafari.html' , {'pokemons':pokemons, 'meuSafari': meuSafari, 'indicacoesSafari': indicacoesSafari} )

	else:
		return render_response( request,'index.html')

def safari_adicionar(request):
	if request.method == 'POST':

		pessoa = Pessoa.objects.get(codigo=request.session['pessoaCodigo'])

		if request.POST['acao'] == 'alterar':
			amigo = Amigo.objects.get(pessoa_cadastro_id=request.session['pessoaCodigo'],pessoa_amiga_id=request.session['pessoaCodigo'],ativo='SIM')
			safari = amigo.safari 
		else:
			safari = Safari() #COLOCAR PARA CRIA O OBJETO EM BRANCO
			amigo = Amigo()

		safari.tipo = request.POST['tipo']

		pokemon = Pokemon(codigo=request.POST['pokemon1'])
		safari.pokemon1 = pokemon
		pokemon = Pokemon(codigo=request.POST['pokemon2'])
		safari.pokemon2 = pokemon
		pokemon = Pokemon(codigo=request.POST['pokemon3'])
		safari.pokemon3 = pokemon
		safari.save()

		amigo.avaliacao = 5 #AVALIACAO VAI DE 0 A 5
		amigo.descricao = '#' #PADRAO SO PARA NAO DEIXAR NADA EM BRANCO
		pessoa = Pessoa(codigo=request.session['pessoaCodigo'])
		amigo.pessoa_cadastro = pessoa #PESSOA QUE EFETUOU O CADASTRO
		amigo.pessoa_amiga = pessoa #PESSOA PARA QUEM ELA VAI CADASTRAR O SAFARI
		amigo.safari = safari
		amigo.tags = '#' #PADRAO SO PARA NAO DEIXAR NADA EM BRANCO
		
		amigo.save()

		return render_response(request,'pessoas/home.html', {'avisoTipo': 'alert-success', 'msg': 'Thank you. Your Safari successfully registered.'} )
	else:
		return render_response(request,'pessoas/home.html', {'avisoTipo': 'alert-danger', 'msg': 'Error!.'} )

#===FIM SAFARI=======================================================


#===AMIGO=======================================================

<<<<<<< HEAD


#===FIM AMIGO===================================================
=======
def friend_url(request):
	if validaLogin(request):
		amigos = Amigo.objects.filter(pessoa_cadastro_id=request.session['pessoaCodigo'],ativo='SIM').order_by('data_cadastro')

		return render_response( request,'pessoas/friends.html' , {'amigos':amigos} )
	else:
		return render_response( request,'index.html')

def friend_search(request):
	if validaLogin(request):
		if request.method == 'POST':
			textoPesquisa = request.POST['textoPesquisa'].upper().strip();
		else:
			textoPesquisa = ''

		if len(textoPesquisa) > 1:
			sql = ("SELECT pa.codigo FROM pessoas_amigo pa "
				" INNER JOIN pessoas_pessoa pesCad on pesCad.codigo = pa.pessoa_cadastro_id "
				" LEFT JOIN pessoas_safari pesSaf on pesSaf.codigo = pa.safari_id "
				" LEFT JOIN pokemons_pokemon pok1 on pok1.codigo = pesSaf.pokemon1_id "
				" LEFT JOIN pokemons_pokemon pok2 on pok2.codigo = pesSaf.pokemon2_id "
				" LEFT JOIN pokemons_pokemon pok3 on pok3.codigo = pesSaf.pokemon3_id "
				" WHERE "
				" (pesCad.nome like '%s' OR "
				" pesCad.nome like '%s' OR "
				" pesCad.nickname like '%s' OR "
				" pesCad.friendcode like '%s' OR "
				" pesSaf.tipo like '%s' OR "
				" pok1.nome like '%s' OR "
				" pok2.nome like '%s' OR "
				" pok1.tags like '%s' OR "
				" pok2.tags like '%s' OR "
				" pok3.tags like '%s' OR "
				" pok3.nome like '%s') AND "
				" pa.pessoa_amiga_id = pa.pessoa_cadastro_id") % ('%%'+textoPesquisa+'%%','%%'+textoPesquisa+'%%','%%'+textoPesquisa+'%%','%%'+textoPesquisa+'%%', '%%'+textoPesquisa+'%%', '%%'+textoPesquisa+'%%', '%%'+textoPesquisa+'%%',
				'%%'+textoPesquisa+'%%','%%'+textoPesquisa+'%%','%%'+textoPesquisa+'%%','%%'+textoPesquisa+'%%')
	
			amigos = Amigo.objects.raw(sql)
		else:	
			amigos = Amigo.objects.filter(pessoa_cadastro_id=request.session['pessoaCodigo'],ativo='SIM').order_by('data_cadastro')

		return render_response( request,'pessoas/friends.html' , {'amigos':amigos, 'textoPesquisa': textoPesquisa} )
	else:
		return render_response( request,'index.html')





#===FIM AMIGO=======================================================
>>>>>>> 050b0d69d3d4f3d7ea488d277caca20a89397c65

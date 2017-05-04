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
from django.db.models import Sum
from django.template.defaultfilters import slugify
#from recaptcha.client import captcha 
from django.utils.translation import ugettext_lazy as _


def render_response(req, *args, **kwargs):
	kwargs['context_instance'] = RequestContext(req)
	return render_to_response(*args, **kwargs)

def validaEmail(email, codigo):

	# Descobrir o código da pessoa, somar com mais 321 e enviar o link criado para o e-mail da pessoa.
	# Quando o e-mail voltar, ele habilita o ativo SIM no cadastro da pessoa e libera ela para entrar no sistema.
	codigo = codigo + 321
	mensagem = unicode(_('Click on this link or Copy & Paste in your internet Browser to validate your registration at PokeTracer: http://poketracer.com/validation/%d' % codigo))

	try:
		if email:
			send_mail('PokeTracer: E-mail validation', mensagem, 'PokeTracer <mail@poketracer.com.br>',[email], fail_silently=False)
			return True
		else:
			return False
	except Exception as e:

		return redirect('/',{'avisoTipo': 'alert-danger', 'msg': unicode(_('Error on e-mail validation and sending! Try Again!'))})

def senhaEmail(email, senha, codigo):

	codigo = codigo + 321
	mensagem = unicode(_('You requested to send your PokeTracer password by email, so here it is: '+senha+' (and follow your validation link if you had problem when registering on the website: http://poketracer.com/validation/'+str(codigo)+' )')) 

	try:
		if email:
			send_mail('PokeTracer: Password Request', mensagem, 'PokeTracer <mail@poketracer.com.br>',[email], fail_silently=False)
			return True
		else:
			return False
	except Exception as e:
		raise e
		return False

def amigoEmail(pessoa_amiga_codigo, request):

	try:
		amigos = Amigo.objects.get(pessoa_cadastro_id=pessoa_amiga_codigo, pessoa_amiga_id=request.session['pessoaCodigo'] ,ativo='SIM')
		jaAdicionou = True
	except Exception as e:
		jaAdicionou = False


	if jaAdicionou:
		email = amigos.pessoa_cadastro.email
		mensagem = unicode(_('You added '+amigos.pessoa_amiga.nickname+' ('+amigos.pessoa_amiga.friendcode+') in '+str(amigos.data_cadastro)+', and now he added you back on PokeTracer! To remind you, here is the user profile: http://poketracer.com/'+str(amigos.pessoa_amiga.codigo)))
	else:
		pessoa_cadastro = Pessoa.objects.get(codigo=request.session['pessoaCodigo'] ,ativo='SIM')
		pessoa_amiga = Pessoa.objects.get(codigo=pessoa_amiga_codigo ,ativo='SIM')
		email = pessoa_amiga.email
		mensagem = unicode(_('The Pokemon trainer '+pessoa_cadastro.nickname+' ( http://poketracer.com/'+str(pessoa_cadastro.codigo)+' ) added you as a friend on PokeTracer!'))

	try:
		if email:
			send_mail('PokeTracer: Friend Alert!', mensagem, 'PokeTracer <mail@poketracer.com.br>',[email], fail_silently=False)
			return True
		else:
			return False
	except Exception as e:
		return False

def updateEmail(pessoa_amiga_codigo, request):

	try:
		pessoaAmiga = Pessoa.objects.get(codigo=pessoa_amiga_codigo,ativo='SIM')
		email = pessoaAmiga.email
		encontrou = True
	except Exception as e:
		encontrou = False

	if encontrou:
		mensagem = unicode(_('Your profile on PokeTracer have received an update by this user ( http://poketracer.com/'+str(request.session['pessoaCodigo'])+' ) check your profile here: http://poketracer.com/'+str(pessoa_amiga_codigo)))

		try:
			send_mail('PokeTracer: Account Update!', mensagem, 'PokeTracer <mail@poketracer.com.br>',[email], fail_silently=False)
			return True
		except Exception as e:
			return False
	else:
		return False


def validaLogin(request):
	try:
		if request.session['pessoaCodigo']: 
			return True
		else:
			return False
	except Exception as e:
		return False

#===PESSOA=======================================================

def pessoa_url(request): 

	if validaLogin(request):
		pessoaCodigo = str(request.session['pessoaCodigo'])
		try:
			#Last Friends added by me...
			#amigos1 = Amigo.objects.filter(pessoa_cadastro_id=request.session['pessoaCodigo'],ativo='SIM').exclude(pessoa_amiga_id=request.session['pessoaCodigo']).order_by('-data_cadastro')[:5]
			amigos1 = Amigo.objects.raw("select * from pessoas_amigo where ativo = 'SIM' and descricao = 'THIS IS ME! WELCOME TO MY SAFARI!' and pessoa_cadastro_id in (select pessoa_amiga_id from pessoas_amigo where ativo = 'SIM' and pessoa_cadastro_id = %s and pessoa_amiga_id not in (select pessoa_cadastro_id from pessoas_amigo where pessoa_cadastro_id in (select pessoa_amiga_id from pessoas_amigo where pessoa_cadastro_id = %s and ativo = 'SIM') and pessoa_amiga_id = %s and ativo = 'SIM')) order by data_cadastro DESC  LIMIT 0 , 5",[pessoaCodigo, pessoaCodigo,pessoaCodigo])[:5]
		except Exception as e:
			raise e
			amigos1 = Amigo()

		try:
			#Latest people who added me...
			amigos2 = Amigo.objects.raw("select * from pessoas_amigo where ativo = 'SIM' and descricao = 'THIS IS ME! WELCOME TO MY SAFARI!' and pessoa_cadastro_id in (select pessoa_cadastro_id from pessoas_amigo where ativo = 'SIM' and  pessoa_amiga_id = %s and pessoa_cadastro_id not in (select pessoa_cadastro_id from pessoas_amigo where pessoa_cadastro_id in (select pessoa_amiga_id from pessoas_amigo where pessoa_cadastro_id = %s and ativo = 'SIM' ) and pessoa_amiga_id = %s and ativo = 'SIM')) LIMIT 0 , 5",[pessoaCodigo,pessoaCodigo,pessoaCodigo])[:5]
		except Exception as e:
			#raise e
			amigos2 = Amigo()

		try:
			#Latest friend connection...
			amigos3 = Amigo.objects.raw("select * from pessoas_amigo where ativo = 'SIM' and descricao = 'THIS IS ME! WELCOME TO MY SAFARI!' and pessoa_cadastro_id in (select pessoa_cadastro_id from pessoas_amigo where ativo = 'SIM' and pessoa_cadastro_id in (select pessoa_amiga_id from pessoas_amigo where pessoa_cadastro_id = %s and pessoa_amiga_id <> %s and ativo = 'SIM') and pessoa_amiga_id = %s and ativo = 'SIM') order by data_cadastro desc LIMIT 0 , 5",[pessoaCodigo,pessoaCodigo,pessoaCodigo])[:5]
		except Exception as e:
			#raise e
			amigos3 = Amigo()

		try:
			#Safaris that were updated by their owners or friends...
			#amigos4 = Amigo.objects.raw('SELECT * FROM pessoas_amigo GROUP BY pessoa_amiga_id ORDER BY data_alteracao DESC')[:5]
			#amigos4 = Amigo.objects.raw("select * from pessoas_amigo where ativo = 'SIM' and descricao = 'THIS IS ME! WELCOME TO MY SAFARI!' and pessoa_cadastro_id in (select pessoa_cadastro_id from pessoas_amigo where ativo = 'SIM' GROUP BY pessoa_cadastro_id) ORDER BY data_alteracao DESC LIMIT 0 , 11")[:11]
			amigos4 = Amigo.objects.raw("select pa.* from pessoas_amigo pa inner join pessoas_pessoa p on p.codigo = pa.pessoa_cadastro_id and p.ativo = 'SIM' where pa.pessoa_amiga_id = pa.pessoa_cadastro_id and pa.ativo = 'SIM' ORDER BY pa.data_alteracao DESC LIMIT 0 , 15")[:15]
		except Exception as e:
			#raise e
			amigos4 = Amigo()

		try:
			#User by qualifications...
			amigos5 = Amigo()
			#amigos5 = Amigo.objects.raw('SELECT codigo FROM pessoas_amigo GROUP BY pessoa_amiga_id ORDER BY count(1) DESC')[:5]
		except Exception as e:
			#raise e
			amigos5 = Amigo()

		try:
			meuSafari = Amigo.objects.get(pessoa_cadastro_id=request.session['pessoaCodigo'],pessoa_amiga_id=request.session['pessoaCodigo'],ativo='SIM')
		except Exception as e:
			#raise e
			meuSafari = Amigo()

		return render_response(request,'pessoas/home.html', {'meuSafari': meuSafari,
															 'amigo1': amigos1,
															 'amigo2': amigos2,
															 'amigo3': amigos3,
															 'amigo4': amigos4,
															 'amigo5': amigos5 })
	else:
		#return render_response(request,'index.html')
		return redirect('/')

def pessoa_lembrarEmail(request):
	if request.method == 'POST':
		try:
			email = request.POST.get('email', '').upper().strip()
			if len(email) > 5:
				pessoa = Pessoa.objects.filter(email=email).count()
			else:
				return render_response(request,'index.html',{'avisoTipo': 'alert-warning', 'msg': _('Invalid E-mail! Try Again!')})			

			if pessoa >= 1:
				pessoa = Pessoa.objects.filter(email=email)[:1]
				if senhaEmail(pessoa[0].email, pessoa[0].senha, pessoa[0].codigo):
					return render_response(request,'index.html', {'avisoTipo': 'alert-info', 'msg': _('An e-mail ('+email+') was sent to you with your password and instructions , Ok!')})
				else:
					return render_response(request,'index.html',{'avisoTipo': 'alert-warning', 'msg': _('Error sending email to '+email+' . Try Again!')})	
			else:
				return render_response(request,'index.html', {'avisoTipo': 'alert-warning', 'msg': _('Register at PokeTracer because we did not find your e-mail '+email+' on the system.')})
				
		except Exception as e:
			raise e
			return render_response(request,'index.html', {'avisoTipo': 'alert-danger', 'msg': _('Our system have been dropped OR erroneous data found on your profile!')})
	else:
		return redirect('/')


def pessoa_validarEmail(request, codigo=0):
	try:
		codigo = int(codigo) - int(321)
		pessoa = Pessoa.objects.get(codigo=codigo, ativo='VAL')

		if pessoa:
			pessoa.ativo = 'SIM'
			pessoa.save()
			return render_response(request,'index.html', {'avisoLogin': _('OK! You can Login now!')} )
	except Exception as e:
		return render_response(request,'index.html', {'avisoLogin': _('User already checked!')} )

def pessoa_logout(request):
	request.session['pessoaCodigo'] = False
	del request.session['pessoaCodigo']
	request.session.flush()
	request.session.modified = True
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
				return render_response(request,'index.html', {'avisoLogin': _('Error - Try Again!')} )

			if pessoa.codigo > 0:
				request.session['pessoaCodigo'] = pessoa.codigo
				return redirect('/home/', {'pessoa': pessoa})
			else:
				return render_response(request,'index.html', {'avisoLogin': _('Error - Try Again!!')} )
		else:
			return render_response(request,'index.html', {'avisoLogin': _('Error - Try Again!!!')} )
	else:
		return render_response(request,'index.html', {'avisoLogin': _('Error - Try Again!!!!')} )

def pessoa_adicionar(request):
	#Validacao Captcha Google
	#response = captcha.submit(
	#	request.POST.get('recaptcha_challenge_field'),
	#	request.POST.get('recaptcha_response_field'),
	#	'6LcnKOoSAAAAAAkgNOpNskdAmZWdmdjmR8dWU1Mt',
	#	request.META['REMOTE_ADDR'],
	#	)
	
	#if response.is_valid:  
	if True:  
		pessoaValidacao = Pessoa.objects.filter(email=request.POST.get('email', '').strip().upper(), ativo='SIM').count()

		if pessoaValidacao > 0:
			return render_response(request,'register.html', {'avisoTipo': 'alert-danger', 'msg': _('Error! Your email is already registered! Look on the page footer to retrieve your password.')} )

		if len(slugify(request.POST.get('nome', '').strip())) <= 5:
			return render_response(request,'register.html', {'avisoTipo': 'alert-danger', 'msg': _('Error! Name and Last Name required!')} )

		if len(slugify(request.POST.get('nickname', '').strip())) <= 3:
			return render_response(request,'register.html', {'avisoTipo': 'alert-danger', 'msg': _('Error! In game name required! Name > 3 character!')} )

		if len(slugify(request.POST.get('senha', '').strip())) <= 5:
			return render_response(request,'register.html', {'avisoTipo': 'alert-danger', 'msg': _('Error! Choose a good password!')} )

		if int(request.POST.get('friendcode', '0').strip().replace('-','')) < 1000000000: 
			return render_response(request,'register.html', {'avisoTipo': 'alert-danger', 'msg': _('Error! Enter a real FriendCode!')} )


		friendcode = request.POST.get('friendcode').strip()
		friendcode = friendcode.replace(' ', '-')

		if len(friendcode) == 12:
			friendcode = friendcode[0:4]+'-'+friendcode[4:8]+'-'+friendcode[8:12]

		try:
			pessoa = Pessoa(
				nome = slugify(request.POST.get('nome', '').strip()).upper().replace('-',' '),
				nickname = slugify(request.POST.get('nickname', '').strip()).upper().replace('-',' '),
				friendcode = request.POST.get('friendcode', '').strip(),
				email = request.POST.get('email', '').strip().upper(),
				senha = slugify(request.POST.get('senha', '')).strip(),

				shinyvalue = '0000',
				gameregion = '___',
				nativevivillon = 'NOVIVILLON.png',
				)

			pessoa.save()

			safari = Safari(
				tipo = 'I DONT KNOW!',	
				pokemon1_id = 1,
				pokemon2_id = 1,
				pokemon3_id = 1,
				)

			safari.save()

			amigo = Amigo(
				avaliacao = 5,
				descricao = 'THIS IS ME! WELCOME TO MY SAFARI!',
				pessoa_cadastro = pessoa,
				pessoa_amiga = pessoa,
				safari = safari,
				tags = '#'+str(pessoa.codigo),
				)

			amigo.save()
			validaEmail(pessoa.email, pessoa.codigo)

		except Exception as e:
			return render_response(request,'register.html', {'avisoTipo': 'alert-danger', 'msg': _('Error! Verify your information and try again!')} )
			
		return render_response(request,'register.html', {'avisoTipo': 'alert-success', 'msg': _('Verify your e-mail '+pessoa.email+' for confirmation!')} )
	else:
		return render_response(request,'register.html', {'avisoTipo': 'alert-danger', 'msg': _('Error! Wrong Captcha! Try again.')} ) 

	

def pessoa_editar(request):
	if validaLogin(request):  
		if request.method == 'POST':
			if request.session['pessoaCodigo'] >= 1:
				pessoa = Pessoa.objects.get(codigo=request.session['pessoaCodigo'])
				pessoa.nome = slugify(request.POST['nome']).strip().upper().replace('-',' ')  
				pessoa.nickname = slugify(request.POST['nickname']).strip().upper().replace('-',' ')
				pessoa.descricao = slugify(request.POST['descricao']).strip().upper().replace('-',' ')[0:140]
				pessoa.friendcode = slugify(request.POST['friendcode']).strip().upper()				
				pessoa.gameregion = request.POST['gameregion']
				pessoa.nativevivillon = request.POST['nativevivillon']
				pessoa.facebook = request.POST['facebook'].strip()
				pessoa.twitter = request.POST['twitter'].strip()
				pessoa.gplus = request.POST['gplus'].strip()
				pessoa.skype = request.POST['skype'].strip()
				#pessoa.avatar = request.POST['manual']
				#pessoa.notificacoes = request.POST['manual']
				#pessoa.tags = request.POST['manual']
				#pessoa.ativo = request.POST['manual']
				#pessoa.email = request.POST['gerente'].upper()
				#pessoa.senha = request.POST['senha']
				#pessoa.badge = request.POST['download']

				try:
					pessoa.shinyvalue = int(slugify(request.POST['shinyvalue']).strip().upper()[0:4])
				except Exception as e:
					pessoa.shinyvalue = '0000'

				pessoa.save()
				return redirect('/home/')
			else:
				return render_response( request,'index.html')
		else:
			return render_response( request,'index.html')
	else:
		return redirect('/')

def pessoa_remove_amigo(request, codigo=0):
	if validaLogin(request):
		if codigo > 0:
			meuAmigo = Amigo.objects.get(pessoa_cadastro_id=request.session['pessoaCodigo'],pessoa_amiga_id=codigo,ativo='SIM')
			meuAmigo.ativo = 'NAO' #REMOVER TB O SAFARI COM O NAO FUTURAMENTE
			meuAmigo.safari.ativo = 'NAO'
			meuAmigo.save()

			return redirect('/home/')
		else:
			return render_response( request,'index.html') #SE CASO PASSAR A URL SEM CODIGO
	else:
		return redirect('/') #SE CASO NAO TENHA FEITO LOGIN

def pessoa_add_amigo(request, codigo=0):
	if validaLogin(request):
		if codigo > 0:
			safari = Safari()
			amigo = Amigo()
			safari.tipo = 'I DONT KNOW!'	
			safari.pokemon1_id = 1
			safari.pokemon2_id = 1
			safari.pokemon3_id = 1

			safari.save()

			amigo = Amigo()
			amigo.safari = safari
			amigo.avaliacao = 0
			#amigo.descricao = 
			amigo.pessoa_cadastro_id = request.session['pessoaCodigo']
			amigo.pessoa_amiga_id = codigo
			#amigo.tags = request.POST['tags'].upper().strip()
			
			amigo.save()

			amigoEmail(codigo, request)
			return redirect('/'+codigo)
		else:
			return render_response( request,'index.html') #SE CASO PASSAR A URL SEM CODIGO
	else:
		return redirect('/') #SE CASO NAO TENHA FEITO LOGIN

def verificarAmizade(request, codigo=0):
	try:
		verificaAmigo = Amigo.objects.filter(pessoa_cadastro_id=request.session['pessoaCodigo'],pessoa_amiga_id=codigo, ativo='SIM').count()

		if verificaAmigo > 0:
			return True
		else:
			return False
	except Exception as e:
		#raise e
		return False

def pessoa_perfil(request, codigo=0):
	if codigo > 0:
		try:
			pokemons = Pokemon.objects.filter(ativo='SIM').order_by('nome')
		except Exception as e:
			#raise e
			pokemons = Pokemon()

		try:
			meuSafariComPessoa = Amigo.objects.get(pessoa_cadastro_id=request.session['pessoaCodigo'],pessoa_amiga_id=codigo,ativo='SIM')
		except Exception as e:
			meuSafariComPessoa = Amigo()

		try:
			indicacoesSafari = Amigo.objects.filter(pessoa_amiga_id=codigo, ativo='SIM').order_by('data_cadastro')
		except Exception as e:
			#raise e
			indicacoesSafari = Amigo()

		amizade = verificarAmizade(request, codigo)

		try:
			#PRIMEIRO PROCURA O DADO MAIS COMPLETO DO SAFARI
			pessoa = Amigo.objects.get(pessoa_cadastro_id=codigo,pessoa_amiga_id=codigo,ativo='SIM')
			return render_response( request,'pessoas/user.html' , {'pessoa': pessoa, 'indicacoesSafari': indicacoesSafari, 'pokemons': pokemons, 'amizade': amizade, 'meuSafariComPessoa':meuSafariComPessoa}  )
		except Exception as e:
			#SE NAO RETORNAR NADA NO SAFARI, ELE TENTA DIRETO PELO PERFIL
			#raise e
			try:
				pessoa = Pessoa.objects.get(codigo=codigo,ativo='SIM')
				return render_response( request,'pessoas/user.html' , {'pessoa': pessoa, 'indicacoesSafari': indicacoesSafari, 'pokemons': pokemons, 'amizade': amizade, 'meuSafariComPessoa':meuSafariComPessoa} )
			except Exception as e:
				#SE NAO RETORNAR NADA MESMO ASSIM, ELE RETORNA PARA A PAGINA INICIAL
				#raise e
				return render_response( request,'index.html')

	else:
		return redirect('/') #SE CASO PASSAR A URL SEM CODIGO

def pessoa_atualiza_amigo(request):
	if validaLogin(request):
		if request.method == 'POST':
			amigo = Amigo.objects.get(codigo=request.POST['safari_codigo'])

			if request.POST['tipo'] != 'I DONT KNOW!':
				amigo.safari.tipo = request.POST['tipo']
			else:
				amigo.safari.tipo = 'I DONT KNOW!'	

			if request.POST['pokemon1'] != 'I DONT KNOW!' and request.POST['pokemon1'] > 0:
				amigo.safari.pokemon1_id = request.POST['pokemon1']
			else:
				amigo.safari.pokemon1_id = 1

			if request.POST['pokemon2'] != 'I DONT KNOW!' and request.POST['pokemon2'] > 0:
				amigo.safari.pokemon2_id = request.POST['pokemon2']
			else:
				amigo.safari.pokemon2_id = 1

			if request.POST['pokemon3'] != 'I DONT KNOW!' and request.POST['pokemon3'] > 0:
				amigo.safari.pokemon3_id = request.POST['pokemon3']
			else:
				amigo.safari.pokemon3_id = 1

			amigo.safari.save()

			amigo.avaliacao = request.POST['avaliacao']
			amigo.descricao = request.POST['descricao'].upper().strip()[:140]
			#amigo.pessoa_cadastro_id = request.session['pessoaCodigo']
			#amigo.pessoa_amiga_id = request.POST['pessoa_amiga']
			amigo.tags = request.POST['tags'].upper().strip()
			
			amigo.save()

			updateEmail(request.POST['pessoa_amiga'], request)

			return redirect('/'+request.POST['pessoa_amiga'])
		else:
			return render_response(request,'index.html')
	else:
		return redirect('/')

def pessoa_chat(request):
	if validaLogin(request):
		return render_response(request,'chat.html')
	else:
		return redirect('/')

#===FIM PESSOA=======================================================

#===SAFARI=======================================================

def sarafi_url(request):
	if validaLogin(request):
		pokemons = Pokemon.objects.filter(ativo='SIM').order_by('nome')
		
		try:
			meuSafari = Amigo.objects.get(pessoa_cadastro_id=request.session['pessoaCodigo'],pessoa_amiga_id=request.session['pessoaCodigo'],ativo='SIM')
		except Exception as e:
			meuSafari = Amigo()

		try:
			indicacoesSafari = Amigo.objects.filter(pessoa_amiga_id=request.session['pessoaCodigo'],ativo='SIM').exclude(pessoa_cadastro_id=request.session['pessoaCodigo']).order_by('-data_cadastro')
		except Exception as e:
			indicacoesSafari = Amigo()


		return render_response( request,'pessoas/registersafari.html' , {'pokemons':pokemons, 'meuSafari': meuSafari, 'indicacoesSafari': indicacoesSafari} )

	else:
		return redirect('/')

def safari_adicionar(request):
	if request.method == 'POST':

		if request.POST['acao'] == 'alterar':
			amigo = Amigo.objects.get(pessoa_cadastro_id=request.session['pessoaCodigo'],pessoa_amiga_id=request.session['pessoaCodigo'],ativo='SIM')
			safari = amigo.getSafari()
			print safari.codigo
		else:
			safari = Safari() #COLOCAR PARA CRIA O OBJETO EM BRANCO
			amigo = Amigo()

		if request.POST['tipo'] != 'I DONT KNOW!':
			safari.tipo = request.POST['tipo']
		else:
			safari.tipo = 'I DONT KNOW!'	

		if request.POST['pokemon1'] != 'I DONT KNOW!' and request.POST['pokemon1'] > 0:
			safari.pokemon1_id = request.POST['pokemon1']
		else:
			safari.pokemon1_id = 1

		if request.POST['pokemon2'] != 'I DONT KNOW!' and request.POST['pokemon2'] > 0:
			safari.pokemon2_id = request.POST['pokemon2']
		else:
			safari.pokemon2_id = 1

		if request.POST['pokemon3'] != 'I DONT KNOW!' and request.POST['pokemon3'] > 0:
			safari.pokemon3_id = request.POST['pokemon3']
		else:
			safari.pokemon3_id = 1

		safari.save()

		amigo.avaliacao = 5 #AVALIACAO VAI DE 0 A 5
		amigo.descricao = 'THIS IS ME! WELCOME TO MY SAFARI!' #PADRAO SO PARA NAO DEIXAR NADA EM BRANCO
		amigo.pessoa_cadastro_id = request.session['pessoaCodigo'] #PESSOA QUE EFETUOU O CADASTRO
		amigo.pessoa_amiga_id = request.session['pessoaCodigo'] #PESSOA PARA QUEM ELA VAI CADASTRAR O SAFARI (ELA MESMA!)
		amigo.safari = safari
		amigo.tags = '#'+str(request.session['pessoaCodigo']) #PADRAO SO PARA NAO DEIXAR NADA EM BRANCO
		
		amigo.save()

		return render_response(request,'index.html',{'avisoTipo': 'alert-success', 'msg': _('Thank you. Your Safari successfully registered.')})
	else:
		return redirect('/')


#===FIM SAFARI=======================================================


#===AMIGO=======================================================

def friend_url(request):
	if validaLogin(request):
		amigos = Amigo.objects.filter(pessoa_cadastro_id=request.session['pessoaCodigo'], pessoa_amiga_id=request.session['pessoaCodigo'],ativo='SIM')

		contador = len(list(amigos))
		return render_response( request,'pessoas/friends.html' , {'amigos':amigos, 'contador': contador} )
	else:
		return redirect('/')

def friend_search(request):
	if validaLogin(request):
		if request.method == 'POST':
			textoPesquisa = request.POST['textoPesquisa'].upper().strip()
		else:
			textoPesquisa = ''

		if len(textoPesquisa) > 1:
			sql = ("SELECT pa.codigo FROM pessoas_amigo pa "
				" INNER JOIN pessoas_pessoa pesCad on pesCad.codigo = pa.pessoa_cadastro_id and pesCad.ativo = 'SIM' "
				" LEFT JOIN pessoas_safari pesSaf on pesSaf.codigo = pa.safari_id and pesSaf.ativo = 'SIM' "
				" LEFT JOIN pokemons_pokemon pok1 on pok1.codigo = pesSaf.pokemon1_id "
				" LEFT JOIN pokemons_pokemon pok2 on pok2.codigo = pesSaf.pokemon2_id "
				" LEFT JOIN pokemons_pokemon pok3 on pok3.codigo = pesSaf.pokemon3_id "
				" WHERE "
				" (pesCad.shinyvalue = '%s' OR "
				" pesCad.gameregion = '%s' OR "
				" pesCad.nativevivillon like '%s' OR "
				" pesCad.nome like '%s' OR "
				" pesCad.nickname like '%s' OR "
				" pesCad.friendcode = '%s' OR "
				" pesSaf.tipo like '%s' OR "
				" pok1.nome like '%s' OR "
				" pok2.nome like '%s' OR "
				" pok1.tags like '%s' OR "
				" pok2.tags like '%s' OR "
				" pok3.tags like '%s' OR "
				" pok3.nome like '%s') AND "
				" pa.pessoa_amiga_id = pa.pessoa_cadastro_id and pa.ativo = 'SIM' ") % (textoPesquisa, textoPesquisa,'%%'+textoPesquisa+'%%','%%'+textoPesquisa+'%%','%%'+textoPesquisa+'%%',textoPesquisa,'%%'+textoPesquisa+'%%', '%%'+textoPesquisa+'%%', '%%'+textoPesquisa+'%%', '%%'+textoPesquisa+'%%',
				'%%'+textoPesquisa+'%%','%%'+textoPesquisa+'%%','%%'+textoPesquisa+'%%')
	
			amigos = Amigo.objects.raw(sql)	
		else:	
			amigos = Amigo.objects.filter(pessoa_cadastro_id=request.session['pessoaCodigo'],ativo='SIM').order_by('data_cadastro')

		contador = len(list(amigos))
		return render_response( request,'pessoas/friends.html' , {'amigos':amigos, 'textoPesquisa': textoPesquisa, 'contador':contador} )
	else:
		return redirect('/')

def friend_amigos1(request):
	if validaLogin(request):
		try:
			pessoaCodigo = request.session['pessoaCodigo']
			amigos1 = Amigo.objects.raw("select * from pessoas_amigo where ativo = 'SIM' and descricao = 'THIS IS ME! WELCOME TO MY SAFARI!' and pessoa_cadastro_id in (select pessoa_amiga_id from pessoas_amigo where ativo = 'SIM' and pessoa_cadastro_id = %s and pessoa_amiga_id not in (select pessoa_cadastro_id from pessoas_amigo where pessoa_cadastro_id in (select pessoa_amiga_id from pessoas_amigo where pessoa_cadastro_id = %s and ativo = 'SIM') and pessoa_amiga_id = %s and ativo = 'SIM'))  LIMIT 0 , 150",[pessoaCodigo, pessoaCodigo,pessoaCodigo])[:150]
		except Exception as e:
			amigos1 = Amigo()

		return render_response( request,'pessoas/list.html' , {'titulo': 'Added Friends', 'amigos': amigos1} )
	else:
		return redirect('/')

def friend_amigos2(request):
	if validaLogin(request):
		try:
			pessoaCodigo = request.session['pessoaCodigo']
			amigos2 = Amigo.objects.raw("select * from pessoas_amigo where ativo = 'SIM' and descricao = 'THIS IS ME! WELCOME TO MY SAFARI!' and pessoa_cadastro_id in (select pessoa_cadastro_id from pessoas_amigo where ativo = 'SIM' and  pessoa_amiga_id = %s and pessoa_cadastro_id not in (select pessoa_cadastro_id from pessoas_amigo where pessoa_cadastro_id in (select pessoa_amiga_id from pessoas_amigo where pessoa_cadastro_id = %s and ativo = 'SIM' ) and pessoa_amiga_id = %s and ativo = 'SIM')) LIMIT 0 , 150",[pessoaCodigo,pessoaCodigo,pessoaCodigo])[:150]
		except Exception as e:
			amigos2 = Amigo()

		return render_response( request,'pessoas/list.html' , {'titulo': 'Added Me', 'amigos': amigos2} )
	else:
		return redirect('/')

def friend_amigos3(request):
	if validaLogin(request):
		try:
			pessoaCodigo = request.session['pessoaCodigo']
			amigos3 = Amigo.objects.raw("select * from pessoas_amigo where ativo = 'SIM' and descricao = 'THIS IS ME! WELCOME TO MY SAFARI!' and pessoa_cadastro_id in (select pessoa_cadastro_id from pessoas_amigo where ativo = 'SIM' and pessoa_cadastro_id in (select pessoa_amiga_id from pessoas_amigo where pessoa_cadastro_id = %s and pessoa_amiga_id <> %s and ativo = 'SIM') and pessoa_amiga_id = %s and ativo = 'SIM') order by data_cadastro desc LIMIT 0 , 150",[pessoaCodigo,pessoaCodigo,pessoaCodigo])[:150]
		except Exception as e:
			#raise e
			amigos3 = Amigo()

		return render_response( request,'pessoas/list.html' , {'titulo': 'Friends Reply', 'amigos': amigos3} )
	else:
		return redirect('/')

def friend_amigos4(request):

	if validaLogin(request):
		try:
			#amigos4 = Amigo.objects.raw("select * from pessoas_amigo inner join pessoa p on p. where ativo = 'SIM' and descricao = 'THIS IS ME! WELCOME TO MY SAFARI!' and pessoa_cadastro_id in (select pessoa_cadastro_id from pessoas_amigo where ativo = 'SIM' GROUP BY pessoa_cadastro_id) ORDER BY data_alteracao DESC LIMIT 0 , 120")[:120]
			amigos4 = Amigo.objects.raw("select pa.* from pessoas_amigo pa inner join pessoas_pessoa p on p.codigo = pa.pessoa_cadastro_id and p.ativo = 'SIM' where pa.pessoa_amiga_id = pa.pessoa_cadastro_id and pa.ativo = 'SIM' ORDER BY pa.data_alteracao DESC LIMIT 0 , 120")[:120]

		except Exception as e:
			amigos4 = Amigo()	

		return render_response( request,'pessoas/list.html' , {'titulo': 'Safari Updates', 'amigos': amigos4} )
	else:
		return redirect('/')

def friend_amigos5(request):
	if validaLogin(request):
		try:
			#RETIRADO PARA REFINAR O CODIGO
			amigos5 = Amigo.objects.raw('SELECT codigo FROM pessoas_amigo GROUP BY pessoa_amiga_id ORDER BY count(1) DESC')[:5]
		except Exception as e:
			amigos5 = Amigo()

		return render_response( request,'pessoas/list.html' , {'titulo': 'Ranking', 'amigos': amigos5} )
	else:
		return redirect('/')

#===FIM AMIGO=======================================================


#===POKEMON=======================================================
def pokemon_url(request):
	if validaLogin(request):
		pokemons = Pokemon.objects.filter(numero__gt=0, ativo='SIM').order_by('codigo')

		return render_response( request,'pokemons/home.html' , {'pokemons':pokemons} )
	else:
		return redirect('/')
#===FIM POKEMON=======================================================


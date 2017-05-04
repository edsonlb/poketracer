
# -*- coding: utf-8 -*-
#from pokemons.models import Pokemon
import urllib2  
import MySQLdb



response = urllib2.urlopen("http://pokemondb.net/pokedex/national") 
page_source = response.read()

# $1$ INICIO DA LINHA
# $2$ FIM DA LINHA

page_source = page_source.replace('''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>List of Pokémon (sprites gallery) | Pokémon Database</title>

	<link rel="stylesheet" href="/static/css/min/pokemondb.9.css">
	<link rel="stylesheet" href="/static/css/min/pkmn-sprites.4.css">

	<meta name="viewport" content="width=device-width, initial-scale=1">

	<meta name="description" content="A simple list of all 649 Pokémon by National Dex number, with images.">
	<link rel="canonical" href="http://pokemondb.net/pokedex/national">

	<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">
	<link rel="alternate" type="application/rss+xml" href="http://pokemondb.net/news/feed" title="The Pokemon Database newsfeed">

	<!--[if lt IE 9]>
	<script src="/static/js/html5shiv.js"></script>
	<link rel="stylesheet" href="/static/css/ie.css">
	<![endif]-->

	<script>
	var _gaq = [['_setAccount', 'UA-1974891-7'],['_trackPageview']];
	(function() {
		var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
		ga.src = 'http://www.google-analytics.com/ga.js';
		var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
	})();
	</script>
	<script async src="http://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
</head>

<body>

<header class="grid-wrapper">
	<a class="header-logo" href="/">Pokémon Database</a>

	<form method="get" action="/search" class="sitesearch-form">
		<input type="text" name="q" id="sitesearch" autocomplete="off" placeholder="Enter keywords" class="sitesearch-input">
		<button type="submit" class="sitesearch-btn">Search</button>
		<div id="sitesearch-results" class="sitesearch-results"></div>
	</form>
</header>


<nav class="main-menu grid-wrapper">
<ul class="main-menu-list">
	<li><a href="/sitemap">Pokémon data</a>
		<ul class="main-menu-sub">
			<li><a href="/pokedex">Pokédex</a>
			<li><a href="/move">Moves</a>
			<li><a href="/type">Type chart</a>
			<li><a href="/ability">Abilities</a>
			<li><a href="/item">Items</a>
			<li><a href="/evolution">Evolution chains</a>
			<li><a href="/location">Pokémon locations</a>
			<li><a href="/sprites">Sprite gallery</a>
			<li><a href="/pokedex/all">Pokémon stats</a>
		</ul>
	</li>
	<li><a href="/sitemap">Game mechanics</a>
		<ul class="main-menu-sub">
			<li><a href="/mechanics/breeding">Breeding &amp; egg groups</a>
			<li><a href="/mechanics/move-tutors">Move Tutors</a>
			<li><a href="/type/dual">Dual type chart</a>
			<li><a href="/ev">Effort Values (EVs)</a>
			<li><a href="/mechanics/natures">Natures</a>
			<li><a href="/mechanics/hidden">IVs/Personality</a>
			<li class="hr-title">Useful tools
			<li><a href="/tools/moveset-search">Moveset searcher</a>
			<li><a href="/tools/type-coverage">Type coverage checker</a>
		</ul>
	</li>
	<li><a href="/sitemap">Pokémon games</a>
		<ul class="main-menu-sub">
			<li><a href="/x-y">X &amp; Y</a>
			<li class="hr">
			<li><a href="/black-white-2">Black 2 &amp; White 2</a>
			<li><a href="/black-white">Black &amp; White</a>
			<li class="hr">
			<li><a href="/heartgold-soulsilver">HeartGold &amp; SoulSilver</a>
			<li><a href="/platinum">Platinum</a>
			<li><a href="/diamond-pearl">Diamond &amp; Pearl</a>
			<li class="hr">
			<li><a href="/emerald">Emerald</a>
			<li><a href="/firered-leafgreen">FireRed &amp; LeafGreen</a>
			<li><a href="/ruby-sapphire">Ruby &amp; Sapphire</a>
			<li class="hr">
			<li><a href="/crystal">Crystal</a>
			<li><a href="/gold-silver">Gold &amp; Silver</a>
			<li class="hr">
			<li><a href="/yellow">Yellow</a>
			<li><a href="/red-blue">Red &amp; Blue</a>
			<li class="hr">
			<li><a href="/spinoff/pokemon-bank">Pokémon Bank</a>

		</ul>
	</li>
	<li><a href="/sitemap">Community</a>
		<ul class="main-menu-sub">
			<li><a href="/pokebase/">Pokémon Q&amp;A</a>
			<li><a href="/pokebase/rmt">Pokémon Rate My Team</a>
			<li><a href="/pokebase/chat">Chat Room</a>
			<li><a href="/pokebase/meta/">Meta (Suggestion Box)</a>
		</ul>
	</li>
	<li><a href="/sitemap">Other information</a>
		<ul class="main-menu-sub">
			<li><a href="/">Pokémon News (home page)</a>
			<li><a href="/maps">Maps/Puzzles</a>
			<li><a href="/events">Pokémon events &amp; passwords</a>
			<li><a href="/etymology">Pokémon name origins</a>
			<li><a href="/glossary">Pokémon dictionary</a>
			<li><a href="/about">About this site</a>
			<li class="hr-title">Quick links
			<li><a href="/pokedex/national">Full Pokémon list</a>
			<li><a href="/pokedex/game/black-white-2">Black 2 &amp; White 2 Pokédex</a>
			<li><a href="/pokedex/game/black-white">Black &amp; White Pokédex</a>
		</ul>
	</li>
</ul>
</nav>

<article class="main-content grid-wrapper">

<h1>List of Pokémon</h1>

<ul class="nav-list island">
	<li class="title">Jump to</li>
	<li><a href="#gen-1">Generation 1</a></li>
	<li><a href="#gen-2">Generation 2</a></li>
	<li><a href="#gen-3">Generation 3</a></li>
	<li><a href="#gen-4">Generation 4</a></li>
	<li><a href="#gen-5">Generation 5</a></li>
	<li><a href="#gen-6">Generation 6</a></li>
</ul>

<div class="intro">
	<p>This is the complete <strong>National Pokédex</strong> for Generation V (up to <a href="/black-white">Black &amp; White</a>),
		which lists every one of the 649 Pokémon discovered so far.</p>
	<p>Click a pokemon's name to see its detailed Pokédex page, or click a type to see other pokemon of the same type. See also:
		<a href="/pokedex/all">Pokédex with stats</a>.</p>

		<div class="share-icons">
		<i class="share-blurb">Share this page:</i>
		<a href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fpokemondb.net%2Fpokedex%2Fnational&amp;t=List+of+Pok%C3%A9mon+%28sprites+gallery%29"
			class="icon-facebook" title="Share on Facebook" target="_blank">Facebook</a>
		<a href="http://twitter.com/share?url=http%3A%2F%2Fpokemondb.net%2Fpokedex%2Fnational&amp;text=List+of+Pok%C3%A9mon+%28sprites+gallery%29+%28via+%40pokemondb%29+"
			class="icon-twitter" title="Tweet this page" target="_blank">Twitter</a>
		<a href="https://plus.google.com/share?url=http%3A%2F%2Fpokemondb.net%2Fpokedex%2Fnational"
			class="icon-gplus" title="Share on Google+" target="_blank">Google+</a>
		<a href="mailto:?subject=Pokemon+link&amp;body=Check+out+this+cool+Pokemon+page%21%0A%0AList+of+Pok%C3%A9mon+%28sprites+gallery%29%0Ahttp%3A%2F%2Fpokemondb.net%2Fpokedex%2Fnational"
			class="icon-email" title="Email this page" target="_blank">Email</a>
	</div>
	</div>

<div class="ad-responsive">
	<style>
  .adresp-leaderboard { width: 320px; height: 50px; margin-left: -5px; }
  @media(min-width: 795px) { .adresp-leaderboard { width: 728px; height: 90px; } }
</style>
<!-- Pokemon [responsive] - leaderboard, text -->
<ins class="adsbygoogle adresp-leaderboard"
  style="display:inline-block"
  data-ad-client="ca-pub-4942990752504243"
  data-ad-slot="5568695004"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>


<div class="infocard-tall-list">

	<hr>
	<h2 id="gen-1">Generation 1 Pokémon</h2>''', '')


page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgRBY n', ' $1$ ')
page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgGSC n', ' $1$ ')
page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgRSE n', ' $1$ ')
page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgDPP n', ' $1$ ')
page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgBW n', ' $1$ ')
page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgXY n', ' $1$ ')
page_source = page_source.replace('href="/pokedex/', 'nome_pokemon=')
page_source = page_source.replace('href="/pokedex/', 'nome_pokemon=')
page_source = page_source.replace('></a><br><small>', 'numero_pokemon=')
page_source = page_source.replace('</small><br><a class="ent-name', ' ')
page_source = page_source.replace('</a><br><small class="aside"><a href="', ' " ')
page_source = page_source.replace('" /type/', ' $33$ ')
page_source = page_source.replace('</a></small></span>', ' $5$ ') #FIM DA LINHA
page_source = page_source.replace('</a> &middot; <a href="', ' $segundotipo$ ') #SEGUNDO TIPO DE POKEMON
page_source = page_source.replace('" class="itype', ' $3$ ') #SEGUNDO TIPO DE POKEMON


pagepokemons = open('pokemonstxt.txt','w')
pagepokemons.write(page_source)

pagepokemons.close()

pagepokemons = open('pokemonstxt.txt','r')



# class Pokemon:
# 	numero = ''
# 	nome = ''
# 	tipo = ''
# 	def __init__(self, numero, nome, tipo):
# 		self.numero = numero
# 		self.nome = nome

pokemons = ()

db = MySQLdb.connect(host="201.76.55.146", user="celuladigital15", passwd="CDS1005", db="celuladigital15")
cursor = db.cursor()

cursor.execute("TRUNCATE pokemons_pokemon")
db.commit()

cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://127.0.0.1:8000/media/img/idontknow.png','http://poketracer.com', 0, 'I DONT KNOW!', 'I DONT KNOW!')")
db.commit()

for linha in pagepokemons.readlines():
	POSICAO1 = linha.find('nome_pokemon=')
	POSICAO2 = linha.find('"numero_pokemon')
	nome_pokemon = linha[POSICAO1:POSICAO2].replace('nome_pokemon=', '')

	POSICAO = linha.find('numero_pokemon=#')
	numero_pokemon = linha[POSICAO:POSICAO+19].replace('numero_pokemon=#', '')

	POSICAO1 = linha.find('$33$')
	POSICAO2 = linha.find('$3$')
	tipo_pokemon1 = linha[POSICAO1:POSICAO2].replace('$33$', '')

	POSICAO1 = linha.find('$segundotipo$')
	POSICAO2 = linha.find('$5$')
	tipo_pokemon2 = linha[POSICAO1:POSICAO2]

	POSICAO1 = tipo_pokemon2.find('$3$')
	POSICAO2 = tipo_pokemon2.find('">')
	tipo_pokemon2 = tipo_pokemon2[POSICAO1:POSICAO2].replace('$3$  ', '')



	if len(nome_pokemon.strip()) > 2:

		print "========="
		print nome_pokemon.strip()
		print numero_pokemon.strip()
		print tipo_pokemon1.strip()
		if len(tipo_pokemon2.strip()) > 2:
			print tipo_pokemon2.strip()

		if nome_pokemon.strip() == 'deoxys':
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/deoxys-normal.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'DEOXYS', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/deoxys-attack.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'DEOXYS ATTACK', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/deoxys-defense.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'DEOXYS DEFENSE', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/deoxys-speed.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'DEOXYS SPEED', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
		elif nome_pokemon.strip() == 'wormadam':
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/wormadam-plant.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'WORMADAM PLANT', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/wormadam-sandy.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'WORMADAM SANDY', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/wormadam-trash.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'WORMADAM TRASH', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
		elif nome_pokemon.strip() == 'rotom':
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/rotom-normal.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'ROTOM', 'ELECTRIC GHOST')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/rotom-heat.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'ROTOM HEAT', 'ELECTRIC FIRE')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/rotom-wash.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'ROTOM WASH', 'ELECTRIC WATER')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/rotom-frost.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'ROTOM FROST', 'ELECTRIC ICE')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/rotom-fan.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'ROTOM FAN', 'ELECTRIC FLYING')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/rotom-mow.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'ROTOM MOW', 'ELECTRIC GRASS')")
		elif nome_pokemon.strip() == 'giratina':
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/giratina-altered.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'GIRATINA ALTERED', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/giratina-origin.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'GIRATINA ORIGIN', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
		elif nome_pokemon.strip() == 'shaymin':
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/shaymin-land.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'SHAYMIN LAND', 'GRASS')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/shaymin-sky.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'SHAYMIN SKY', '	GRASS FLYING')")
		elif nome_pokemon.strip() == 'darmanitan':
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/darmanitan-standard.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'DARMANITAN', 'FIRE')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/darmanitan-zen.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'DARMANITAN ZEN', 'FIRE PSYCHIC')")
		elif nome_pokemon.strip() == 'meloetta':
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/meloetta-aria.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'MELOETTA ARIA', 'NORMAL PSYCHIC')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/meloetta-pirouette.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'MELOETTA PIROUETTE', 'NORMAL FIGHTING')")
		elif nome_pokemon.strip() == 'aegislash':
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/aegislash-blade.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'AEGISLASH BLADE', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
			cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/aegislash-shield.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", 'AEGISLASH SHIELD', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
		else:
			try:
				teste = urllib2.urlopen(urllib2.Request('http://img.pokemondb.net/artwork/'+nome_pokemon.strip().lower()+'.jpg'))
				cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/"+nome_pokemon.strip().lower()+".jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", '"+nome_pokemon.strip().upper()+"', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
			except Exception as e: 
				try:
					teste = urllib2.urlopen(urllib2.Request('http://img.pokemondb.net/artwork/dream/'+nome_pokemon.strip().lower()+'.png'))
					cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/dream/"+nome_pokemon.strip().lower()+".png','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", '"+nome_pokemon.strip().upper()+"', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
				except Exception as e:
					try:
						teste = urllib2.urlopen(urllib2.Request('http://img.pokemondb.net/artwork/'+nome_pokemon.strip().lower()+'-male.jpg'))
						cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://img.pokemondb.net/artwork/"+nome_pokemon.strip().lower()+"-male.jpg','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", '"+nome_pokemon.strip().upper()+"', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")
					except Exception as e:
						cursor.execute("INSERT INTO pokemons_pokemon (pokecode, foto, pokedex_link, numero,nome,tags) VALUES ('#','http://127.0.0.1:8000/media/img/idontknow.png','http://pokemondb.net/pokedex/"+nome_pokemon.strip().lower()+"', "+numero_pokemon.strip()+", '"+nome_pokemon.strip().upper()+"', '"+tipo_pokemon1.strip().upper() +" "+tipo_pokemon2.strip().upper()+"')")


		db.commit()

	
pagepokemons.close()
cursor.close()
db.close()





# //ANDAR LINHA A LINHA, SE NAO TIVER MARCACAO INICIAL, PULA LINHA
# //FOR AONDE ESTIVER A PRIMEIRA MARCACAO
# //page_source.find('$1$') OU  string.index(character)
# //VC ANDA EM UM FOR ATE O CARACTERE DE MARCACAO FINAL
# //VAI ADICIONANDO OS CARACTERES NA MESMA POSICAO DO OBJETO
# pokemon = Pokemon()
# pokemon.numero.append(page_source[4])
# pokemons = []
# pokemons.add(pokemon)

# //PASSA OBJETO POR OBJETO NO POKEMONS E ADICIONA NO BANCO DE DADOS


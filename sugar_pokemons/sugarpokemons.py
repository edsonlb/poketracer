import urllib2  

# class Pokemon():
# 	numero
# 	nome
# 	tipo

response = urllib2.urlopen("http://pokemondb.net/pokedex/national") 
page_source = response.read()

# $1$ INICIO DA LINHA
# $2$ FIM DA LINHA

# page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgRBY n', ' $1$ ')
# page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgGSC n', ' $1$ ')
# page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgRSE n', ' $1$ ')
# page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgDPP n', ' $1$ ')
# page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgBW n', ' $1$ ')
# page_source = page_source.replace('<span class="infocard-tall "><a class="pkg " data-sprite=" pkgXY n', ' $1$ ')
# page_source = page_source.replace('href="/pokedex/', 'nome_pokemon=')
# page_source = page_source.replace('></a><br><small>', 'numero_pokemon=')
# page_source = page_source.replace('</small><br><a class="ent-name', ' ')
# page_source = page_source.replace('</a><br><small class="aside"><a href="', ' " ')
# page_source = page_source.replace('</a></small></span>', ' $2$ ') #FIM DA LINHA
# page_source = page_source.replace('</a> &middot; <a href="', ' $segundotipo$ ') #SEGUNDO TIPO DE POKEMON
# page_source = page_source.replace('class="itype', '') #SEGUNDO TIPO DE POKEMON


# pagepokemons = open('/home/lucaslinux/projetos/poketracer/sugar_pokemons/pokemons.txt','w')
# pagepokemons.write(page_source)

# pagepokemons.close()

pagepokemons = open('/home/lucaslinux/projetos/poketracer/sugar_pokemons/pokemons.txt','r')

pokemons = ()
for linha in pagepokemons.readlines():
	POSICAO1 = linha.find('nome_pokemon=')
	POSICAO2 = linha.find(' $2$ ')
	pokemon = linha[POSICAO1:POSICAO2]
	pokemon = pokemon.replace('nome_pokemon=', '')
	print linha
	print POSICAO1
	print POSICAO2
	print pokemon
	break

	
pagepokemons.close()

print "-=============="
print POSICAO1
print POSICAO2
print pokemon






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


# Projeto Tutorial Scrapy
Esse projeto é baseado no tutorial da documentação oficial do Scrapy https://docs.scrapy.org/en/latest/intro/tutorial.html

## Criando um novo projeto Scrapy
```sh
$ scrapy startproject <nome-do-projeto>
```

## Criando uma spider
Criar um novo arquivo .py dentro da pasta `spiders` e editar usando a [spider desse projeto](raspador2/spiders/forbes.py) como referência 
ou essa [seção do tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html#our-first-spider)

## Rodando uma spider
Após criar sua spider, você pode rodar ela com o comando
```sh
$ scrapy crawl <nome-da-spider>
```
o nome da spider vai ser a sua propriedade `name`, [aqui um exemplo](raspador2/spiders/forbes.py#L4).

Esse comando só ira mostrar o log da operação. 

Para salvar o resultado da raspagem em um arquivo, o comando é:
```sh
$ scrapy crawl <nome-da-spider> -O <nome-do-arquivo>
```

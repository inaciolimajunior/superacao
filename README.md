# SUPERAÇÃO
Projeto apresentando o teste para a empresa Super Escola, que propôs a criação de um projeto para a listagem e respostas de exercícios cadastrados.

## Pré-Requisitos
- Python 3.9.2
- Django 4.0.1
- Django Rest Framework 3.13.1
- Django CkEditor 6.2.0

## Instalação
- Faça o download do código deste projeto e descompacte--o
- Realizar o download da versão do Python correspondente ao seu equipamento: https://www.python.org/downloads/
- Efetuar a instalação do Python segundo instruções do fornecedor
- Abrir o terminal de comandos (shell, terminal, cmd...) e efetuar os seguintes comandos:
- - pip install django
- - pip install django-ckeditor
- - pip install djangorestframework
- Mudar o diretório atual do terminal para o diretório onde o projeto fora descompactado e efetuar o seguinte comando:
- - python manage.py runserver
- Acessar o sistema pelo link http://localhost:8000/admin e efetuar o login com usuário: admin e senha: admin ou
- Acessar a api através do link http://localhost:8000/api

## Testes
O projeto conta com 05 testes automatizados a saber:

| Nome  | Descrição  |
| ------------ |---------------|
| test_exercicios_listar | Listagem de Exercícios |
| test_resposta_certa | Usuário escolhendo a alternativa correta o exercício |
| test_resposta_errada | Usuário escolhendo a alternativa errada |
| test_resposta_invalida | Usuário escolhendo uma alternativa inválida |
| test_resposta_embranco | Usuário respondendo em branco |

Para efetuar os testes abra um segundo terminal de comando, mude a pasta para a pasta do projeto e efetue o seguinte comando:
#### python manage.py test

## Autor
###Inácio Pereira Lima Júnior
####Desenvolvedor Full Stack Java/Python

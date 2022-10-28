# iClinic Python Challenge

Este projeto é a minha solução para o [desafio de Python da iClinic](https://github.com/iclinic/iclinic-python-challenge).

## Arquivos do projeto

```text
.
|--- src
|    |--- datasets
|    |    |--- patients.csv
|    |--- binary_tree.py
|    |--- dataset.py
|    |--- flask_restful_api.py
|--- tests
|    |--- test_flask_restful_api.py
|--- LICENSE
|--- README.md
```

## Instalção

> Se você estiver utilizando o Linux, o Python já estará pré-instalado, apenas certifique-se de ter a versão 3.x.x.  
> O `pip` será utilizado apenas para instalar os pacotes necessários.

### Pré-requisitos

- [Python 3+](https://www.python.org)
- [pip](https://pypi.org/project/pip)
- [Virtualenv](https://virtualenv.pypa.io)
- [Flask](http://flask.pocoo.org)
- [Flask-RESTful](https://flask-restful.readthedocs.io)
- [pytest](https://docs.pytest.org)

### Instruções (informações)

> A seguir estão as informações do que é necessário para executar o projeto, mas na próxima seção estão os comandos referentes a essas instruções.  

1. Clone ou faça download deste repositório
2. Abra o **Terminal** e entre no diretório raiz deste repositório
3. Crie um ambiente virtual no qual o projeto será executado
4. Entre no diretório criado pelo ambiente virtual
5. Ative o ambiente virtual
6. Instale os pacotes: `flask`, `Flask-RESTful` e `pytest`
7. Mova os diretórios **src** e **tests** da raiz do repositório para dentro do diretório criado pelo ambiente virtual
8. Tudo pronto! :-)

### Instruções (comandos)

> Para executar os comandos abaixo, é necessário ter o "pip" e o "virtualenv" instalados.

```bash
# Instalar o "pip3"
$ sudo apt update
$ sudo apt install python3-pip

# Instalar o "virtualenv"
$ [sudo] pip3 install virtualenv
```

```bash
# 1. e 2. não precisam de comandos

# 3. Crie um ambiente virtual (vou chamá-lo de: "flask-restful-api")
$ virtualenv -p python3 flask-restful-api

# 4. Entre no diretório criado pelo ambiente virtual
$ cd flask-restful-api

# 5. Ative o ambiente virtual
$ source bin/activate

# 6. Instale os pacotes: "flask", "Flask-RESTful" e "pytest"
$ pip3 install flask Flask-RESTful pytest

# 7. Mova os diretórios "src" e "tests" da raiz do repositório
#    para dentro do diretório criado pelo ambiente virtual
$ mv ../src ./
$ mv ../tests ./

# 8. Tudo pronto!
```

## Modo de uso

### Executando a aplicação

Através do **Terminal**, entre no diretório `src` e execute o comando abaixo:

```bash
$ python3 flask_restful_api.py
```

Com a aplicação disponível, execute o seguinte comando para visualizar os **_endpoints_** disponíveis:

```bash
$ curl -X GET -H "Content-Type: application/json" http://0.0.0.0:5000/endpoints
```

### Testando a aplicação

Através do **Terminal**, entre no diretório `tests` e execute o comando abaixo:

```bash
$ pytest
```

## Autor

Eduardo S. Marçal

## Contact

[LinkedIn](https://linkedin.com/in/eduardosmarcal)  
[Twitter](https://twitter.com/eduardosmarcal_)

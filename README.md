# Star War API


Uma API feita com Django Rest Framework que puxa dados do https://swapi.dev


## Atualmente contém os dados de:


<ul>
<li>Planetas</li>
<li>Pessoas</li>
</ul>

## Descrição

-Ao acessar um dos links ele vai puxar todo o banco de dados do swapi do tema referente e adicionar ao banco de dados o que já não estiver
Depois vai exibir o conteudo do swapi, caso a conexão não seja estabelecida, irá mostrar o que tem no banco de dados local

-É possivel procurar usando /search/"nome", exemplo:(/planets/search/Malastare/)
irá exibir os resultados da pesquisa equivalente no swapi e salvar no banco de dados local os dados ainda não salvos.

## Pré-requisitos
   <ul>
   <li>Docker</li>
   <li>Python</li>
   </ul>

## Instruções de uso

### baixe e execute o projeto utilizando o comando:

    docker run -p 8000:8000 ttrema/swapiapidb
   
### Depois acesse no:

    http://localhost:8000/

## Outra opção:

 - Caso não queira usar o docker, use o metodo abaixo:

### Crie e ative um virtual environment:

    Windows:
        Crie a venv usando o comando python -m venv nome_da_venv (exemplo: python -m venv venv).
        Ative a venv usando o comando .\nome_da_venv\Scripts\activate (exemplo: .\venv\Scripts\activate).

    Linux e macOS:
        Crie a venv usando o comando python3 -m venv nome_da_venv (exemplo: python3 -m venv venv).
        Ative a venv usando o comando source nome_da_venv/bin/activate (exemplo: source venv/bin/activate).

### Use o comando:

    pip install -r requirements.txt

### Use o comando:

    python manage.py runserver

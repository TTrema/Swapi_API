Uma API feita com Django Rest Framework que pega seus dados do https://swapi.dev

Atualmente contém os dados de:

-Planetas
-Pessoas

-Ao acessar um dos links ele vai puxar todo o banco de dados do swapi do tema referente e adicionar ao banco de dados o que já não estiver
Depois vai exibir o conteudo do swapi, caso a conexão não seja estabelecida, ira mostar o que tem no banco de dados local

-É possivel procurar usando /search/"nome", exemplo:(/planets/search/Malastare/)
Ira exibir a pesquisa equivalente no swapi e salvar no banco de dados local tudo que não tiver.
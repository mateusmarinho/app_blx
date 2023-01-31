# App BLX

Treinamento com FastAPI.

App para anúncio e venda de produtos na vizinhança.

## Funcionalidades
* Qualquer pessoa poderá anunciar produtos
* Qualquer pessoa poderá fazer pedidos dos produtos anunciados
* Uma pessoa tem:
    * id
    * nome
    * telefone (whatsapp)
    * senha
* Um produto tem:
    * id
    * nome
    * detalhamento
    * preço
    * disponibilidade (sim/não)
    * fotos (?)
* Um pedido tem:
    * Produto
    * Pessoa que está pedindo
    * Quantidade
    * Local de entrega
    * Entrega ou retirada
    * Observações 
* Cada usuário terá uma lista de pedidos recebidos (minhas vendas) 
e pedidos feitos (minhas compras)
* O pedido deverá ser aceito pelo vendedor
* O comprador poderá acompanhar seus pedidos
    * Status (Feito, Aceito, A caminho, Finalizado, Cancelado)

## Arquitetura e Ferramentas
* Python + FastAPI
* API REST
* Validação de dados com Pydantic
* Banco de dados: PostgreSQL e/ou MongoDB
* Docker para o PostgreSQL
* MVC
* DDD (Domain Driven Design) e Arquitetura Limpa

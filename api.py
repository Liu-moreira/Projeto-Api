from flask import Flask, request

app = Flask(__name__)


# Altera uma configuração do Flask que permite exibir e 
# retornar caracteres do utf-8 sem quebrá-lo, podendo passar
# acentuações e cedilhas sem problemas
app.config['JASON_AS_ASCII']=False


@app.route("/")
def route():
    return "<h1>Projeto API</h1>"

print('====================')
print('API Livros Espíritas')
print('====================')

# Criação do Banco de dados
livros_dados={
    1: {
        'id': 1,
        'titulo': 'O que é o espiritismo',
        'autor': 'Allan Kardec'
    },
    2: {
        'id': 2,
        'titulo': 'Laços Eternos',
        'autor': 'Zibia Gasparetto'
    }
}

# Criação do método para retornar como resposta os livros da 
# fonte de dados:
def response_livros():
    return {'livros': list(livros_dados.values())}


# Criação de uma rota e de uma função para retornar os livros
# via API:
@app.route('/livros')
def list_livros():
    return response_livros()

# Criação de uma rota e função de inclusão de novos livros:
@app.route('/livros', methods=['POST'])
def incluir_livro():
    # Criação do corpo:
    body = request.json
    # Primeiro, para que sempre crie um id a cada novo livro 
    # incluído, é capturado todos os ids existentes em uma
    # lista:
    ids = list(livros_dados.keys())
    if ids:
        novo_id = ids[-1] + 1
    else:
        novo_id = 1
    # Atualizar o dicionário de livros:
    livros_dados[novo_id] = {
        'id': novo_id,
        'titulo': body['titulo'],
        'autor': body['autor']
    }
    return response_livros()


# Criação de um código para executar a nossa aplicação:
# app.run(debug=True)
# debug=True é útil para que se consiga ativar o modo
# debug, ou seja, sempre que editar algum código no
# arquivo e salvá-lo, a aplicação será 
# automaticamente atualizada.
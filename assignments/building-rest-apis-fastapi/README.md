# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda os fundamentos de APIs REST construindo uma API de biblioteca com FastAPI. Você vai praticar rotas HTTP, operações CRUD, validação de dados e respostas com códigos de status apropriados.

## 📝 Tasks

### 🛠️ Criar a Aplicação e as Rotas de Leitura

#### Descrição
Configure e execute uma aplicação FastAPI para uma pequena biblioteca. Comece verificando se a API está ativa e permitindo consultar os livros cadastrados.

#### Requisitos
O programa concluído deve:

- Instalar as dependências `fastapi` e `uvicorn`.
- Criar uma aplicação FastAPI com o título `Book Library API`.
- Disponibilizar `GET /health`, que retorna `{"status": "ok"}`.
- Disponibilizar `GET /books`, que retorna uma lista de livros com identificador, título e autor.
- Incluir pelo menos dois livros iniciais armazenados em memória.
- Permitir iniciar o servidor com `uvicorn main:app --reload` e acessar a documentação interativa em `/docs`.

### 🛠️ Implementar as Operações CRUD

#### Descrição
Adicione rotas para consultar, cadastrar, atualizar e remover livros. Use os métodos HTTP apropriados e mantenha os dados em memória enquanto o servidor estiver em execução.

#### Requisitos
O programa concluído deve:

- Disponibilizar `GET /books/{book_id}` para consultar um livro pelo identificador.
- Disponibilizar `POST /books` para cadastrar um livro e atribuir a ele um identificador único.
- Disponibilizar `PUT /books/{book_id}` para atualizar o título e o autor de um livro existente.
- Disponibilizar `DELETE /books/{book_id}` para remover um livro existente.
- Retornar `201 Created` ao cadastrar um livro e `204 No Content` ao removê-lo com sucesso.
- Retornar `404 Not Found` quando uma rota de consulta, atualização ou remoção receber um identificador inexistente.
- Confirmar que os livros cadastrados, atualizados ou removidos também aparecem corretamente em `GET /books`.

### 🛠️ Validar Dados e Testar a API

#### Descrição
Valide os dados enviados para cadastrar ou atualizar livros e teste os diferentes resultados das rotas usando a documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Usar modelos Pydantic para os dados de entrada de cadastro e atualização.
- Exigir título com 1 a 100 caracteres e autor com 1 a 80 caracteres.
- Retornar `422 Unprocessable Entity` para dados que não atendam aos limites de validação.
- Testar em `/docs` um cadastro válido, uma consulta por identificador, uma atualização, uma remoção e ao menos uma entrada inválida.
- Verificar que operações feitas em `/docs` produzem os códigos de status e os resultados esperados.

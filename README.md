# 📝 To-Do List API

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-6.0%2B-092E20?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/Django_REST-Framework-ff1709?style=for-the-badge&logo=django)
![JWT](https://img.shields.io/badge/JWT-Auth-black?style=for-the-badge&logo=json-web-tokens)

#### Projeto de estudo de uma API REST desenvolvida com Django REST Framework, utilizando autenticação por Token, JWT e Session.

---

## 📖 Sobre o Projeto

Este projeto consiste em uma aplicação backend simples para gerenciamento de tarefas (To-Do), desenvolvida com o
objetivo de estudar e praticar conceitos do Django REST Framework, como:

- **Autenticação Multi-camadas:** Token, JWT e Session.
- **Permissões Granulares:** Diferenciação entre Admins e Usuários comuns.
- **Isolamento de Dados:** Cada usuário acessa estritamente seus próprios recursos.
- **Otimização de API:** Paginação, filtros dinâmicos e ordenação.

---

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework:** Django & Django REST Framework
- **Autenticação:** SimpleJWT & DRF Token
- **Filtros:** Django-Filter
- **Banco de Dados:** SQLite (Padrão) / PostgreSQL (Suportado)

---

## 🔐 Autenticação

### 1️⃣ JWT (SimpleJWT) - Recomendado

Ideal para frontends modernos (React, Vue, Mobile).

| Método          | Endpoint                   | Body                                     |
|:----------------|:---------------------------|:-----------------------------------------|
| **Obter Token** | POST `/api/token/`         | `{"username": "...", "password": "..."}` |
| **Refresh**     | POST `/api/token/refresh/` | `{"refresh": "..."}`                     |
| **Verify**      | POST `/api/token/verify/`  | `{"token": "..."}`                       |

- **Header para requisições**: Authorization: Bearer <seu_token_de_acesso>

### 2️⃣ Token Authentication (DRF)

Simples e persistente, ideal para integrações via script.

- **Gerar Token**: POST `/api-token-auth/`
- **Body**:
    ```json
    {
     "username": "user", "password": "senha"
     }
     ```
- **Header**: Authorization: Token <seu_token>

### 3️⃣ Session Authentication

Utilizado para acesso via navegador (Browsable API).

- **Login**: `/api-auth/login/`

---

## 🚀 Endpoints da API

### 👤 Usuários (`api/v1/users/`)

🛑 **Acesso Restrito**: Apenas administradores (IsAdminUser) podem gerenciar usuários.

| Método | Endpoint              | Descrição                                       |
|:-------|:----------------------|:------------------------------------------------|
| GET    | `/api/v1/users/`      | Lista todos os usuários (com filtros/ordenação) |
| POST   | `/api/v1/users/`      | Cria um novo usuário                            |
| GET    | `/api/v1/users/{id}/` | Detalhes de um usuário específico               |
| PUT    | `/api/v1/users/{id}/` | Atualiza um usuário                             |
| DELETE | `/api/v1/users/{id}/` | Remove um usuário                               |

- **Filtros Disponíveis**: name, email, is_staff, is_active, date_joined.

---

### ✅ Tarefas (`api/v1/tasks/`)

🔒 **Privacidade**: Usuários autenticados acessam apenas suas próprias tasks.

### Modelo de Dados

| Campo     | Tipo    | Detalhes                              |
|:----------|:--------|:--------------------------------------|
| id        | Integer | PK, Automático                        |
| titulo    | String  | Obrigatório (Max 64 chars)            |
| descricao | String  | Opcional                              |
| status    | String  | pendente ou concluido                 |
| user      | FK      | Definido automaticamente pelo request |

### Operações:

**1. Listar Tarefas**

- **Endpoint**: GET `/api/v1/tasks/`
- **Exemplo**: `/api/v1/tasks/?status=pendente&ordering=-criada_em`

**2. Criar Tarefa**

- **Endpoint**: POST `/api/v1/tasks/`
- **Body**:
    ```json
    {
      "titulo": "Aprender Docker", "descricao": "...", "status": "pendente"
    }
    ```
- **Nota**: Não envie o campo user, o sistema o identifica pelo token(se enviado será ignorado).

**3. Atualizar e Deletar**

- **Atualizar**: PUT/PATCH `/api/v1/tasks/{id}/`
- **Deletar**: DELETE `/api/v1/tasks/{id}/`

---

## 📄 Paginação

A API implementa paginação para performance.

- **Tamanho da página**: 3 itens (configurável).
- **Parâmetro**: `?page=X`

**Exemplo de Resposta**:

```json
{
  "count": 12,
  "next": "http://api/v1/tasks/?page=3",
  "previous": "http://api/v1/tasks/?page=1",
  "results": [
    {
      "id": 4,
      "titulo": "Task 04",
      "status": "pendente"
    }
  ]
}
```

---

## 🧠 Engenharia e Boas Práticas

Este projeto não é apenas um CRUD, mas uma demonstração de arquitetura limpa dentro do Django:

- ✅ <u>Security First</u>: O campo user é injetado via `perform_create`, impedindo que um usuário crie tasks para
  terceiros.

- ✅ <u>Queryset Isolation</u>: Sobrescrita do `get_queryset` garante que dados não vazem entre usuários.

- ✅ <u>Versionamento</u>: Namespace `/api/v1/` preparado para evoluções futuras.

- ✅ <u>Clean Code</u>: Uso extensivo de ViewSets e Routers para reduzir código boilerplate.

## 💻 Como Rodar Localmente

### 🔹 <u>Opção 1: Utilizando Poetry (recomendado)</u>

### Clone o repositório

```bash
  git clone https://github.com/seu-usuario/todo-api.git  
  cd todo-api
```

### Instale as dependências

```bash
  poetry install
```

### Ative o ambiente virtual

```bash
  poetry shell
```

### Execute as migrações

```bash
  python manage.py migrate
```

### Crie um superusuário

```bash
  python manage.py createsuperuser
```

### Rode o servidor

```bash
  python manage.py runserver
```

---

### 🔹 <u>Opção 2: Sem Poetry (utilizando venv e pip)</u>

### Clone o repositório

```bash
  git clone https://github.com/seu-usuario/todo-api.git  
  cd todo-api
```

### Crie um ambiente virtual

```bash
  python -m venv .venv
```

### Ative o ambiente virtual

**Linux/Mac:**

```bash
  source .venv/bin/activate
```

**Windows:**

```bash
  .venv\Scripts\activate
```

### Instale as dependências

```bash
  pip install -r requirements.txt
```

### Execute as migrações

```bash
  python manage.py migrate
```

### Crie um superusuário

```bash
  python manage.py createsuperuser
```

### Rode o servidor

```bash
  python manage.py runserver
```

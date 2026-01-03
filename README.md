# 📘 To-do API — Documentação

#### Este é um projeto de estudo de API REST desenvolvida com **Django REST Framework**, com autenticação por **Token**, **JWT** e **Session**.

 ---

## 🔐 Autenticação

A API suporta **três métodos** de autenticação:

### 1️⃣ Token Authentication (DRF)

#### Obter token:

**POST** `/api-token-auth/`

**Request:**

 ```json
 {
  "username": "user",
  "password": "senha"
}
 ```

**Response:**

 ```json
 {
  "token": "abc123..."
}
 ```

**Header::**

 ```
 Authorization: Token abc123...
 ```

 ---

### 2️⃣ JWT (SimpleJWT)

#### Obter token:

**POST** `/api/token/`

 ```json
 {
  "username": "user",
  "password": "senha"
}
 ```

**Response:**

 ```json
 {
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
 ```

**Header:**

 ```
 Authorization: Bearer jwt_access_token
 ```

#### Refresh:

**POST** `/api/token/refresh/`

#### Verify:

**POST** `/api/token/verify/`

 ---

### 3️⃣ Session Authentication

- Browsable API
- Login em `/api-auth/login/`

 ---

## 👤 Usuários (`/api/v1/users/`)

🔒 **Acesso restrito a administradores (`IsAdminUser`)**

### Campos expostos

- `id`
- `name`
- `email`
- `date_joined` *(read-only)*
- `tasks` *(relacionamento 1:N)*

 ---

### Endpoints

#### 📄 Listar usuários

**GET** `/api/v1/users/`

**Filtros:**

- `name`
- `email`
- `is_staff`
- `is_active`
- `date_joined`

**Ordenação:**

- `name`
- `email`
- `is_staff`
- `is_active`
- `date_joined`

**Exemplo:**

 ```
 /api/v1/users/?is_active=true&ordering=-date_joined
 ```

 ---

#### 🔍 Detalhar usuário

**GET** `/api/v1/users/{id}/`

 ---

#### ➕ Criar usuário

**POST** `/api/v1/users/`

 ```json
 {
  "name": "Derick",
  "email": "derick@email.com",
  "password": "123456"
}
 ```

 ---

#### ✏️ Atualizar usuário

**PUT / PATCH** `/api/v1/users/{id}/`

 ---

#### ❌ Deletar usuário

**DELETE** `/api/v1/users/{id}/`

 ---

## ✅ Tasks (`/api/v1/tasks/`)

🔒 **Usuário autenticado só acessa suas próprias tasks**

### Modelo Task

| Campo       | Tipo     | Observação               |
 |-------------|----------|--------------------------|
| `id`        | integer  | automático               |
| `titulo`    | string   | máx 64                   |
| `descricao` | string   | opcional                 |
| `status`    | enum     | `pendente` / `concluido` |
| `criada_em` | datetime | automático               |
| `user`      | FK       | definido automaticamente |

 ---

### Endpoints

#### 📄 Listar tasks

**GET** `/api/v1/tasks/`

**Filtros:**

- `status`
- `criada_em`

**Ordenação:**

- `status`
- `criada_em`

**Padrão:**

 ```
 ordering=-criada_em
 ```

**Exemplo:**

 ```
 /api/v1/tasks/?status=pendente&ordering=criada_em
 ```

 ---

#### 🔍 Detalhar task

**GET** `/api/v1/tasks/{id}/`

 ---

#### ➕ Criar task

**POST** `/api/v1/tasks/`

 ```json
 {
  "titulo": "Estudar DRF",
  "descricao": "Documentar a API",
  "status": "pendente"
}
 ```

📌 O campo `user` é definido automaticamente pelo usuário autenticado.

 ---

#### ✏️ Atualizar task

**PUT / PATCH** `/api/v1/tasks/{id}/`

 ---

#### ❌ Deletar task

**DELETE** `/api/v1/tasks/{id}/`

 ---

## 📄 Paginação

A API utiliza paginação baseada em número de páginas (**PageNumberPagination**).

### Configuração

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3
}
```

### Funcionamento

- Cada resposta retorna **3 registros por página**
- Parâmetro de paginação: `page`

### Exemplo de requisição

```http
GET /api/v1/tasks/?page=2
```

### Estrutura da resposta paginada

```json
{
  "count": 10,
  "next": "http://localhost:8000/api/v1/tasks/?page=3",
  "previous": "http://localhost:8000/api/v1/tasks/?page=1",
  "results": [
    {
      "id": 4,
      "titulo": "Exemplo",
      "descricao": "",
      "status": "pendente",
      "criada_em": "2025-01-01T10:00:00Z"
    }
  ]
}
```

## ⚙️ Regras importantes

- Usuários não acessam tasks de outros usuários
- Campo `user` não é aceito no payload
- Apenas admins acessam `/users`
- Filtros via `django-filter`
- Ordenação via `ordering`

 ---

## 🧠 Boas práticas aplicadas

- Isolamento de dados por usuário (`get_queryset`)
- Ownership automático (`perform_create`)
- Versionamento de API
- Múltiplos métodos de autenticação
- ViewSets + Routers
- Filtros e ordenação declarativos

 ---
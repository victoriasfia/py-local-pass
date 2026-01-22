# 🛡️ Cofre de Senhas (Secrets Vault)
Um gerenciador de senhas Full Stack simples, desenvolvido apenas para praticar conceitos de APIs REST e Containerização.
O projeto utiliza uma arquitetura de microsserviços, separando a lógica de segurança (Python) da interface do usuário (Node.js).

## 🚀 Tecnologias Utilizadas
## Backend (API & Segurança)
 Linguagem: Python 3.11
 Framework: FastAPI (para criação da API REST)
 Banco de Dados: SQLite (com persistência via Volume)
 Segurança: Criptografia Fernet (Symmetric Encryption)

## Frontend (Interface)
Runtime: Node.js
Framework: Express
View Engine: EJS (Embedded JavaScript)
Estilização: CSS Customizado

### Infraestrutura
Containerização: Docker / Podman
Orquestração: Docker Compose / Podman Compose

## ✨ Funcionalidades
🔐 Criptografia Real: As senhas são salvas no banco de dados como hash ilegível. Apenas a chave mestra pode descriptografá-las.

🔑 Master Key Única: Uma única chave para acessar todo o cofre.

👁️ Visualização Protegida: As senhas ficam ocultas até que o usuário solicite vê-las.

➕ CRUD Completo: Adicionar, Listar, Editar e Excluir senhas.

💾 Persistência de Dados: O banco de dados sobrevive ao reinício dos containers.

    📂 Estrutura do Projeto
    /
    ├── backend/              # Código do Backend (Python)
        ├── data/                 # Pasta onde o banco de dados (vault.db) é salvo
    │   ├── main.py           # API FastAPI e lógica de criptografia
    │   └── requirements.txt  # Dependências Python
    │
    ├── frontend/       # Código do Frontend (Node.js)
    │   ├── views/            # Telas (Login, Lista, Modal)
    │   ├── server.js         # Servidor Express
    │   └── package.json      # Dependências JS
    │
    ├── data/                 # Pasta onde o banco de dados (vault.db) é salvo
    ├── docker-compose.yml    # Orquestração dos containers
    ├── Dockerfile            # Construção da imagem do Backend
    └── README.md             # Documentação
### ⚙️ Como Rodar o Projeto
#### Pré-requisitos
*Ter o Docker ou Podman instalado.*

#### Passo a Passo
*Clone o repositório ou baixe os arquivos.*
*Inicie os serviços: Abra o terminal na pasta raiz do projeto e execute:*
### Se usar Podman:
    podman-compose up -d --build

### Se usar Docker:
    docker-compose up -d --build
Gere sua Chave Mestra (Apenas na 1ª vez): Antes de logar, você precisa criar uma chave.

Acesse o Swagger da API: 
**http://localhost:8000/docs**

Vá na rota GET /generate-key e clique em Try it out > Execute.
Copie a chave gerada (Ex: Ty16b1CA...). Salve-a em um local seguro!

Abra o navegador em: 
    **http://localhost:3000**

Cole sua chave mestra para entrar.

🛠️ Comandos Úteis
Parar os containers:

Bash
podman-compose down
Verificar logs (se der erro):

Bash
### Logs do Backend
    podman logs cofre-seguro

### Logs do Frontend (se estiver rodando via node localmente)
    node server.js
Forçar recriação (caso altere código):

### 📝 Notas de Aprendizado
Este projeto foi desenvolvido com foco em:

Entender como o Frontend (Node) se comunica com o Backend (Python) via HTTP.

Configurar CORS para permitir essa comunicação.

Manipular banco de dados SQLite com Python.

Configurar Volumes no Docker para não perder dados ao reiniciar.

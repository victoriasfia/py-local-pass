# 🛡️ Cofre de Senhas

Um gerenciador de senhas simples criado especificamente para praticar **FastAPI** e **Containerização (Podman)**. A interface foi gerada com auxílio de IA para facilitar os testes.

## 🚀Tecnologias

* **Backend:** Python 3.11, FastAPI, SQLite, Fernet (Criptografia)
* **Frontend:** Node.js, Express, EJS
* **Infra:** Podman Compose

## ⚙️ Como Rodar o Projeto

**1. Suba os containers:**
No terminal, na raiz do projeto, execute:
`podman-compose up -d --build`

**2. Gere sua Chave Mestra (Apenas na 1ª vez):**
* Acesse a documentação interativa (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)
* Vá na rota `GET /generate-key`, clique em *Try it out* > *Execute*.
* **Copie a chave gerada** (Ex: `Ty16b1CA...`) e guarde em um local seguro. Ela é a sua senha de acesso.

**3. Acesse a Interface:**
* Abra [http://localhost:3000](http://localhost:3000) no seu navegador.
* Cole a chave mestra que você gerou para entrar no cofre.


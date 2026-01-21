import os
import sqlite3
from fastapi import FastAPI, HTTPException, Header, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cryptography.fernet import Fernet
import base64

app = FastAPI (title = "Vault API", description="Cofre de senhas seguras")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Libera geral (para facilitar o teste)
    allow_credentials=True,
    allow_methods=["*"], # Libera GET, POST, DELETE...
    allow_headers=["*"],
)
#inciando banco de dados
def init_db():
    os.makedirs("data", exist_ok=True)    
    conn = sqlite3.connect("data/vault.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS secrets (
            name TEXT PRIMARY KEY,
            encrypted_content BLOB
        )
    """)
    conn.commit()
    conn.close()

init_db()

class SecretPayLoad(BaseModel):
    name : str
    password : str

@app.get("/")
def home ():
    return {"status" : "cofre trancado  seguro. use docs para interagir."}

@app.get("/generate-key")
def get_new_key():
    key = Fernet.generate_key()
    return {"master_key" : key.decode()}

@app.get("/secrets")
def list_secrets():
    conn = sqlite3.connect("data/vault.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM secrets")
    rows = cursor.fetchall()
    conn.close()
    
    # Transforma em lista simples: ['netflix', 'instagram']
    lista = [row[0] for row in rows]
    return {"secrets": lista}

@app.post("/secrets")
def save_secret (
    payload : SecretPayLoad,
    x_master_key : str = Header(..., description="Sua chave mestra de criptografia")
):
    try:
        key_bytes = x_master_key.encode() 
        f = Fernet(key_bytes)
        
        pwd_bytes = payload.password.encode()
        token = f.encrypt(pwd_bytes)
        
        os.makedirs("data", exist_ok=True)
        conn = sqlite3.connect("data/vault.db")
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO secrets (name, encrypted_content) VALUES (?, ?)", 
                    (payload.name, token))
        conn.commit()
        conn.close()
        
        return {"status": "Senha salva e criptografada com sucesso!"}
    
    except Exception as e:
        print(f"ERRO REAL: {e}") 
        raise HTTPException(status_code=400, detail=f"Erro na criptografia: {str(e)}")
    
@app.get("/secrets/{name}")
def retrieve_secret(
    name: str, 
    x_master_key: str = Header(..., description="A mesma chave usada para salvar")
):
    os.makedirs("data", exist_ok=True)    
    conn = sqlite3.connect("data/vault.db")
    cursor = conn.cursor()
    cursor.execute("SELECT encrypted_content FROM secrets WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException (status_code=404, detail="Segredo não encontrado")
    
    encrypted_data = row[0]

    try:
        f = Fernet(x_master_key.encode())
        decrypted_password = f.decrypt(encrypted_data).decode()
        return {"service": name, "password": decrypted_password}
    except Exception as e:
        print(f"Erro no decrypt: {e}")
        raise HTTPException (status_code=401, detail="Chave mestra incorreta. Acesso negado!")
    
@app.delete("/secrets/{name}")
def delete_secret(name: str):
    conn = sqlite3.connect('data/vault.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM secrets WHERE name =?", (name,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException (status_cod=404, detail="Senha secreta não econtrada")
    
    cursor.execute("DELETE FROM secrets WHERE name = ?", (name,))
    conn.commit()
    conn.close()

    return {"ststus": f"O segredo '{name}' foi detelado." }
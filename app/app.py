import sqlite3
from fastapi import FastAPI, HTTPSExceotion, Header, Body
from pydantic import BaseModel
from cryptography.fernet import Fernet
import base64

app = FastAPI (title = "Vault API", description="Cofre de senhas seguras")


def init_db():
    conn = sqlite3.connect("vault.db")
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


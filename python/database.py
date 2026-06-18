import sqlite3

DATABASE_NAME = "leads.db"


def get_connection():
    """
    Cria e retorna uma conexão com o banco.
    """
    return sqlite3.connect(DATABASE_NAME)

def get_all_leads():
    """
    Retorna todos os leads cadastrados.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leads")

    leads = cursor.fetchall()

    conn.close()

    return leads

def create_table():
    """
    Cria a tabela de leads caso ela não exista.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            principal_desafio TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_lead(lead: dict):
    """
    Insere um lead validado no banco.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO leads (
            nome,
            telefone,
            email,
            especialidade,
            principal_desafio
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        lead["nome"],
        lead["telefone"],
        lead["email"],
        lead["especialidade"],
        lead["principal_desafio"]
    ))


    conn.commit()

    lead_id= cursor.lastrowid

    conn.close()

    return lead_id
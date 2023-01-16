import sqlite3

conn = sqlite3.connect('financial.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE financial (
    ticker TEXT NOT NULL PRIMARY KEY,
    nome TEXT NOT NULL,
    ano INTEGER NOT NULL
);
""")

print('Tabela criada com sucesso!')

conn.close()
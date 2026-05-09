from database.conn import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   titulo TEXT NOT NULL,
   salario TEXT,
   modalidade TEXT,
   link TEXT UNIQUE
)
""")

conn.commit()

conn.close()

print("tabela criada")

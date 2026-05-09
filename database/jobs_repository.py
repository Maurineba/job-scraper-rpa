from bot.logger import logger

from .conn import get_connection

from sqlite3 import IntegrityError

def save_job(job):

   conn = get_connection()
   cursor = conn.cursor()

   try:
      cursor.execute("""
      INSERT INTO jobs (
         titulo,
         salario,
         modalidade,
         link
      )
      VALUES (?, ?, ?, ?)
      """,
      (
         job["titulo"],
         job["salario"],
         job["modalidade"],
         job["link"]
      ))
      conn.commit()
      logger.info(
         f"vaga salva: {job['titulo']}"
      )

   except IntegrityError:
      logger.warning(
         f"vaga duplicada: {job['titulo']}"
      )

   finally:
      conn.close()

def get_all_jobs():

   conn = get_connection()

   cursor = conn.cursor()

   cursor.execute("SELECT titulo, salario, modalidade, link FROM jobs")

   rows = cursor.fetchall()

   conn.close()

   return [
      {
        "titulo": r[0],
        "salario": r[1],
        "modalidade": r[2],
        "link": r[3]
      }
      for r in rows
   ]

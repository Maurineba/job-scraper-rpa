from bot.logger import logger
from utils.resolve_salary import resolve_salary
from utils.parse_salary import parse_salary

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


def get_jobs():
   logger.info("iniciando web scrap...")

   nav = webdriver.Chrome(
      service=Service(ChromeDriverManager().install()),
      options=options
   )

   jobs = []

   try:
      nav.get("https://www.nerdin.com.br/vagas-estagio-junior.php")

      for page in range(1, 10):

         items = nav.find_elements("class name", "vaga-card")
         logger.info(f"{len(items)} vagas encontradas")

         for i in items:
            try:
               name = i.find_element("class name", "vaga-titulo").text
               work_model = i.find_element("class name", "vaga-local").text
               salary = i.find_element("class name", "vaga-salario").text
               link = i.find_element("class name", "btn-ver-vaga")

               jobs.append({
                  "titulo": name,
                  "salario": parse_salary(resolve_salary(salary)),
                  "modalidade": work_model,
                  "link": link.get_attribute("href")
               })

            except Exception as e:
               logger.error(f"erro ao processar vaga: {e}")

         if page > 2:
            nav.get(f"https://www.nerdin.com.br/vagas-estagio-junior.php?pagina={page}")

   except Exception as e:
      logger.critical(f"erro geral no scraping: {e}")

   finally:
      logger.info("finalizando navegador")
      nav.quit()

   logger.info("fim do web scrap")

   return jobs

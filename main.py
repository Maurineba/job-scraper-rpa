from bot.scrapper import get_jobs
from bot.exporter import export_jobs
from database.jobs_repository import save_job

jobs = get_jobs()

for job in jobs:
   save_job(job)

export_jobs()

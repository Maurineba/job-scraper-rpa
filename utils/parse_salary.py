def parse_salary(value):
   if not value:
      return 0
   value = value.lower()
   if "a combinar" in value:
      return 0

   value = (
      value
      .replace("r$", "")
      .replace(".", "")
      .replace(",", ".")
      .strip()
   )
   try:
      if "-" in value:
         min_salary, max_salary = value.split("-")
         min_salary = float(min_salary.strip())
         max_salary = float(max_salary.strip())
         return (min_salary + max_salary) / 2
      return float(value)

   except ValueError:
       return 0
